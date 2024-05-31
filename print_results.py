#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Mohammad Zaatra
# DATE CREATED:2024/05/28
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    # Prints summary statistics over the run
    print("\n\n*** Results Summary for CNN Model Architecture",model.upper(), 
          "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))
    # Prints summary statistics (percentages) on Model Run
    print(" ")
    for key in results_stats_dic:

        if key.startswith('p'):
            print("{:20}: {:.2f}".format(key, results_stats_dic[key]))
    if (print_incorrect_dogs and 
        ( (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
          != results_stats_dic['n_images'] ) 
       ):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key in results_dic:
            if (results_dic[key][3] == 1 and results_dic[key][4] == 0) or (results_dic[key][3] == 0 and results_dic[key][4] == 1):
                print("Pet Image Label: {:>26}   Classifier Label: {:>30}".format(results_dic[key][0], results_dic[key][1]))
    if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']) 
       ):
        print("\nINCORRECT Dog Breed Assignment:")
        for key in results_dic:
            if ( sum(results_dic[key][3:]) == 2 and
                results_dic[key][2] == 0 ):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0],
                                                          results_dic[key][1]))