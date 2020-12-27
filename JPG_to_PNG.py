#!/bin/Python3
import os
from sys import argv
from PIL import Image

# grab first and second argument
if len(argv) != 3:
    print("Requires three positional arguments.")
    exit(1)

source_folder = argv[1]
output_folder = argv[2]
print(source_folder, output_folder)

# check is new/ exist, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# loop trough pokedex
for file in os.listdir(source_folder):
    img = Image.open(f'{source_folder}{file}')
    img.save(output_folder+file.replace('jpg', 'png'), 'png')

