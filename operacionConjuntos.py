set_a = {'col', 'mex','bol'}
set_b = {'per','bol'}

print(set_a)
print(set_b)

print("********union********")
set_c = set_a.union(set_b)
print(set_c)

print("********interseccion********")
set_c = set_a.intersection(set_b)
print(set_c)

print("********diferencia********")
set_c = set_a.difference(set_b)
print(set_c)

print("********diferencia simetrica********")
set_c = set_a.symmetric_difference(set_b)
print(set_c)