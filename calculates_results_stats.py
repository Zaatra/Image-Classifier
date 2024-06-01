# calculates_results_stats.py
def calculate_percentage(numerator, denominator):
    """Calculates percentage with safe division."""
    return (numerator / denominator) * 100.0 if denominator > 0 else 0.0

def calculates_results_stats(results_dic):
    """
    Calculates statistics based on the results of the image classification.

    Args:
      results_dic (dict): Dictionary with 'key' as image filename and 'value' as a 
                          List. The list contains:
                            - Pet image label (string)
                            - Classifier label (string)
                            - 1/0 (int)  where 1 = match between pet image and 
                                      classifier labels and 0 = no match
                            - 1/0 (int)  where 1 = pet image label is a dog and 
                                      0 = pet Image label isn't a dog
                            - 1/0 (int)  where 1 = Classifier classifies image 
                                      as Dog (& pet image is a dog)
                                      0 = Classifier classifies image as NOT a 
                                      Dog (& pet image is a dog)

    Returns:
      results_stats_dic (dict): Dictionary that contains the results statistics (either
                   a percentage or a count) where the key is the statistic's 
                   name (starting with 'pct' for percentages) and the value is the
                   statistic's value.
    """
    results_stats_dic = {
        'n_dogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0,
        'n_images': len(results_dic),
    }

    for value in results_dic.values():
        results_stats_dic['n_match'] += value[2]
        if value[3] == 1:  # It's a dog image
            results_stats_dic['n_dogs_img'] += 1
            if value[4] == 1:  # Classifier correctly identified as dog
                results_stats_dic['n_correct_dogs'] += 1
            if value[2] == 1:  # Correct breed match
                results_stats_dic['n_correct_breed'] += 1 
        else:  # It's NOT a dog image
            if value[4] == 0:  # Classifier correctly identified as NOT dog
                results_stats_dic['n_correct_notdogs'] += 1

    results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']
    results_stats_dic['pct_match'] = calculate_percentage(results_stats_dic['n_match'], results_stats_dic['n_images'])
    results_stats_dic['pct_correct_dogs'] = calculate_percentage(results_stats_dic['n_correct_dogs'], results_stats_dic['n_dogs_img'])
    results_stats_dic['pct_correct_breed'] = calculate_percentage(results_stats_dic['n_correct_breed'], results_stats_dic['n_dogs_img'])
    results_stats_dic['pct_correct_notdogs'] = calculate_percentage(results_stats_dic['n_correct_notdogs'], results_stats_dic['n_notdogs_img'])

    return results_stats_dic