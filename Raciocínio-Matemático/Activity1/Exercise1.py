#Lista de exercícios de conjuntos e números complexos passados pela professora Roveredo

from math import sqrt, pi

print("\n>>>PÁGINA 2<<<")

#=================================
#Atividade 1
#=================================

S = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
A = {3, 6, 5, 8, 1, 7}
B = {2, 3, 4, 5, 6, 7}
C = {1, 8, 9, 7}

print("\n✅ | Atividade 1")
print(f"\nA) A' = {S-A}")
print(f"B) B' = {S-B}")
print(f"C) C' = {S-C}")
print(f"D) AuB = {A.union((S-B))}")
print(f"E) AnC = {A.intersection(C)}")
print(f"F) (AnC)' = {S-(A.intersection(C))}")
print(f"G) (A-B)uC = {(A-B).union(C)}")
print(f"H) (A-B)'nC' = {(S-(A-B)).intersection(S-C)}")
print(f"I) A'nC' = {(S-A).intersection(S-C)}")


#=================================
#Atividade 2
#=================================

A = {1, 3, 5, pi, 7, 8, (9, 10)}
B = {3, 5, pi}
C = (pi, (9))

D = (9, 10)

print("\n✅ | Atividade 2")

if 9 in A:
    print("\nA) True")
else:
    print("\nA) False")

if {9, 10} <= A:
    print("B) True")
else:
    print("B) False")