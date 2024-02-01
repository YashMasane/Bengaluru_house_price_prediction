import json
import pickle
import numpy as np
import sklearn

__locations = None
__column_data = None
__model = None


def get_location_names():
    load_saved_data()
    return __locations


def load_saved_data():
    global __column_data
    global __locations

    with open('./artifacts/column.json', 'r') as f:
        __column_data = json.load(f)['data_columns']
        __locations = __column_data[3:]

    global __model
    with open('./artifacts/bangalore_house_price_prediction.pickle', 'rb') as f:
        __model = pickle.load(f)


def get_estimated_price(location, sqft, bath, bhk):
    load_saved_data()
    global __column_data
    global __model
    try:
        loc_index = __column_data.index(location.title())
    except:
        loc_index = -1

    x = np.zeros(len(__column_data))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


if __name__ == '__main__':
    load_saved_data()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location
