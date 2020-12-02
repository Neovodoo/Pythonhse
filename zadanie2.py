m = int(input())
l = m - 1
def my_div(m):
    z = "xx"
    for i in range (2, l):
        if m % i == 0:
            z = i
    if z == "xx":
        return(m)
    else:
        return(z)

print(my_div(m))
