from classifier import classifier
import os  # Import the os module for path manipulation

def classify_images(images_dir, results_dic, model):
    for key, value in results_dic.items(): 
        # Use os.path.join() to construct the correct file path
        image_path = os.path.join(images_dir, key) 
        image_classification = classifier(image_path, model)
        lower_case_classifier = image_classification.lower()
        classifier_label = lower_case_classifier.strip()
        truth = value[0]

        if truth in classifier_label:
            value.extend([classifier_label, 1])
        else:
            value.extend([classifier_label, 0])

        print(f"Image: {key}, Predicted: {classifier_label}, Correct: {truth}, Match: {truth in classifier_label}")