# 1 2 3 4 5 6
def enumerating_gene_orders(n):
    permutations = []
    for i in range(1, n + 1):
        add_list = []
        add_list.append(i)
        for k in range(1, n + 1):
            if i == k:
                pass
            else:
                add_list.append(k)
        permutations.append(add_list)

    print(len(permutations))
    for permutation in permutations:
        print(permutation)

enumerating_gene_orders(3)