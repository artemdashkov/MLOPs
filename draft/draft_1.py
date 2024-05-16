import numpy as np
import os
import pandas as pd
data_length = 10


def create_data(base_value, noise_value):
    """
    Генерация псевдослучайных данных
    :param base_value:  основная величина признака без шума
    :param noise_value: амплитуда шума
    :return: массив numpy размером data_length на 1
    """
    return np.array([int(base_value * x) +
                     int(np.random.choice([-1, 1]) * noise_value * np.random.rand())
                     for x in np.random.rand(data_length)])

data_1 = create_data(20, 4)
print(data_1)
