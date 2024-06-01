from time import time, sleep
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results_isadog import adjust_results_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results
from tabulate import tabulate

def main():
    start_time = time()
    in_arg = get_input_args()

    # Creates pet image labels by creating a dictionary with key=filename 
    # and value=pet label
    results = get_pet_labels(in_arg.dir)

    # Classifies images by using CNN to create the classifier labels and 
    # comparing the classifier labels to the pet image labels. 
    # This function inputs:
    #         - The results dictionary as results_dic within classify_images 
    #             function.
    #         - The CNN model architecture as model within classify_images 
    #             function.
    # Outputs:
    #         - The results dictionary as results_dic within classify_images 
    #             function. 
    #         - None if classify_images function fails
    classify_images(in_arg.dir, results, in_arg.arch)

    # Adjusts the results dictionary to determine if an image is a dog 
    # (and to identify the breed if applicable)
    adjust_results_isadog(results, in_arg.dogfile)

    # Calculates results of pet image classification, identifying any 
    # misclassifications and then reports the results statistics. 
    results_stats = calculates_results_stats(results)

    # Prints summary results, incorrectly classified images, and  
    # incorrectly classified breeds. 
    print_results(results, results_stats, in_arg.arch, True,
                  dir=in_arg.dir, arch=in_arg.arch, dogfile=in_arg.dogfile) 

    # Measure total program runtime 
    end_time = time()
    tot_time = end_time - start_time
    seconds = int((tot_time % 3600) % 60)
    minutes = int((tot_time % 3600) / 60)
    hours = int((tot_time / 3600))
    print(f"\nTotal Elapsed Runtime Is : {hours} : {minutes} : {seconds}.\n")

if __name__ == "__main__":
    main()