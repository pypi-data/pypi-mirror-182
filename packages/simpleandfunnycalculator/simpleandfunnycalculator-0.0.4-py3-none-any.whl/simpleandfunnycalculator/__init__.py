UNIVARIATE_DATASET_NAMES_2018 = ['ArrowHead', 'BeetleFly',  'Yoga',  'Ham', 'MoteStrain',  'GunPointOldVersusYoung',  'OliveOil', 'Wine', 'FreezerSmallTrain', 'WordSynonyms', 'Lightning7',
                                 'Car', 'ProximalPhalanxTW', 'InsectWingbeatSound', 'InlineSkate', 'FaceAll', 'EOGVerticalSignal',    'Earthquakes', 'ACSF1', 'Adiac', 'Beef', 'BirdChicken', 
                                 'BME', 'CBF', 'Haptics', 'Plane', 'Strawberry', 'Coffee', 'Computers', 'CricketX', 'DiatomSizeReduction','DistalPhalanxTW',  'FiftyWords', 'Fish', 
                                 'ECG200',  'GunPoint', 'HandOutlines', 'EthanolLevel', 'FaceFour', ]


import os


def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def exp(a, b):
    return a**b

def display_path():
    directory = os.getcwd()
    print(directory)