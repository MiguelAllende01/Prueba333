
def menu():
    while True:
        opcion = input("1.- Leer un archivo\n2.- Salir\nelige una opcion: ")
        if opcion == "1":
            lectura_de_archivo()
        elif opcion == "2":
            break
        else:
            print("Ingresa opcion valida") 

def lectura_de_archivo():
    nombre_de_archivo = input("Ingresa el nombre del archivo que quieres leer: ")
    with open(nombre_de_archivo, "r") as archivo:
            texto = archivo.read() 
            num_letras = len(texto) # cuenta letras
            num_espacios = texto.count(" ") # cuenta caracter q le pidas
            total_de_letras = num_letras - num_espacios # cantidad de letras 
    with open("lector.txt", "w") as archi_salida: 
            archi_salida.write(f"La cantidad de letras del archivo es {total_de_letras} y la cantidad de espacios es de {num_espacios}")
    print(f"La cantidad de letras del archivo es  {total_de_letras} y la cantidad de espacios que tiene {num_espacios}")
 
menu()