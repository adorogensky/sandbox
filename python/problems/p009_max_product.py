def max_product(a):
    max_product = product = None
    for i in range(0, len(a) - 1):
        product = a[i] * a[i + 1]
        if max_product == None or max_product < product:
            max_product = product 
    return max_product
