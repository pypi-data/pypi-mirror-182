def cuadrado ():
    base = float(input("Introduce la base del cuadrado: "))
    sup = base * base
    print(f"La superficie del cuadrado es: {sup}")

def rectangulo ():
    base = float(input("Introduce la base del rectangulo: "))
    altura = float(input("Introduce la altura del rectangulo: "))
    sup = base * altura
    print(f"La superficie del rectangulo es: {sup}")

def trapecio ():
    basemayor = float(input("Introduce la base mayor del trapecio: "))
    basemenor = float(input("Introduce la base menor del trapecio: "))
    altura = float(input("Introduce la altura del trapecio: "))
    sup = ((basemayor+basemenor)/2)*altura
    print(f"La superficie del trapecio es {sup}")

def triangulo ():
    base = float(input("Introduce la base del triangulo: "))
    altura = float(input("Introduce la altura del triangulo: "))
    sup = base * (altura/2)
    print(f"La superficie del triangulo es: {sup}")

def circulo ():
    radio = float(input("Introduce el radio del circulo: "))
    sup = (radio**2) * 3.14
    print(f"La superficie del circulo es: {sup}")

def romboide ():
    diagonalmayor = float(input("Introduce la diagonal mayor del romboide: "))
    diagonalmenor = float(input("Introduce la diagonal menor del romboide: "))
    sup = (diagonalmayor * diagonalmenor)/2
    print(f"La superficie del romboide es: {sup}")