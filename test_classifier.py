from classifier import classifier 
test_image="pet_images/Collie_03797.jpg"
model = "vgg"
image_classification = classifier(test_image, model)
print("\nResults from test_classifier.py\nImage:", test_image, "using model:",
      model, "was classified as a:", image_classification)