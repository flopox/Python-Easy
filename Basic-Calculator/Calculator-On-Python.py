def suma(a, b):

  return a + b

def resta(a, b):

  return a - b

def multiplicacion(a, b):

  return a * b

def division(a, b):

  return a / b

def main():
  print("Bienvenido a la calculadora simple")

  while True:
    print("¿Qué operación desea realizar?")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = input()

    if opcion not in ("1", "2", "3", "4"):
      print("Opción inválida")
      continue

    print("Ingrese el primer número:")
    a = float(input())
    print("Ingrese el segundo número:")
    b = float(input())

    if opcion == "1":
      resultado = suma(a, b)
    elif opcion == "2":
      resultado = resta(a, b)
    elif opcion == "3":
      resultado = multiplicacion(a, b)
    else:
      resultado = division(a, b)

    print("El resultado es:", resultado)

    print("¿Desea realizar otra operación? (s/n)")
    respuesta = input()
    if respuesta == "n":
      break

if __name__ == "__main__":
  main()