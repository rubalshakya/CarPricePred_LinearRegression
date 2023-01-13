import config
import json
import pickle
import numpy as np


class CarPricePrediction():

    def __init__(self,form_dict):
        self.form_dict = form_dict


    def load_model(self):
        with open(config.LABEL_ENCODED_DATA_PATH , "r") as f:
            self.json_data = json.load(f)
        with open(config.MODEL_FILE_PATH , "rb") as f:
            self.model = pickle.load(f)

    def get_PredCarPrice(self):
        self.load_model()
        test_array = []       
        for k,v in self.form_dict.items():
            if k not in self.json_data.keys():
                test_array.append(float(v))
            else:
                test_array.append(float(self.json_data[k][v]))
        
        # print(test_array)
        self.result = round(self.model.predict([np.array(test_array)])[0], 2)
        
        return self.result