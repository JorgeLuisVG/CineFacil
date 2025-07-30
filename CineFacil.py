ListaReservas = []

def Funciones():
    print("Funciones")
    print("1 = The Dark Knight")
    print("2 = El Hombre Araña")
    print("3 = Interstellar")
    print("4 = Contacto Sangriento")
    print("5 = Rambo")
    print("6 = Rocky")
    Funcion = input()

    if Funcion == "1":
        pelicula = "The Dark Knight"
    elif Funcion == "2":
        pelicula = "El Hombre Araña"
    elif Funcion == "3":
        pelicula = "Interstellar"
    elif Funcion == "4":
        pelicula = "Contacto Sangriento"
    elif Funcion == "5":
        pelicula = "Rambo"
    elif Funcion == "6":
        pelicula = "Rocky"

    print("Horarios")
    print("1 = 10:00 am")
    print("2 = 2:00 pm")
    print("3 = 4:00 pm")
    print("4 = 6:00 pm")
    print("5 = 8:00 pm")
    print("6 = 10:00 pm")
    Horario = input()

    if Funcion == "1":
        hora = "10:00 am"
    elif Funcion == "2":
        hora = "2:00 pm"
    elif Funcion == "3":
        hora = "4:00 pm"
    elif Funcion == "4":
        hora = "6:00 pm"
    elif Funcion == "5":
        hora = "8:00 pm"
    elif Funcion == "6":
        hora = "10:00 pm"
    
    FuncionHora = {"Pelicula": pelicula, "Horario": hora}

    return FuncionHora

def HacerReserva():
    Nombre = input("ingrese el nombre del cliente")
    PeliHora = Funciones()
    Cantidadboletos = int(input("Ingrese la cantidad de boletos que desea comprar"))
    Cuenta = Cantidadboletos * 45
    
    Reserva = {
        "Nombre": Nombre,
        "Funcion y hora": PeliHora,
        "Cantidad de boletos": Cantidadboletos,
        "Cuenta": Cuenta
    }



while True:
    print("1 = Hacer reservas")
    print("2 = Ver reservas")
    opcion = input()

    if opcion == "1":
        print()
    elif opcion == "2":
        print()
