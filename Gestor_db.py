import sqlite3
#Tratamiento de errores en DB
#OperationalError (Cuando la tabla ya existe)
def crear_db():
    con = sqlite3.connect("alumnos.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE libro (id INTEGER PRIMARY KEY AUTOINCREMENT)")
    cur.execute('''CREATE TABLE alumnos 
    (
    dni INTEGER PRIMARY KEY NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    folio INTEGER NOT NULL,
    libro INTEGER NOT NULL,
    FOREIGN KEY (libro) REFERENCES libro (id)
    )
    ''')
    con.commit()
    con.close()

def ingresar_alumno_db(datos_alumno):
    con = sqlite3.connect("alumnos.db")
    cur = con.cursor()
    cur.execute("INSERT INTO alumnos VALUES (?,?,?,?)", datos_alumno)
    con.commit()
    con.close()

def buscar_dni_db(dni):
    con = sqlite3.connect("alumnos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM alumnos WHERE dni = ?", dni)
    datos = cur.fetchone()
    con.close()

def buscar_libro_db(nLibro):
    con = sqlite3.connect("alumnos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM alumnos WHERE nLibro = ?", nLibro)
    datos = cur.fetchall()
    con.close()

def borrar_alumno_db(dni):
    con = sqlite3.connect("alumnos.db")
    cur = con.cursor()
    cur.execute("DELETE FROM alumnos WHERE dni = ?", dni)
    con.commit()
    con.close()



