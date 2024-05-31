#!/bin/bash

# Create the Results directory if it doesn't exist
mkdir -p Results

# Loop through each model architecture
for arch in resnet alexnet vgg; do
  # Build the output filename
  output_file="Results/${arch}_uploaded-images.txt"

  # Run the Python script with the specified arguments
  # and redirect output to the output file
  python check_images.py --dir uploaded_images/ --arch ${arch} --dogfile dognames.txt > ${output_file}

  # Print a message to the terminal indicating completion
  echo "Results for ${arch} saved to ${output_file}"
done