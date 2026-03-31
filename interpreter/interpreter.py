math_query = input("Enter :")
x, y, z = math_query.split()
x = float(x)
z = float(z)


if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "*":
    answer = x * z
else:
    answer = x / z

print(answer)