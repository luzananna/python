def permutations(lst):
    if lst == []:
        return [[]]
    if len(lst) == 0:
        return [' ']
    if len(lst) == 1:
        return [lst]
    a = [] 
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutations(remLst):
           a.append([m] + p)
    return a
