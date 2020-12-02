A = int(input("Введите число A:"))
B = int(input("Введите число B:"))
if A<B:
 for M in range (A,B+1):
  print(M)
elif A>B:
 for M in range (A,B-1,-1):
  print(M)
elif A == B:
  print(A)
