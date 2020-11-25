A = int(input("Введите число A:"))
B = int(input("Введите число B:"))
if A>999 and A<10000 and B>999 and B<10000 and A<B:
  for M in range(A,B):
    z = M // 1000
    x = (M // 100) % 10
    c = (((M // 10) % 100) % 10)
    v = (((M % 1000) % 100) % 10)
    if (z == v) and (x == c):
      print(M)
