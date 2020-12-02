a = int(input("Введите число: "))
n = int(input("Введите степень числа: "))
def my_power(a, n):
    if n == 0:
        return 1
    return a * my_power(a, n-1)
print("Ответ:")
print(my_power(a,n))
