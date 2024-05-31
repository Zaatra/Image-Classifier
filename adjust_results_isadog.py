def adjust_results_isadog(results_dic, dogfile):
    dognames_dic = dict()
    with open (dogfile, "r") as infile:
      line = infile.readline()
      while line != "":
        line = line.rstrip()
        if line not in dognames_dic:
          dognames_dic[line] = 1
        else:
          print("Duplicate Dogname", line)
        line = infile.readline()

    # Use .values() to iterate over the dictionary values directly
    for value in results_dic.values():
        if value[0] in dognames_dic:
            if value[1] in dognames_dic:
                value.extend((1, 1))
            else:
                value.extend((1, 0))
        else:
            if value[1] in dognames_dic:       
                value.extend((0, 1))
            else:
                value.extend((0, 0))