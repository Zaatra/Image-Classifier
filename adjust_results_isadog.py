# adjust_results_isadog.py
def adjust_results_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to include whether or not an image is of a dog
    and whether or not the classifier correctly classified the image.

    Args:
      results_dic (dict): Dictionary with 'key' as image filename and 'value' as a 
                          List. The list contains for one image, the pet image label, 
                          confidence score, if it's a match to the label, if it's a dog image,
                          and if the classifier identified it as a dog image.
      dogfile (str): Full path to a file containing dog names, one per line.

    Returns:
      None - Results are updated in place in the `results_dic`
    """
    with open(dogfile, "r") as infile:
        dognames = set(line.strip().lower() for line in infile)  # Normalize to lowercase

    for key, value in results_dic.items():  # Iterate through key-value pairs
        # Extract pet name for clarity
        pet_name = value[0].lower()  # Normalize to lowercase
        
        is_dog = int(pet_name in dognames)
        is_classifier_dog = int(value[1] in dognames)
        value.extend((is_dog, is_classifier_dog))  # Extend the list with new values