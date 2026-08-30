import sqlite3

def ct():
    db = sqlite3.connect("mydb.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, edad INTEGER)")
    db.close()

def insertdata(datos):
    db = sqlite3.connect("mydb.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", datos)
    db.commit()
    db.close()
    print("Datos insertados con éxito")


def rdata():
    db = sqlite3.connect("Mydb.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios")
    filas = cursor.fetchall()
    
    print("datos en la tabla")
    for fila in filas:
        print(f"ID: {fila[0]} | Nombre: {fila[1]} | Edad: {fila[2]}")
    if not filas:
        print("No hay datos en la tabla")
    
    db.close()

def main():
    pass
    

    #insertdata(("Juan", 25))
    insertdata(("Alejandro", 17))
    #insertdata(("Alejandra", 19))
    #insertdata(("Alena", 19))
    
    
    #rdata() 
    

def duser():
    db = sqlite3.connect("mydb.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM usuarios WHERE nombre = ? " ,("Alejandro" ,))
    db.commit()
    db.close()
    
#main()
#duser()
#rdata()

def updt():
    db = sqlite3.connect("mydb.db")
    cursor = db.cursor()
    cursor.execute("UPDATE usuarios SET id = ? WHERE nombre = ?", (1, "Alejandro" ))
    db.commit()
    db.close()
    
    
def dall():
    db = sqlite3.connect("mydb.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM usuarios")
    db.commit()
    db.close()
#updt()
#rdata()
dall()
main()
updt()
rdata()