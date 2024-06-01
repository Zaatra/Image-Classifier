# Udacity Project - AI Programming With Python - Image Classifier
This repository provides a simple image classification model built using TensorFlow and Keras. The model is trained on a dataset of images and can be used to classify new images into different categories.
## Installation
### Clone the repository:
`git clone https://github.com/Zaatra/Image-Classifier.git`
### Install dependencies:
`pip install -r requirements.txt`
## Usage
### Prepare your dataset:
* Organize your images into folders corresponding to their respective classes.
* Ensure the images are in a format supported by TensorFlow (e.g., JPG, PNG).
### Use The Model:
* Run Check_images.py with the following arguments
    * --arch : (alexnet , vgg , resnet).
    * --dir : (pet_images/ , uploaded_images/).
    * --dogfile : (dognames.txt).
## Known Bugs
* This is a simple project and may not perform optimally for complex image classification tasks.
* The model has not been thoroughly tested with various datasets and may require further tuning for specific use cases.
## Contributing
Contributions are welcome! If you find any bugs, have suggestions for improvements, or want to add new features, feel free to create a pull request.
## License
This project is licensed under the MIT License.