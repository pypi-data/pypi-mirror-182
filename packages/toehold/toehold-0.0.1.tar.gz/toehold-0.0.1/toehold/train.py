import numpy as np
import pandas as pd
from subprocess import call

from scipy import stats, interp

from keras.layers import Activation, Conv1D, Conv2D, Reshape, BatchNormalization, Dropout, Flatten, Dense, merge, Input
from keras.models import Model
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping

import sklearn
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.preprocessing import QuantileTransformer


# Progress Bar
from tqdm import tqdm

# Warnings
import warnings
from pysster.One_Hot_Encoder import One_Hot_Encoder
warnings.filterwarnings("ignore")

#Visualization mode
#%matplotlib ipympl

## Define helper function to copy full directory for backups
def copy_full_dir(source, target):
    call(['cp', '-a', source, target])  # Unix


# Get number of available GPUs
def get_available_gpus():
    from tensorflow.python.client import device_lib
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']

alph_letters = sorted('ATCG')
alph = list(alph_letters)
# one-hot encode
one = One_Hot_Encoder(alph_letters)
def _get_one_hot_encoding(seq):
    one_hot_seq = one.encode(seq)
    return one_hot_seq


def custom_r2_loss(y_true, y_pred):
    from keras import backend as K
    SS_res =  K.sum(K.square( y_true-y_pred ))
    SS_tot = K.sum(K.square( y_true - K.mean(y_true) ) )
    return (SS_res/(SS_tot + K.epsilon()))

#Definition of Custom metric as loss related to Weigted Mean Absolute error
#  Improvement points towards zero, but penalizes loss for small values and improves it for larger values
def custom_wmae_loss(y_true, y_pred):
    from keras import backend as K
    weightedMAE = K.abs((y_true-y_pred)*y_true) #Increase loss for large ON or OFF values -- Skews focus of distribution right
    return weightedMAE
def r2(x, y):
    return stats.pearsonr(x, y)[0] ** 2
def compute_metrics(preds_y, true_y):
    preds_y = np.squeeze(preds_y)
    true_y = np.squeeze(true_y)
    r2_score = r2(preds_y, true_y)
    pearson_corr = stats.pearsonr(preds_y, true_y)[0]
    spearman_corr = stats.spearmanr(preds_y, true_y)[0]
    mse_val = sklearn.metrics.mean_squared_error(preds_y, true_y)
    mae_val = sklearn.metrics.mean_absolute_error(preds_y, true_y)
    print('R2: ', r2_score)
    print('Pearson: ', pearson_corr)
    print('Spearman: ', spearman_corr)
    return [r2_score, pearson_corr, spearman_corr, mse_val, mae_val]


# Define path to load desired Toehold dataset file (.csv)
data_filename = "newQC_toehold_data.csv"
data_path = 'data/' + data_filename
data = pd.read_csv(data_path)

# Fix random seed for reproducibility
seed = 7
np.random.seed(seed)  # Seed can be any number

### Datata Sequence ID selection
id_data = data['sequence_id']

### Toehold Switch dataset input/output columns for selection
input_cols = 'switch_sequence'
output_cols = ['on_value', 'off_value', 'onoff_value']
qc_levels = [1.1]
doTrain = True
loss_init = 'mae' #'logcosh', #'mse', 'mae', 'r2'
num_folds = 10
verbose_init = True
evaluate  = True
display_init = True
### Define data scaler (if any)
scaler_init = True
scaler = QuantileTransformer(output_distribution='uniform')
### DEFINE MODEL NAME (e.g. MLP, CNN, LSTM, etc.)
model_name = 'MLP_1D'


df_data_output = data[data.onoff_qc >= 1.1]
df_data_output = df_data_output[output_cols]
df_data_output = df_data_output.dropna(subset=output_cols)
data_output = df_data_output.values.astype('float32')
data_output_orig = data_output
data_output = scaler.fit_transform(data_output)
data_input = data[input_cols][df_data_output.index.values]
data_input = np.stack([_get_one_hot_encoding(s) for s in data_input]).astype('float32')

#Show sample of dataframe structure
print(data.head())


