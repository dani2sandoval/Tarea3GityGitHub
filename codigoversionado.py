print("¡Bienvenido a la Calculadora!")


a = 2
b = 3
print(a + b)


def sumar(a, b):
    return a + b

try:
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    print("Resultado:", sumar(a, b))
except ValueError:
    print("Error: Debes ingresar solo números.")
