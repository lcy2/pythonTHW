def swap_nums(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    
    return [a, b]