### Function to create Keras MLP for regression prediction
def create_mlp(width, height, regress=False):
    # Define our MLP network
    inputShape = (width, height)  # DNA/RNA input sequence (one hot encoded)
    inputs = Input(shape=inputShape)
    chanDim = -1
    dropout_init = 0.2

    # Define dense layers
    x = inputs
    x = Conv1D(filters=10, kernel_size=5, padding='same', name='conv_1')(x)
    x = Conv1D(filters=5, kernel_size=3, padding='same', name='conv_2')(x)
    x = Flatten()(x)
    x = Dense(256, activation="relu", name='dense_1')(x)
    x = BatchNormalization(axis=chanDim, name='batchnorm_1')(x)
    x = Dropout(dropout_init,name='drop_1')(x)


    x = Dense(128, activation="relu", name='dense_2')(x)
    x = BatchNormalization(axis=chanDim, name='batchnorm_2')(x)
    x = Dropout(dropout_init,name='drop_2')(x)

    x = Dense(64, activation="relu", name='dense_3')(x)
    x = BatchNormalization(axis=chanDim, name='batchnorm_3')(x)
    x = Dropout(dropout_init,name='drop_3')(x)

    x = Dense(32, activation="relu", name='dense_4')(x)
    x = BatchNormalization(axis=chanDim, name='batchnorm_4')(x)
    x = Dropout(dropout_init,name='drop_4')(x)

    # Check to see if the regression node should be added
    if regress:
        x = Dense(len(output_cols), activation="linear", name='dense_5')(x)

    # Construct the Model
    model = Model(inputs=[inputs], outputs=[x])
    #model = Model(inputs, x)
    # Return the model
    return model

##############################################Run k fold to obtain metrics################################################
avg_metric_folds_on = []
avg_metric_folds_off = []
avg_metric_folds_onoff = []
std_metric_folds_on = []
std_metric_folds_off = []
std_metric_folds_onoff = []

cv_scores_on = []
cv_scores_off = []
cv_scores_onoff = []
seed = 0 # set for reproducability
np.random.seed(seed)
patience_init = 15  # Number of epochs to wait for no model improvement before early stopping a training
epochs_init = 300  # Max number of epochs to perform (to cap training time)
validation_spit_init = 0.1
batch_size_init = 128
#   valuable metrics for regression evaluation
es = EarlyStopping(monitor='val_loss', patience=patience_init, verbose=1)
opt = Adam(lr=0.001)  # epsilon=1e-1 for POISSON loss
(width, height) = np.shape(data_input[0])
kfold = KFold(n_splits=num_folds, shuffle=True, random_state= 0)
fold_count = 0
for train, test in kfold.split(data_input, data_output):
    print('Beginning fold #', fold_count)
    #X_val, X_test, y_val, y_test = train_test_split(data_input[test], data_output[test], test_size=0.5)
    model = create_mlp(width, height, regress=True)
    #opt = Adam(lr=0.001, epsilon=None, decay=1e-3 / 200, amsgrad=False)
    if loss_init == "r2":
        model.compile(loss=custom_r2_loss, optimizer=opt, metrics=['mse', 'mae', 'mape', 'cosine', 'acc', custom_r2_loss])
    elif loss_init == "wmae":
        model.compile(loss=custom_wmae_loss, optimizer=opt,metrics=['mse', 'mae', 'mape', 'cosine', 'acc', custom_wmae_loss])
    else:
        model.compile(loss=loss_init, optimizer=opt, metrics=['mse', 'mae'])

    model_history = model.fit(data_input[train], data_output[train],validation_split=0.1, epochs=epochs_init,
                            batch_size=batch_size_init, callbacks=[es], verbose=verbose_init)

    testX_Preds = model.predict(data_input[test])
    if scaler_init == True:
        testY = scaler.inverse_transform(data_output[test])
        testX_Preds = scaler.inverse_transform(testX_Preds)

    model_path = 'checkpoint/'
    
    print('--- ON Metrics ---')
    on_metrics = compute_metrics(testX_Preds[:,0], testY[:, 0])
    print('--- OFF Metrics ---')
    off_metrics = compute_metrics(testX_Preds[:,1], testY[:, 1])
    print('--- ONOFF Metrics ---')
    onoff_metrics = compute_metrics(testX_Preds[:,2], testY[:, 2])
    # save raw csv scores
    cv_scores_on.append(on_metrics)
    cv_scores_off.append(off_metrics)
    cv_scores_onoff.append(onoff_metrics)
    fold_count += 1
    del model
