from turtle import clear
import pyautogui, webbrowser
from time import sleep

def enviarMsj():
    webbrowser.open("https://web.whatsapp.com/send?phone=" + numero)
    sleep(10)
    for i in range(cantidad):
        pyautogui.typewrite(mensaje)
        pyautogui.press('enter')

def mostrarInfo():
    print("")
    print("Datos ingresados")
    print("Numero = " + numero)
    print("cantidad de mensajes a enviar = " + str(cantidad))
    print("Mensaje = " + mensaje)
    print("")
    print("En 10 segundos se abrira su navegador por defecto")

# Ejecucion del programa

print("Hola, soy el bot de shadow")
print("Que deseas hacer hacer?")
print("1 - Mandar mensajes a un numero de whatsapp")
print("2 - Mandar mensajes a un grupo de whatsapp")
print("3 - Nose")

bien = False
while not bien:
    opcion = int(input("Opcion: "))

    if opcion == 1:
        print("")
        numero = input("ingrese el numero de telefono 'incluyendo el +54': ")
        cantidad = int(input("ingrese la cantidad de mensajes a enviar: "))
        mensaje = input("escriba el mensaje a enviar: ")
        print("")

        confirmar = False
        opciones = ["si", "no", "s", "n", "y"]
        while not confirmar:
            confirmacionUsuario = input("Desea continuar? s/n = ").lower()

            if confirmacionUsuario in opciones:
                if confirmacionUsuario == "s" or confirmacionUsuario == "y" or confirmacionUsuario == "si":
                    print("Recolectando los datos ingresados.......")
                    sleep(3)
                    mostrarInfo()
                    sleep(10)
                    enviarMsj()
                    confirmar = True
                else:
                    print("Nos vemos!")
                    confirmar = True
            else:
                print(f'la opcion "{confirmacionUsuario}" no es valida, a ver si haces una bien')
                confirmar = False

            bien = True

    elif opcion == 2:
        print("Lo siento :(, la hermana de nik esta con shadow")
        bien = True
    elif opcion == 3:
        print("Sos pelotudo?, no sabes que queres hacer?")
        bien = True
    else:
        print("ERROR: 'Opcion incorrecta, ingresa una opcion valida'")


