import argparse

def get_input_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='pet_images/', 
                       choices=['pet_images/', 'uploaded_images/'],                         
                       help='Path to the folder of pet images: pet_images , uploaded_images') 
    parser.add_argument('--arch', type=str, default='vgg',
                       choices=['vgg', 'alexnet', 'resnet'], 
                       help='CNN model architecture to use: ResNet, AlexNet, or VGG')
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                       help='File that contains the list of valid dognames')
    in_arg = parser.parse_args()
    return in_arg