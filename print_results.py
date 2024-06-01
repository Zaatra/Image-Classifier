from prettytable import PrettyTable
import os  # Import the os module for file path handling

def print_summary_results(results_stats_dic, model, file=None):
    """Prints summary results to console or file."""
    print("*** Results Summary for CNN Model Architecture", model.upper(), "***", file=file)

    summary_table = PrettyTable(["Metric", "Count"])
    summary_table.add_row(["Total Images", results_stats_dic['n_images']])
    summary_table.add_row(["Correct Dog Images", results_stats_dic['n_correct_dogs']])
    summary_table.add_row(["Correct Not-Dog Images", results_stats_dic['n_correct_notdogs']])
    print(summary_table, file=file)
    print(file=file) 

    print("***  Percentage Results ***", file=file)

    pct_table = PrettyTable(["Metric", "Percentage"])
    pct_table.add_row(["Match", results_stats_dic['pct_match']])
    pct_table.add_row(["Correct Dogs", results_stats_dic['pct_correct_dogs']])
    pct_table.add_row(["Correct Breed", results_stats_dic['pct_correct_breed']])
    pct_table.add_row(["Correct Not-Dogs", results_stats_dic['pct_correct_notdogs']])
    print(pct_table, file=file)

def print_incorrect_classifications(results_dic, results_stats_dic, file=None):
    """Prints incorrectly classified images if applicable."""
    if (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']
          != results_stats_dic['n_images']):
        print("\nINCORRECT Dog/NOT Dog :", file=file)
        incorrect_dogs = []
        for value in results_dic.values():
            if value[3] != value[4]:
                incorrect_dogs.append([value[0], value[1]])
        incorrect_dogs_table = PrettyTable(["Real", "Classifier"])
        for row in incorrect_dogs:
            incorrect_dogs_table.add_row(row)
        print(incorrect_dogs_table, file=file)

def print_argument_info(dir, arch, dogfile, file=None):
    """Prints information about the script arguments."""
    print("*** Argument Information ***", file=file)
    argument_table = PrettyTable(["Argument", "Value"])
    argument_table.add_row(["Directory", dir])
    argument_table.add_row(["Architecture", arch])
    argument_table.add_row(["Dog Names File", dogfile])
    print(argument_table, file=file)

def save_detailed_results(results_dic, output_file):
    """Saves detailed prediction results to a file."""
    detailed_table = PrettyTable(["Pet Label", "Classifier Label", "Match", "Real Dog?", "Classifier Dog?"])
    for image_name, results in results_dic.items():
        pet_label, classifier_label, match, is_dog, is_classifier_dog = results

        match = "Yes" if match == 1 else "No"
        is_dog = "Yes" if is_dog == 1 else "No"
        is_classifier_dog = "Yes" if is_classifier_dog == 1 else "No"

        detailed_table.add_row([pet_label, classifier_label, match, is_dog, is_classifier_dog])

    with open(output_file, "a") as f:  # Open in append mode ('a')
        print(detailed_table, file=f)

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False,
                  dir='', arch='', dogfile='', image_source=''):
    """
    Prints summary results and saves detailed results to a file.

    Args:
      results_dic (dict): Dictionary with image classification results.
      results_stats_dic (dict): Dictionary with classification statistics.
      model (str): CNN model architecture used.
      print_incorrect_dogs (bool): True prints incorrectly classified images.
      dir (str): Path to the image directory.
      arch (str): CNN model architecture used.
      dogfile (str): Path to the dog names file.
      image_source (str): Source of the images processed ('pet' or 'uploaded').
    """
    output_file = os.path.join("Results", f"{arch}_results_{image_source}.txt")

    print_summary_results(results_stats_dic, model)

    if print_incorrect_dogs:
        print_incorrect_classifications(results_dic, results_stats_dic)

    print_argument_info(dir, arch, dogfile)

    # --- Write the 3 summary tables to the file --- #
    with open(output_file, "w") as f:
        print_summary_results(results_stats_dic, model, file=f)
        if print_incorrect_dogs:
            print_incorrect_classifications(results_dic, results_stats_dic, file=f)
        print_argument_info(dir, arch, dogfile, file=f)

        # Correctly print the detailed results header to the file
        print("***  Detailed Prediction Results ***", file=f)

    # --- Append the detailed table to the file --- #
    save_detailed_results(results_dic, output_file)
