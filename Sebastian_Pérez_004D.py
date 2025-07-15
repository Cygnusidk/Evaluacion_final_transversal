productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def validar_texto(mensaje_input):
    while True:
        texto = input(mensaje_input)
        if len(texto.strip()) == 0:
            continue
        else:
            return texto
        
def stock_marca(modelo:str):
    stock_producto = 0
    for i in productos:
        print([i])
        if productos[i][0].lower() == modelo.lower():
            for e in stock:
                if e == 1:
                    stock_producto <= int[e][1]
                    break
    print(f"el stock es {stock_producto}")

def buscar_nombre(nombre_notebook:str):
    for i in productos:
        if productos [i][0].lower() == nombre_notebook.lower():
            notebook_encontrado=productos[i]
            notebook_encontrado.insert(0,i)
            return notebook_encontrado
                
            

def buscar_por_precio(rango_minimo:int, rango_maximo:int):
    notebooks = []
    while True:
        try:
            for i in stock:
                if stock [i][0] >= rango_minimo and stock [i] [0] <= rango_maximo:
                    print(f"Los notebooks entre los precios que consultas son: [{productos[i][0]}--")
        except ValueError:
            print("solo numeros positivos.")

def validar_numero_entero_positivo(msg_input:str):
    while True:
        try:
            numero = int(input(msg_input))
            if numero <= 0:
                print("El numero no puede ser negativo.")
                continue
            else:
                return numero
        except ValueError:
            print("Ingresa solo numeros enteros.")
            continue

def actualizar_precio_producto(modelo,p):
    notebook_encontrado = buscar_nombre(modelo)
    if notebook_encontrado != None:
        print(notebook_encontrado)
        for i in stock:
            if i.upper() == notebook_encontrado[0].upper():
                stock [i][0] = p
                return True
            else:
                return False


def menu():
    print("*** MENU PRINCIPAL ***")
    while True:
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir")
    
        try:
            opcion = int(input("Ingrese una opcion. [1 - 4]: "))
        except ValueError:
            print("Ingrese solo valores numericos.")

        if opcion == 1:
            validar_texto("Ingrese marca a consultar: ")
            stock_marca(modelo)
        elif opcion == 2:
            rango_minimo = validar_numero_entero_positivo("Ingrese el rango minimo: ")
            rango_maximo = validar_numero_entero_positivo("Ingrese el rango maximo: ")
            buscar_por_precio(rango_minimo, rango_maximo)
        elif opcion == 3:
            notebooks = validar_texto("Ingrese modelo a actualizar: ")
            actualizar_precio_producto("Ingrese nuevo precio: ")
        elif opcion == 4:
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida!!")

menu()