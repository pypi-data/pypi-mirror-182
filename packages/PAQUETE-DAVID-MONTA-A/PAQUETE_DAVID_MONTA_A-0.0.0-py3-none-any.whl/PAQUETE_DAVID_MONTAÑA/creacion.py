def CALCULADOR_AREAS_FIGURAS():
    while True:
        print("Las figuras de las cuales puede calcular areas mi paquete son las siguientes: cuadrado, rectangulo, rombo, romboide, triangulo")
        print("PULSA CAULQUIER OTRA TECLA PARA SALIR")

        def figura():
            global tipo
            tipo=input("Introduce el tipo de figura: ")
        figura()

        def cuadrado():
            if tipo=="cuadrado":
                lado1=int(input("Introduce el valor del 1er lado: "))
                lado2=int(input("Introduce el valor del 2do lado: "))
                area=lado1*lado2
                print(f"El area de tu poligono es {area}")
        cuadrado()

        def rectangulo():
            if tipo=="rectangulo":
                largo=int(input("Introduce el largo de tu rectangulo: "))
                ancho=int(input("Introduce el ancho de tu rectangulo: "))
                area=largo*ancho
                print(f"El area de tu rectangulo es {area}")
        rectangulo()

        def rombo():
            if tipo=="rombo":
                diagonal_mayor=int(input("Introduce el valor de la diagonal mayor de tu rombo"))
                diagonal_menor=int(input("Introduce el valor de la diagonal menor de tu rombo"))
                area=(diagonal_mayor*diagonal_menor/2)
                print(f"El area de tu rombo es {area}")
        rombo()

        def romboide():
            if tipo=="romboide":
                base=int(input("Introduce la base de tu romboide: "))
                altura=int(input("Introduce la altura de tu romboide: "))
                area=base*altura
                print(f"El area de tu romboide es {area}")
        romboide()

        def triangulo():
            if tipo=="triangulo":
                base=int(input("Introduce la base de tu triangulo: "))
                altura=int(input("Introduce la altura de tu triangulo: "))
                area=(base*altura/2)
                print(f"El area de tu triangulo es {area}")
        triangulo()

        def otros():
            if tipo!="cuadrado" and tipo!="triangulo" and tipo!="rombo" and tipo!="romboide" and tipo!="rectangulo":
                print("Introduce una figura VALIDA, con todas las letras en minusculas")
                exit()
        otros()

CALCULADOR_AREAS_FIGURAS()