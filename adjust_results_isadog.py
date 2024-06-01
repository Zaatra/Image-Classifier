def adjust_results_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if an image is a dog
    (and to identify the breed if applicable).
    
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
        List. The list contains for one image, the pet image label (string),
        the classifier label (string), and match (int).
      dogfile - A string representing the filename in which the dog names are 
        stored.
    
    Returns:
      None - modifies the results_dic dictionary in place
    """
    dognames_dic = dict()
    with open(dogfile, "r") as infile:
        line = infile.readline()
        while line != "":
            line = line.rstrip()
            if line not in dognames_dic:
                dognames_dic[line] = 1
            else:
                print("Duplicate Dogname", line)
            line = infile.readline()

    # Use .values() to iterate over the dictionary values directly
    for value in results_dic.values():
        # Check if the pet image label is a dog
        is_dog = value[0] in dognames_dic

        # Check if the classifier label is a dog
        is_classifier_dog = value[1] in dognames_dic

        # Extend the value list with dog and breed match indicators
        value.extend((int(is_dog), int(is_classifier_dog))) 