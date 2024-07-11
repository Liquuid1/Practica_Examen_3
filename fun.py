import csv

def menu():
    menu = """      SELECCIONA
*******************************************
[1] Asignar llamadas
[2] Clasificar llamadas
[3] Ver llamadas
[4] Reportes
[5] Listar Archivo CSV
[6] Salir
--> """
    print(menu,end="")

def validar_dato_numerico(menor,mayor):
    while True:
        try:
            op = int(input())
            if op<menor or op>mayor:
                raise ValueError
            else:
                return op
        except:
            print("Ingresa una opción valida. --> ",end="")

#lista y telefonistas son alias
def asignar_llamadas(lista):
    for i in range(3):
        nombre = input(f"Ingrese el nombre del telefonista {i+1}: ")
        print("Ingrese la cantidad de minutos que hablo el telefonista (Entre 10 y 50): ",end="")
        minutos = validar_dato_numerico(10,50)
        print("Ingrese [1] si el horario fue alto y [2] si el horario fue bajo: ",end="")
        op = validar_dato_numerico(1,2)
        if op==1:
            horario = "Alto"
        else:
            horario = "Bajo"
        
        tel = {"Nombre":nombre,"Horario":horario,"Total Minutos":minutos}
        lista.append(tel)

def clasificar_llamadas(lista):
    print("NOMBRE       |HORARIO      |MINUTOS       ")
    for persona in lista:
        print(f"{persona["Nombre"]}  |{persona["Horario"]}  |{persona["Total Minutos"]}")

def listar_csv(lista):
    nombre_campos = ["Nombre","Horario","Total Minutos"]
    with open('Telefonista.csv','w',newline="") as archivo:
        escritor = csv.DictWriter(archivo,fieldnames=nombre_campos)
        escritor.writeheader()
        escritor.writerows(lista)

