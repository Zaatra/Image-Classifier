def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    print("\n\n*** Results Summary for CNN Model Architecture",model.upper(),"***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))
    print(" ")
    for key in results_stats_dic:
        if key.startswith('p'):
            print("{:20}: {:.2f}".format(key, results_stats_dic[key]))

    # Use .values() to iterate over the dictionary values directly
    if (print_incorrect_dogs and 
        ( (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
          != results_stats_dic['n_images'] )):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for value in results_dic.values():
            if value[3] != value[4]:  # Simplified condition
                print("Real: {:>26}   Classifier: {:>30}".format(value[0], value[1]))

    if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])):
        print("\nIncorrect Dog Breed Assignment:")
        for value in results_dic.values():
            if ( sum(value[3:]) == 2 and
                value[2] == 0 ):
                print("Real: {:>26}   Classifier: {:>30}".format(value[0],
                                                          value[1]))