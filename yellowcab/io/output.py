from .utils import get_data_path
import os
import pickle


def save_model(model,filename):
    pickle.dump(model, open(os.path.join(get_data_path(), "output", filename), 'wb'))