# save K-fold metrics
# generate average scores
avg_metric_folds_on = np.mean(cv_scores_on, axis=0)  # avg over columns
std_metric_folds_on = np.std(cv_scores_on, axis=0)  # st dev over columns
avg_metric_folds_off = np.mean(cv_scores_off, axis=0)  # avg over columns
std_metric_folds_off = np.std(cv_scores_off, axis=0)  # st dev over columns
avg_metric_folds_onoff = np.mean(cv_scores_onoff, axis=0)  # avg over columns
std_metric_folds_onoff = np.std(cv_scores_onoff, axis=0)  # st dev over columns
# bad code: need to convert to np array for saving later
avg_metric_folds_on = np.array(avg_metric_folds_on)
avg_metric_folds_off = np.array(avg_metric_folds_off)
avg_metric_folds_onoff = np.array(avg_metric_folds_onoff)
std_metric_folds_on = np.array(std_metric_folds_on)
std_metric_folds_off = np.array(std_metric_folds_off)
std_metric_folds_onoff = np.array(std_metric_folds_onoff)
cv_scores_on = np.array(cv_scores_on)
cv_scores_off = np.array(cv_scores_off)
cv_scores_onoff = np.array(cv_scores_onoff)
on_df = pd.DataFrame({'R2': cv_scores_on[:, 0], 'Pearson': cv_scores_on[:, 1],
                      'Spearman': cv_scores_on[:, 2],
                      'MSE': cv_scores_on[:, 3], 'MAE': cv_scores_on[:, 4],
                    'R2 (mean)': avg_metric_folds_on[0], 'Pearson (mean)': avg_metric_folds_on[1],
                      'Spearman (mean)': avg_metric_folds_on[2],
                      'MSE (mean)': avg_metric_folds_on[3], 'MAE (mean)': avg_metric_folds_on[4],
                      'R2 (std)': std_metric_folds_on[0], 'Pearson (std)': std_metric_folds_on[1],
                      'Spearman (std)': std_metric_folds_on[2],
                      'MSE (std)': std_metric_folds_on[3], 'MAE (std)': std_metric_folds_on[4]
                      })

on_df.to_csv(model_path + '/K-Fold-ON-metrics.csv')

off_df = pd.DataFrame({'R2': cv_scores_off[:, 0], 'Pearson': cv_scores_off[:, 1],
                      'Spearman': cv_scores_off[:, 2],
                      'MSE': cv_scores_off[:, 3], 'MAE': cv_scores_off[:, 4],
                    'R2 (mean)': avg_metric_folds_off[0], 'Pearson (mean)': avg_metric_folds_off[1],
                      'Spearman (mean)': avg_metric_folds_off[2],
                      'MSE (mean)': avg_metric_folds_off[3], 'MAE (mean)': avg_metric_folds_off[4],
                      'R2 (std)': std_metric_folds_off[0], 'Pearson (std)': std_metric_folds_off[1],
                      'Spearman (std)': std_metric_folds_off[2],
                      'MSE (std)': std_metric_folds_off[3], 'MAE (std)': std_metric_folds_off[4]
                      })
off_df.to_csv(model_path + '/K-Fold-OFF-metrics.csv')

onoff_df = pd.DataFrame({'R2': cv_scores_onoff[:, 0], 'Pearson': cv_scores_onoff[:, 1],
                      'Spearman': cv_scores_onoff[:, 2],
                      'MSE': cv_scores_onoff[:, 3], 'MAE': cv_scores_onoff[:, 4],
                    'R2 (mean)': avg_metric_folds_onoff[0], 'Pearson (mean)': avg_metric_folds_onoff[1],
                      'Spearman (mean)': avg_metric_folds_onoff[2],
                      'MSE (mean)': avg_metric_folds_onoff[3], 'MAE (mean)': avg_metric_folds_onoff[4],
                      'R2 (std)': std_metric_folds_onoff[0], 'Pearson (std)': std_metric_folds_onoff[1],
                      'Spearman (std)': std_metric_folds_onoff[2],
                      'MSE (std)': std_metric_folds_onoff[3], 'MAE (std)': std_metric_folds_onoff[4]
                      })
onoff_df.to_csv(model_path + '/K-Fold-ONOFF-metrics.csv')



##############################################train a final model####################################################
# train_size = 0.85
# X_train, X_val, y_train, y_val = train_test_split(data_input, data_output, test_size=1 - train_size)

# build model
model = create_mlp(width, height, regress=True)
    #opt = Adam(lr=0.001, epsilon=None, decay=1e-3 / 200, amsgrad=False)
if loss_init == "r2":
    model.compile(loss=custom_r2_loss, optimizer=opt, metrics=['mse', 'mae', 'mape', 'cosine', 'acc', custom_r2_loss])
elif loss_init == "wmae":
    model.compile(loss=custom_wmae_loss, optimizer=opt,metrics=['mse', 'mae', 'mape', 'cosine', 'acc', custom_wmae_loss])
else:
    model.compile(loss=loss_init, optimizer=opt, metrics=['mse', 'mae'])

model.fit(data_input, data_output, validation_split=0.2, epochs=epochs_init,
                                       batch_size=batch_size_init, callbacks=[es], verbose=verbose_init)
model_path = 'checkpoint/'

model.save(model_path + '/MLP_THREE_Output_Model.h5')
model.save_weights(model_path + '/MLP_Three_Output_Model_weights.h5')

