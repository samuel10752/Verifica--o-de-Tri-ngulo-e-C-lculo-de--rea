import math

def eh_triangulo(a, b, c):
    return a < b + c and b < a + c and c < a + b

def area_triangulo(a, b, c):
    if eh_triangulo(a, b, c):
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    return None


a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
if eh_triangulo(a, b, c):
    area = area_triangulo(a, b, c)
    print(f"Os valores formam um triângulo com área: {area:.2f}")
else:
    print("Os valores não formam um triângulo:", a, b, c)