import numpy as np
import os
import pandas as pd
import itertools

import keras 

from keras.models import load_model
from keras.regularizers import l2
from tensorflow.python.client import device_lib as _device_lib
from pysster.One_Hot_Encoder import One_Hot_Encoder

from seqprop import *
from seqprop.generator import *
from seqprop.predictor import *
from seqprop.optimizer import *

from utils import *

def _get_one_hot_encoding(seq):
    alph_letters = sorted('ACGT')
    alph = list(alph_letters)
    one = One_Hot_Encoder(alph_letters)
    one_hot_seq = one.encode(seq)
    return one_hot_seq

def load_saved_predictor(model_path):
    saved_model = load_model(model_path)

    def _initialize_predictor_weights(predictor_model, saved_model=saved_model):
        # Load pre-trained model
        predictor_model.get_layer('conv_0').set_weights(saved_model.get_layer('conv_0').get_weights())
        predictor_model.get_layer('conv_0').trainable = False

        predictor_model.get_layer('conv_1').set_weights(saved_model.get_layer('conv_1').get_weights())
        predictor_model.get_layer('conv_1').trainable = False

        predictor_model.get_layer('dense_0').set_weights(saved_model.get_layer('dense_0').get_weights())
        predictor_model.get_layer('dense_0').trainable = False

        predictor_model.get_layer('dense_1').set_weights(saved_model.get_layer('dense_1').get_weights())
        predictor_model.get_layer('dense_1').trainable = False

        predictor_model.get_layer('dense_2').set_weights(saved_model.get_layer('dense_2').get_weights())
        predictor_model.get_layer('dense_2').trainable = False

        predictor_model.get_layer('on_output').set_weights(saved_model.get_layer('on_output').get_weights())
        predictor_model.get_layer('on_output').trainable = False

    def _load_predictor_func(sequence_input):
        # input space parameters
        seq_len = 59
        num_letters = 4  # num nt

        # define new model definition (same architecture except modified input)
        dropout_rate = 0.1
        reg_coeff = 0.0001
        hidden_layer_choices = {5: (150, 60, 15), }
        conv_layer_parameters = [(5, 10), (3, 5), ]
        hidden_layers = hidden_layer_choices[5]

        reshaped_input = Reshape(target_shape=(seq_len, num_letters), name='reshaped_input')(sequence_input)
        prior_layer = reshaped_input
        for idx, (kernel_width, num_filters) in enumerate(conv_layer_parameters):
            conv_layer = Conv1D(filters=num_filters, kernel_size=kernel_width, padding='same', name='conv_' + str(idx))(
                prior_layer)  # mimic a kmer
            prior_layer = conv_layer
        H = Flatten(name='flatten')(prior_layer)
        for idx, h in enumerate(hidden_layers):
            H = Dropout(dropout_rate, name='dropout_' + str(idx))(H)
            H = Dense(h, activation='relu', kernel_regularizer=l2(reg_coeff), name='dense_' + str(idx))(H)
        out_onoff = Dense(1, activation="linear", name='on_output')(H)

        predictor_inputs = []
        predictor_outputs = [out_onoff]

        return predictor_inputs, predictor_outputs, _initialize_predictor_weights

    return _load_predictor_func

def loss_func(predictor_outputs):
    '''
    build loss function
    '''
    # define target on/off values
    target_onoff = 1
    target = [[target_onoff], ] # keep in this format in case you want to adapt for separate on and off predictions
    pwm_logits, pwm, sampled_pwm, predicted_out = predictor_outputs

    target_out = K.tile(K.constant(target), (K.shape(sampled_pwm)[0], 1))
    target_cost = (target_out - predicted_out) ** 2
    return K.mean(target_cost, axis=-1)

def run_gradient_ascent(input_toehold_seq, original_out):
    seq_len = 59
    num_samples = 1
    # template specifying what to modify and what not (biological constaints)
    switch = 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN'
    rbs = 'AACAGAGGAGA'
    start_codon = 'ATG'
    stem1 = 'NNNNNN'#'XXXXXX'
    stem2 = 'NNNNNNNNN'#'XXXXXXXXX'
    model_dir = 'checkpoint/'
    final_model_path = model_dir + 'cnn_ONE_Output_Model.h5'
    bio_constraints = switch + rbs + stem1 + start_codon + stem2
    # build generator network
    # Generator that samples a single one-hot sequence per trainable PWM
    _, seqprop_generator = build_generator(seq_length=seq_len, n_sequences=num_samples, batch_normalize_pwm=True,
                                           init_sequences=[input_toehold_seq],
                                           sequence_templates=[bio_constraints])  # batch_normalize_pwm=True)

    # build predictor network and hook it on the generator PWM output tensor
    # Predictor that predicts the function of the generated input sequence
    _, seqprop_predictor = build_predictor(seqprop_generator, load_saved_predictor(final_model_path),
                                           n_sequences=num_samples, eval_mode='pwm')

    # Build Loss Model (In: Generator seed, Out: Loss function)
    _, loss_model = build_loss_model(seqprop_predictor, loss_func, )

    # Specify Optimizer to use
    opt = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999)

    # Compile Loss Model (Minimize self)
    loss_model.compile(loss=lambda true, pred: pred, optimizer=opt)

    # Fit Loss Model
    # seed_input = np.reshape([X[0]], [1,59,4,1]) # any input toehold to be modified

    callbacks = [
        EarlyStopping(monitor='loss', min_delta=0.001, patience=5, verbose=2, mode='auto'),
        # SeqPropMonitor(predictor=seqprop_predictor)#, plot_every_epoch=True, track_every_step=True, )#cse_start_pos=70, isoform_start=target_cut, isoform_end=target_cut+1, pwm_start=70-40, pwm_end=76+50, sequence_template=sequence_template, plot_pwm_indices=[0])
    ]

    num_epochs = 50
    train_history = loss_model.fit([], np.ones((1, 1)), epochs=num_epochs, steps_per_epoch=1000, callbacks=callbacks)

    # Retrieve optimized PWMs and predicted (optimized) target
    _, optimized_pwm, optimized_onehot, predicted_out = seqprop_predictor.predict(x=None, steps=1)
    print('Original ON/OFF:', original_out)
    print('Predicted ON/OFF: ', predicted_out)

    return optimized_pwm, optimized_onehot, predicted_out

