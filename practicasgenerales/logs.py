log = [
    "LOG : WARNING:  LOGIN FAILED FROM IP : 192.34.21.1",
    "LOG: LOGIN SUCCESS FROM IP : 192.31.2.24",
    "LOG : WARNING:  FILE DOWNLOADED FROM IP : 192.34.21.4",
    "LOG : WARNING:  LOGIN FAILED FROM IP : 192.34.21.1",
    "LOG: ATTEMPT LOGIN FAILED FROM IP : 192.31.2.24 (1)",
    "LOG: ATTEMPT LOGIN FAILED FROM IP : 192.31.2.24 (2)",
    "LOG : WARNING:  FILE DOWNLOADED FROM IP : 192.34.21.4",

]

#filtrado de logs especiales (descargas , logins,)

def filtrodown():
    downloads = 0
    for d in log:
        if "DOWNLOADED" in d:
            downloads += 1

    if downloads > 0:
        print(f"Hubieron {downloads} descargas en este segmento")
    else:
        print("No se vieron descargas")


def fillogin():
    logins = 0
    flogins = 0
    for l in log:
        if "LOGIN SUCCESS" in l: logins += 1
        elif "LOGIN FAILED" in l: flogins += 1

    if logins == 0 and flogins == 0:
        print("NO HUBIERON LOGINS REGISTRADOS")
    print(f"LOGINS FALLIDOS: {flogins} | logins validados: {logins}")


while True:
    print("FILTRADO DE LOGS")
    print("1.- Descargas")
    print("2- Logins")
    print("3.-Ver todos los logs")
    print("4.- Salir")

    opcion = int(input(("Ingrese su opcion: ")))
    match opcion:
     case 1:
        filtrodown()
     case 2:
         fillogin()
     case 3:
            print(log)
     case 4:
            break

