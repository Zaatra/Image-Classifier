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
    if (print_incorrect_dogs and 
        ( (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
          != results_stats_dic['n_images'] )):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key in results_dic:
            if (results_dic[key][3] == 1 and results_dic[key][4] == 0) or (results_dic[key][3] == 0 and results_dic[key][4] == 1):
                print("Pet Image Label: {:>26}   Classifier Label: {:>30}".format(results_dic[key][0], results_dic[key][1]))
    if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])):
        print("\nINCORRECT Dog Breed Assignment:")
        for key in results_dic:
            if ( sum(results_dic[key][3:]) == 2 and
                results_dic[key][2] == 0 ):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0],
                                                          results_dic[key][1]))