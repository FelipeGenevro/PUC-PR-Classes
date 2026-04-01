S = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
A = {3, 6, 5, 8, 1, 7}
B = {2, 3, 4, 5, 6, 7}
C = {1, 8, 9, 7}

print(f'S = {S}')

A_ = S-A
B_ = S-B
C_ = S-C

print(f'A_ = {A_}')
print(f'B_ = {B_}')
print(f'C_ = {C_}')

AuB = A.union(B)
AnB = A.intersection(B)

print(f'AuB = {AuB}')
print(f'AnB = {AnB}')

A_BnC = (A-B).union(C)
print(f'A_BnC = {A_BnC}')

if 10 in S or 12 in S:
    print("true")
else:
    print("false")
