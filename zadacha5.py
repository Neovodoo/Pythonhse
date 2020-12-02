a = ["Daniil Ivanov 18", "Maxim Ivanov 32", "Alina Ivanova 27", "Natalia ivanova 45"]
print(sorted(a, key = lambda x: int(x[-2])))
