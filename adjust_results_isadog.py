def adjust_results_isadog(results_dic, dogfile):
    with open(dogfile, "r") as infile:
        dognames = set(line.strip() for line in infile)

    for value in results_dic.values():
        is_dog = int(value[0] in dognames)
        is_classifier_dog = int(value[1] in dognames)
        value.extend((is_dog, is_classifier_dog))