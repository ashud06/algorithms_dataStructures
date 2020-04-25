A=[]
def generate_list(k):
    result=[]
    for i in range(0,k):
        result.append(i)
    return result

def main(n,k):
    if n == 0: return []
    if n == 1: return generate_list(k)
    return [str(digit) + str(bits) for digit in main(1,k) for bits in main(n-1,k)]



print(main(4,3))
