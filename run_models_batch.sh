python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > Results/resnet_pet-images.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > Results/alexnet_pet-images.txt
python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt > Results/vgg_pet-images.txt
