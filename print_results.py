from tabulate import tabulate

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False,
                  dir='', arch='', dogfile=''):
    print("\n*** Results Summary for CNN Model Architecture",model.upper(),"***")

    # Create a table for summary stats
    summary_table = [
        ["Total Images", results_stats_dic['n_images']],
        ["Correct Dog Images", results_stats_dic['n_correct_dogs']],
        ["Correct Not-Dog Images", results_stats_dic['n_correct_notdogs']],
    ]
    print(tabulate(summary_table, headers=["Metric", "Count"], tablefmt="grid"))
    print()
    
    print("***  Percentage Results ***")

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
        print("\nINCORRECT Dog/NOT Dog :")
        incorrect_dogs = []
        for value in results_dic.values():
            if value[3] != value[4]:  # Simplified condition
                incorrect_dogs.append([value[0], value[1]])
        print(tabulate(incorrect_dogs, headers=["Real", "Classifier"], tablefmt="grid"))

    # Print argument information
    print("\n\n*** Argument Information ***")
    argument_table = [
        ["Directory", dir],
        ["Architecture", arch],
        ["Dog Names File", dogfile],
    ]
    print(tabulate(argument_table, headers=["Argument", "Value"], tablefmt="grid"))