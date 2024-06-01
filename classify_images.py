from classifier import classifier
import os
from tqdm import tqdm  # Import tqdm for the progress bar

def classify_images(images_dir, results_dic, model):
    """
    Classifies images using a CNN model architecture.
    
    Parameters:
        images_dir - String - Path to the folder containing pet images.
        results_dic - Dictionary - Results dictionary for classified images.
        model - String - Model architecture to use for classification.
    
    Returns:
        None - modifies the results_dic dictionary in place
    """
    # Use tqdm to create a progress bar
    for key, value in tqdm(results_dic.items(), desc="Classifying Images"):
        image_path = os.path.join(images_dir, key)
        image_classification = classifier(image_path, model)
        lower_case_classifier = image_classification.lower()
        classifier_label = lower_case_classifier.strip()
        truth = value[0]

        if truth in classifier_label:
            value.extend([classifier_label, 1])
        else:
            value.extend([classifier_label, 0])