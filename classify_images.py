from classifier import classifier 
def classify_images(images_dir, results_dic, model):
    for key in results_dic:
        image_classification = classifier(images_dir + key, model)
        lower_case_classifier = image_classification.lower()
        classifier_label = lower_case_classifier.strip()
        truth = results_dic[key][0]
        if truth in classifier_label:
            results_dic[key].extend([classifier_label, 1])
        else:
            results_dic[key].extend([classifier_label, 0])
        print(f"Image: {key}, Predicted: {classifier_label}, Correct: {truth}, Match: {truth in classifier_label}")