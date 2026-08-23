import sqlite3

# 1. CONNECT: Abres la puerta (Creas la conexión)
con = sqlite3.connect("mi_lab.db") 

# 2. CURSOR: Contratas al asistente (Creas el cursor)
cur = con.cursor()

# 3. EXECUTE: Le gritas la orden al asistente
cur.execute("""CREATE TABLE IF NOT EXISTS mediciones ( 
          experimento TEXT ,
            valores INTEGER 
        )
""")
datos = [
    ("Prueba 1:" , 16),
    ("Prueba 2:" , 18),
    ("Prueba 3:", 20),
    ("Prueba 4:" , 12)
]

cur.executemany("INSERT INTO mediciones VALUES (?, ?)" , datos)

con.commit()
print("Datos guardados exitosamente")
cur.execute("SELECT * FROM mediciones")
print(cur.fetchall())
con.close()