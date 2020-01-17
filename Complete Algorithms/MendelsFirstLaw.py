# return the probability that 2 randomy selected organisms will produice an offspring with at least 1 dominant allele
def mendels_first_law(k, m , n):
    # k = homozygous dominant (2/2)
    # m = heterozygous dominant (1/2)
    # n = homozygous recessive (0/2)
    total = k + m + n
    r_r = (n/total) * ((n-1)/(total-1))
    h_h = (m/total) * ((m-1)/(total-1))
    h_r = (m/total) * ((n/(total-1)) + (n/total))
    recessive_total = r_r + h_h * 1/4 + h_r * 1/2
    dom_tot = 1 - recessive_total
    return dom_tot

k = 28
m = 30
n = 28
print(mendels_first_law(k, m, n))
# not correct