from time import time
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results_isadog import adjust_results_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def format_time(tot_time):
    seconds = int((tot_time % 3600) % 60)
    minutes = int((tot_time % 3600) / 60)
    hours = int((tot_time / 3600))
    return f"{hours} : {minutes} : {seconds}"

def main():
    start_time = time()
    in_arg = get_input_args()

    results = get_pet_labels(in_arg.dir)
    classify_images(in_arg.dir, results, in_arg.arch)
    adjust_results_isadog(results, in_arg.dogfile)
    results_stats = calculates_results_stats(results)
    print_results(results, results_stats, in_arg.arch, True, dir=in_arg.dir, arch=in_arg.arch, dogfile=in_arg.dogfile) 

    tot_time = time() - start_time
    print(f"\nTotal Elapsed Runtime Is : {format_time(tot_time)}.\n")

if __name__ == "__main__":
    main()