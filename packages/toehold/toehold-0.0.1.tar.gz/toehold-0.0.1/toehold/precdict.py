import numpy as np
import pickle
from keras.models import load_model
from pysster.One_Hot_Encoder import One_Hot_Encoder


def _get_one_hot_encoding(seq):
    alph_letters = sorted('ATCG')
    # one-hot encode
    one = One_Hot_Encoder(alph_letters)
    one_hot_seq = one.encode(seq)
    return one_hot_seq

def get_model():
    model_dir = 'checkpoint/'
    final_model_path = model_dir + 'MLP_THREE_Output_Model.h5'
    final_weights_path = model_dir + 'MLP_Three_Output_Model_weights.h5'
    model = load_model(final_model_path)
    model.load_weights(final_weights_path)
    return model

def Infer_ON(seqs):
    model = get_model()
    scaler = pickle.load(open('data/scaler.pkl', 'rb'))
    data_input = np.stack([_get_one_hot_encoding(s) for s in seqs]).astype('float32')
    pred = model.predict(data_input)
    pred = scaler.inverse_transform(pred)
    return pred[:,0]

def Infer_OFF(seqs):
    model = get_model()
    scaler = pickle.load(open('data/scaler.pkl', 'rb'))
    data_input = np.stack([_get_one_hot_encoding(s) for s in seqs]).astype('float32')
    pred = model.predict(data_input)
    pred = scaler.inverse_transform(pred)
    return pred[:,1]

def Infer_ONOFF(seqs):
    model = get_model()
    scaler = pickle.load(open('data/scaler.pkl', 'rb'))
    data_input = np.stack([_get_one_hot_encoding(s) for s in seqs]).astype('float32')
    pred = model.predict(data_input)
    pred = scaler.inverse_transform(pred)
    return pred[:,2]

if __name__ == "__main__":
    seqs = ['AAAATAAGTTAGCTGGATATTGATAAATTTAACAGAGGAGAAAATTTATGAATATCCAG','ATAAACAAAATGGATATTATAGACAAAAAAAACAGAGGAGATTTTTTATGTATAATATC','GATGTTACAAACGATAATATAGACAAAAATAACAGAGGAGAATTTTTATGTATATTATC']
    print("ON value:",Infer_ON(seqs))
    print("OFF value:",Infer_OFF(seqs))
    print("ONOFF value:",Infer_ONOFF(seqs))