#!/bin/sh

# bash-скрипт, последовательно запускающий все python-скрипты.
python3 ./mlops-demo/lab1/data_creation.py
python3 ./mlops-demo/lab1/model_preprocessing.py
python3 ./mlops-demo/lab1/model_preparation.py
python3 ./mlops-demo/lab1/model_testing.py
