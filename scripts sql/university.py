#registro de materias de un estudiante universitario con #id,materia,semestre,nota,aprobado/desaprobado

import sqlite3
def main():
    db = sqlite3.connect("unidb.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS infmaterias (id INTEGER PRIMARY KEY AUTOINCREMENT, materia TEXT, semestre INTEGER,nota INTEGER, aprob TEXT)")
    db.commit()
    db.close()

def indata(datos):
    db = sqlite3.connect("unidb.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO infmaterias (materia, semestre, nota, aprob ) VALUES (? , ? , ? , ?)", datos)
    db.commit()
    db.close()

def rdata():
    db = sqlite3.connect("unidb.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM infmaterias")
    infs = cursor.fetchall()
    if len(infs) == 0:
        print("No hay materias registradas")
    else:
        for inf in infs:
            # inf[0] es el ID, inf[1] es la Materia, inf[2] Semestre, etc.
            print(f"ID: {inf[0]} | MATERIA {inf[1]}, SEMESTRE {inf[2]} , NOTA {inf[3]}")
    db.close()
    
def updtdata(nota,materia ):
    db = sqlite3.connect("unidb.db")
    cursor = db.cursor()
    cursor.execute("UPDATE infmaterias SET nota = ? WHERE materia = ? ",  (nota, materia ))
    db.commit()
    db.close()
    
def deldata(mtdel):
    db = sqlite3.connect("unidb.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM infmaterias WHERE materia = ? ", (mtdel,))
    print(f"Se eliminaron todos los datos de {mtdel}")
    db.commit()
    db.close()
    

#flujo modular
while True:
    print("REGISTRO BASICO DE INFORMACION UNIVERSITARIA")
    print("1.Crear registro")
    print("2. Insertar materia")
    print("3.Leer Registro")
    print("4. Modificar Registro")
    print("5. Eliminar materia")
    print("6. Salir")
    
    opc = input("Ingrese la opcion: ")
    if opc == "1":
        main()
    if opc == "2":
        materia = input("Materia: ")
        semestre = input("Semestre: ")
        nota = input("Nota: ")
        st = input(" Estado: ")
        dt = (materia, semestre, nota ,st)     
        print("Datos guardados correctamente")
        indata(dt)
    if opc == "5":
        mtdel = input("Ingrese la materia a eliminar")
        deldata(mtdel)
    if opc == "4":
        ntupdt = input("Ingrese la nota a modificar")
        mtupdt = input("Ingrese la materia a modificar")
        
        updtdata(ntupdt, mtupdt)
        print("Materia modificada correctamente")
    if opc == "3":
        rdata()
    if opc == "6":
        ("Adios")
        break
        
    
