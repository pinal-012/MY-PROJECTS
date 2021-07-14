l1 = [1,2,3,4,5,6,7,7,6,5,4,3,22,25,41]
l2 = []
l3=[l2.append(i) for i in l1 if i not in l2]
print(l2)
print(l3)