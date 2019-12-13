def max(a,b):
    if a>b:
        return a
    else:
        return b

def max3(n1,n2,n3):
    max = n1
    for i in (n2,n3):
        if(i > max):
            max = i
    return max

def factorielle(a):
    res = 1
    for i in range(1,a+1):
        res *= i
    return res
def quicksort(list):
    if len(list) <= 1:
        return list
    pivot = list.pop()
    lt,gt = [], []
    for e in list:
        if e < pivot:
            lt.append(e)
        else:
            gt.append(e)
    return quicksort(lt) + [pivot] + quicksort(gt)


print(max(1,2))
print(max3(1,2,1))
print(factorielle(5))

list = [1,4,8,3,2,7]

print(quicksort(list))