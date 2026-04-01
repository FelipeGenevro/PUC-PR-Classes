#Lista de exercícios de conjuntos e números complexos passados pela professora Roveredo

from math import sqrt, pi

#=================================
#PÁGINA 1
#=================================

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

print("\n✅ | Atividade 2")

if 9 in A:
    print("\nA) True")
else:
    print("\nA) False")

if {9, 10} <= A:
    print("B) True")
else:
    print("B) False")

if C in A:
    print("C) True")
else:
    print("C) False")

if B < A:
    print("D) True")
else:
    print("D) False")

#=================================
#Atividade 3
#=================================

z1 = complex(3, 4)
z2 = complex(1, 2)
z3 = complex(7, 9)

print("\n✅ | Atividade 3")

print(f"\nA) Z1 + Z2 = {z1 + z2}")
print(f"B) Z2 - Z3 = {z1 - z2}")
print(f"C) Z1 * Z3 = {z1 * z3}")
print(f"D) Z2 / Z3 ≈ {z2 / z3:.2f}")

#=================================
#PÁGINA 2
#=================================

print("\n>>>PÁGINA 1<<<")

#=================================
#Atividade 1
#=================================

S = {2, 5, 17, 27}

print("\n✅ | Atividade 1")

if 5 in S:
    print("\nA) True")
else:
    print("\nA) False")

if 2 + 5 in S:
    print("B) True")
else:
    print("B) False")

if () in S:
    print("C) True")
else:
    print("C) False")

if S in S:
    print("D) True")
else:
    print("D) False")

#=================================
#Atividade 2
#=================================

R = {1, 3, pi, 4, 1, 9, 10}
T = {1, 3, pi}
S = {(1), 3, 9, 10}
U = {(1, 3, pi), 1}

print("\n✅ | Atividade 2")
