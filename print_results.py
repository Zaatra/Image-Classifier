from tabulate import tabulate

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False,
                  dir='', arch='', dogfile=''):
    print("\n\n*** Results Summary for CNN Model Architecture",model.upper(),"***")

    # Create a table for summary stats
    summary_table = [
        ["Total Images", results_stats_dic['n_images']],
        ["Correct Dog Images", results_stats_dic['n_correct_dogs']],
        ["Correct Not-Dog Images", results_stats_dic['n_correct_notdogs']],
    ]
    print(tabulate(summary_table, headers=["Metric", "Count"], tablefmt="grid"))

    # Create a table for percentages
    pct_table = [
        ["Match", results_stats_dic['pct_match']],
        ["Correct Dogs", results_stats_dic['pct_correct_dogs']],
        ["Correct Breed", results_stats_dic['pct_correct_breed']],
        ["Correct Not-Dogs", results_stats_dic['pct_correct_notdogs']],
    ]
    print(tabulate(pct_table, headers=["Metric", "Percentage"], tablefmt="grid"))

    # Use .values() to iterate over the dictionary values directly
    if (print_incorrect_dogs and 
        ( (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
          != results_stats_dic['n_images'] )):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        incorrect_dogs = []
        for value in results_dic.values():
            if value[3] != value[4]:  # Simplified condition
                incorrect_dogs.append([value[0], value[1]])
        print(tabulate(incorrect_dogs, headers=["Real", "Classifier"], tablefmt="grid"))

    if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])):
        print("\nIncorrect Dog Breed Assignment:")
        incorrect_breeds = []
        for value in results_dic.values():
            if ( sum(value[3:]) == 2 and
                value[2] == 0 ):
                incorrect_breeds.append([value[0], value[1]])
        print(tabulate(incorrect_breeds, headers=["Real", "Classifier"], tablefmt="grid"))

    # Print argument information
    print("\n\n*** Argument Information ***")
    argument_table = [
        ["Directory", dir],
        ["Architecture", arch],
        ["Dog Names File", dogfile],
    ]
    print(tabulate(argument_table, headers=["Argument", "Value"], tablefmt="grid"))