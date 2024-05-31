from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (a string) from the image filenames in 
    `image_dir`. These pet image labels are used to check the accuracy of the 
    labels that are returned by the classifier function, `classifier`.
    Parameters:
      image_dir - The (full) path to the folder of images that are to be 
        classified by the classifier function, `classifier`.
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
        List. The list contains for one image, the pet image label (string).
    """
    filename_list = listdir(image_dir)
    results_dic = dict()

    for filename in filename_list:  # Iterate directly over the list
        if not filename.startswith("."):
            image_name = filename.lower()
            word_list_image = image_name.split("_")
            pet_name = ""
            for word in word_list_image:
                if word.isalpha():
                    pet_name += word + " "
            pet_name = pet_name.strip()

            if filename not in results_dic:  # Use filename directly
                results_dic[filename] = [pet_name]
            else:
                print(f"Duplicate file: {filename}")

    return results_dic