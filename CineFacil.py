ListaReservas = []

def HacerReserva():
    def Funciones():
        print("Funciones")
        print("1 = The Dark Knight")
        print("2 = El Hombre Araña")
        print("3 = Interstellar")
        print("4 = Contacto Sangriento")
        print("5 = Rambo")
        print("6 = Rocky")
        while True:
            Funcion = input()
            if Funcion == "1":
                pelicula = "The Dark Knight"
                break
            elif Funcion == "2":
                pelicula = "El Hombre Araña"
                break
            elif Funcion == "3":
                pelicula = "Interstellar"
                break
            elif Funcion == "4":
                pelicula = "Contacto Sangriento"
                break
            elif Funcion == "5":
                pelicula = "Rambo"
                break
            elif Funcion == "6":
                pelicula = "Rocky"
                break
            else:
                print("opcion invalida")

        print("Horarios")
        print("1 = 10:00 am")
        print("2 = 2:00 pm")
        print("3 = 4:00 pm")
        print("4 = 6:00 pm")
        print("5 = 8:00 pm")
        print("6 = 10:00 pm")

        while True:
            Horario = input()
            if Horario == "1":
                hora = "10:00 am"
                break
            elif Horario == "2":
                hora = "2:00 pm"
                break
            elif Horario == "3":
                hora = "4:00 pm"
                break
            elif Horario == "4":
                hora = "6:00 pm"
                break
            elif Horario == "5":
                hora = "8:00 pm"
                break
            elif Horario == "6":
                hora = "10:00 pm"
                break
            else:
                print("Opcion invalida")
        FuncionHora = {"Pelicula": pelicula, "Horario": hora}
        return FuncionHora
    
    Nombre = input("ingrese el nombre del cliente").title()
    PeliHora = Funciones()
    Cantidadboletos = int(input("Ingrese la cantidad de boletos que desea comprar"))
    Cuenta = Cantidadboletos * 45

    Reserva = {
        "Nombre": Nombre,
        "Funcion y hora": PeliHora,
        "Cantidad de boletos": Cantidadboletos,
        "Cuenta": Cuenta
    }

    print()
    print(f"Cliente: {Nombre}. Función: {PeliHora['Pelicula']} a las {PeliHora['Horario']}. Boletos comprados: {Cantidadboletos}. Total: {Cuenta}")
    
    ListaReservas.append(Reserva)

def MostrarReservas():
    if not ListaReservas:
            print("no hay reservas")
    else:
        for i in range(len(ListaReservas)):
            print(ListaReservas[i])
            print()

while True:
    print("1 = Hacer reservas")
    print("2 = Ver reservas")
    print("3 = salir")
    opcion = input()

    if opcion == "1":
        HacerReserva()
    elif opcion == "2":
        MostrarReservas()
    elif opcion == "3":
        break
    else:
        print("Opcion invalida")


