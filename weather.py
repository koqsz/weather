infile = open('weather.dat')
line_data_dic = {}
min_diff = 0
next(infile)
for line in infile:
    if line.rstrip():
        parts = line.split()
        if "mo" in parts[0]:
            break
        else:
            diffs = int(parts[1].replace('*', ''))-int(parts[2].replace('*', ''))
            if min_diff < diffs:
                min_diff = diffs
                min_diff_line = int(parts[0])
line_data_dic[min_diff_line] = min_diff
for key in line_data_dic.keys():
    print ('On the', (key),'day had got the smallest temperature spread')