def invert_onehot(oh_seq):
    alph_letters = sorted('ACGT')
    alph = list(alph_letters)
    return ''.join(alph[idx] for idx in np.argmax(oh_seq,axis=1))

def get_model():
    model_dir = 'checkpoint/'
    final_model_path = model_dir + 'cnn_ONE_Output_Model.h5'
    final_weights_path = model_dir + 'cnn_ONE_Output_Model_weights.h5'
    model = load_model(final_model_path)
    model.load_weights(final_weights_path)
    return model

def optimize_toehold(seqs,num_of_optimization_rounds):
    local_device_protos = _device_lib.list_local_devices()
    gpu_list = [x.name[-1] for x in local_device_protos if 'GPU' in x.device_type]
    gpu_str = ",".join(gpu_list)

    os.environ["CUDA_VISIBLE_DEVICES"] = gpu_str
    # print("Finish loading!")
    # enter a .csv with sequences

    #20 sequences takes ~2 hours to optimize, given compute power,
    # so simplify to just 2 sequences here.
    num_seqs = len(seqs)
    X = np.stack([_get_one_hot_encoding(s) for s in seqs]).astype(np.float32)

    model = get_model()
    storm_pred_onoff_vals = model.predict(X)
    y = np.array(storm_pred_onoff_vals).astype(np.float32)


    optimized_seqs = [] # store the converted sequences to be tested
    predicted_targets = [] # store the original and predicted target values

    # run given optimization rounds for each sequence- part of STORM algorithm
    for idx, (toehold_seq, original_out) in enumerate(zip(seqs, y)):
        for i in range(0, num_of_optimization_rounds):
            _, optimized_onehot, predicted_out = run_gradient_ascent(toehold_seq, original_out)
            predicted_targets.append(predicted_out)
            new_seq = invert_onehot(np.reshape(optimized_onehot, [59,4]))
            optimized_seqs.append(new_seq)

    #Part 8. Change toeholds to adhere to basepairing and toehold structure- post processing
    data_df = pd.DataFrame()
    data_df['old_switches'] = list(itertools.chain.from_iterable(itertools.repeat(x, num_of_optimization_rounds) for x in seqs))
    data_df['old_predicted_onoff'] = list(itertools.chain.from_iterable(itertools.repeat(x, num_of_optimization_rounds) for x in storm_pred_onoff_vals))
    data_df['new_switch'] = optimized_seqs
    data_df['predicted_onoff'] = predicted_targets
    # data_df['optimized_pwm'] = optimized_pwms

    # convert new switches to bp complementarity / toehold structure
    new_fixed_switches = []
    for toehold in data_df['new_switch']:
        base_30nt = toehold[0:30]
        # print('checking for rev comp: ', check_rev_comp(toehold))
        # print('checking for rbs and start codon: ', check_rbs_and_start(toehold))
        new_toehold = turn_switch_to_toehold(base_30nt)
        # print(new_toehold)
        # print('checking for rev comp: ', check_rev_comp(new_toehold))
        # print('checking for rbs and start codon: ', check_rbs_and_start(new_toehold))
        new_fixed_switches.append(new_toehold)
    data_df['NEW_fixed_switch'] = new_fixed_switches
    X = np.stack([_get_one_hot_encoding(s) for s in new_fixed_switches]).astype(np.float32)

    predictions = model.predict(X)
    #print(predictions)

    data_df['NEW_onoff_preds'] = np.reshape(predictions, [num_seqs*num_of_optimization_rounds,])
    best_seqs = pd.DataFrame()
    onoff_col = data_df.columns.get_loc("NEW_onoff_preds")

    # cull so we have just the best out of each 5
    for i in range(0, num_seqs):
        start = i * num_of_optimization_rounds
        end = start + num_of_optimization_rounds
        best_toehold_so_far = data_df.iloc[start,:]
        for j in range(start+1, end):
            curr_toehold = data_df.iloc[j,:]
            if (data_df.iloc[j, onoff_col] > data_df.iloc[start, onoff_col]):
                best_toehold_so_far = curr_toehold
        best_seqs = pd.concat([best_seqs, best_toehold_so_far], axis = 1)
    best_seqs = best_seqs.transpose()

    # change name if you would like
    out_dir = 'data/'
    best_seqs.to_csv(out_dir + 'toeholds_optimized.csv')
    return list(best_seqs['NEW_fixed_switch']),list(best_seqs['NEW_onoff_preds'])
    
if __name__ == "__main__":
    seqs = ['AAATTTTATAACCGTTAATATTGATAAAAAAACAGAGGAGATTTTTAATGATATTAACG','ATCTAAGACTAGTGATTTTCTGACTTTCTTAACAGAGGAGAAAGAAAATGAGAAAATCA']
    optimized_seqs, new_onoff = optimize_toehold(seqs,2)
    print(optimize_toehold)
    print(new_onoff)