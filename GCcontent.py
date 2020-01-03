def GCcontent(file):
    with open(file) as f:
        file_list = [line.rstrip() for line in f]

    name_list = []
    dna_list = []
    print(file_list)
    dna_str = ""
    i = 0

    while i < len(file_list):
        if file_list[i] == file_list[0]:
            name_list.append(file_list[i])
            i += 1
        elif file_list[i][0] == ">":
            name_list.append(file_list[i])
            dna_list.append(dna_str)
            dna_str = ""
            i += 1
        elif i == len(file_list)-1:
            dna_str = dna_str + file_list[i]
            dna_list.append(dna_str)
            i += 1
        else:
            dna_str = dna_str + file_list[i]
            i += 1

    print(name_list)
    print(dna_list)
    gc_list = []

    for dna in dna_list:
        dna_dict = {}
        for nt in dna:
            if nt not in dna_dict:
                dna_dict[nt] = 1
            else:
                dna_dict[nt] += 1
        gc_content = dna_dict["G"] + dna_dict["C"]
        gc_percent = gc_content/len(dna) * 100
        gc_list.append(gc_percent)

    gc_dict = {}
    i = 0
    for name in name_list:
        gc_dict[name] = gc_list[i]
        i += 1
    print(max(gc_dict, key=gc_dict.get))
    print(max(gc_dict.values()))

GCcontent("GCTest")