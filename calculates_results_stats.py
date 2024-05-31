def calculates_results_stats(results_dic):
    results_stats_dic = dict()
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0       

    # Use .values() to iterate over the dictionary values directly
    for value in results_dic.values():
        if value[2] == 1:
            results_stats_dic['n_match'] += 1
        if value[3] == 1 and value[2] == 1:
            results_stats_dic['n_correct_breed'] += 1
        if value[3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            if value[4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
        else:
            if value[4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # The rest of the function remains the same
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - 
                                      results_stats_dic['n_dogs_img']) 
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / 
                                  results_stats_dic['n_images']) * 100.0
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / 
                                          results_stats_dic['n_dogs_img']) * 100.0
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / 
                                          results_stats_dic['n_dogs_img']) * 100.0
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                results_stats_dic['n_notdogs_img'])*100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
    return results_stats_dic