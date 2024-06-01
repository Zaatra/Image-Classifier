def calculate_percentage(numerator, denominator):
    return (numerator / denominator) * 100.0 if denominator > 0 else 0.0

def calculates_results_stats(results_dic):
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
        if value[3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            results_stats_dic['n_correct_breed'] += value[2]
            results_stats_dic['n_correct_dogs'] += value[4]
        else:
            results_stats_dic['n_correct_notdogs'] += 1 - value[4]

    results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']
    results_stats_dic['pct_match'] = calculate_percentage(results_stats_dic['n_match'], results_stats_dic['n_images'])
    results_stats_dic['pct_correct_dogs'] = calculate_percentage(results_stats_dic['n_correct_dogs'], results_stats_dic['n_dogs_img'])
    results_stats_dic['pct_correct_breed'] = calculate_percentage(results_stats_dic['n_correct_breed'], results_stats_dic['n_dogs_img'])
    results_stats_dic['pct_correct_notdogs'] = calculate_percentage(results_stats_dic['n_correct_notdogs'], results_stats_dic['n_notdogs_img'])

    return results_stats_dic