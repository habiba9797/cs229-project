#!/bin/bash

# This is a script to run some experiments for simple cnn model with binarized data that's either 0 or 1.

# Note this assumes that you've pre-downloaded the data for the different classes
# already.

# Run first experiment on {3, 10, 50} classes.

set -x
MAX_ITER=100
echo "Running experiment on 3 classes !"
python3 cnn.py --max_iter=$MAX_ITER --data_folder=data/numpy_bitmap_3/ --experiment_name="binarized_data_3_classes" --using_binarization=True "$@"

# Run experiment on 10 classes
echo "Running experiment on 10 classes !"
python3 cnn.py --max_iter=$MAX_ITER --data_folder=data/numpy_bitmap_10/ --experiment_name="binarized_data_10_classes" --using_binarization=True "$@"

# Run experiment on 50 classes
echo "Running experiment on 50 classes !"
python3 cnn.py --max_iter=$MAX_ITER --data_folder=data/numpy_bitmap_50/ --experiment_name="binarized_data_50_classes" --using_binarization=True "$@"

# All done
echo "All done !"
