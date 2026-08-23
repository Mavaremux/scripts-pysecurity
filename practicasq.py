import sqlite3

conn = sqlite3.connect("mercado.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS gastos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    concept TEXT NOT NULL,
    monto REAL NOT NULL)
""")

conn.commit()

def agregar_gasto():
    print("NUEVO GASTO---")

    concept = input("En que gastaste?")
    monto = float(input("Cuanto gastaste?"))
    cursor.execute("INSERT INTO gastos (concept, monto) VALUES (?, ?) ", (concept, monto)) #estructura por ahroa no cambia
    conn.commit()
    print("Gasto Guardado con exito")
    
    
def ver_gastos():
    print("TUS GASTOS")
    cursor.execute("SELECT * FROM gastos")
    resultados = cursor.fetchall()

    if not resultados:
        print("No hay gastos registrados anteriormente")
    else:
        for fila in resultados:
            print(f"ID: {fila[0]} Concepto: {fila[1]} Monto: {fila[2]}")

def delid():
    print("Elimina gastos que sean innecesarios solamente")
    iddeling = input("Ingrese el concepto de gasto que quiere eliminar ")
    cursor.execute("DELETE FROM gastos WHERE id = ?", (iddeling, ))

    conn.commit()
    print("Gatos guardados exitosamente")

def delall():
    op = input("Eliminaras todos los registros, pagos , montos, ¿estas seguro de continuar? (s/n)")
    if op == "s":
        cursor.execute("DELETE FROM gastos")
        conn.commit()
        print("----")
        print("----")
        print("Se eliminaron todos los gastos")
    elif op == "n":
        print("No se elimino nada, vuelve a empezar")
    else:
        print("Elige una opcion valida")

while True:
    print("Bienvenido al rescatafondospy!")
    print("1.- Depositar dinero")
    print("2- Ver Depositos")
    print("3- Eliminar registros de depositos")
    print("4- Eliminar todos los registros")
    print("5- Salir del banco")

    opc = int(input("Seleccione una opcion:  "))

    if opc == 1:
        agregar_gasto()

    elif opc == 2:
        ver_gastos()

    elif opc == 3:
        delid()

    elif opc == 4:
        delall()

    elif opc == 5:
        print("Adios")
        conn.close()
        break