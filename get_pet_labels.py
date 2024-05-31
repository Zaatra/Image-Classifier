from os import listdir
def get_pet_labels(image_dir):
    filename_list = listdir(image_dir)
    results_dic = dict()
    for idx in range(0, len(filename_list)):
        if not filename_list[idx].startswith("."):
            image_name = filename_list[idx].lower()
            word_list_image = image_name.split("_")
            pet_name = ""
            for word in word_list_image:
                if word.isalpha():
                    pet_name += word + " "
            pet_name = pet_name.strip()
            if filename_list[idx] not in results_dic:
                results_dic[filename_list[idx]] = [pet_name]
            else:
                print(f"Duplicate file: {filename_list[idx]}")
    return results_dic