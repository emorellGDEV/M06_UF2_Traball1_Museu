import psycopg2
import Config


def connect_db():
    conn = psycopg2.connect(
        host=Config.host,
        port=Config.port,
        dbname=Config.dbname,
        user=Config.user,
        password=Config.password,
        sslmode=Config.sslmode,
        sslcompression=Config.sslcompression
    )
    return conn


def llistat_bens():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM bens_culturals")
    bens = cur.fetchall()
    conn.close()
    return bens


def llistat_colleccions():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM col_leccions")
    colleccions = cur.fetchall()
    conn.close()
    return colleccions


def afegir_ben():
    conn = connect_db()
    cur = conn.cursor()
    nom = input("Nom del ben: ")
    descripcio = input("Descripció del ben: ")
    data = input("Data de creació del ben (format AAAA-MM-DD): ")
    autor_id = input("ID de l'autor del ben: ")
    col_leccio_id = input("ID de la col·lecció del ben: ")
    cur.execute("INSERT INTO bens_culturals (nom, descripcio, data_creacio, id_autor, id_col_leccio) "
                "VALUES (%s, %s, %s, %s, %s)",
                (nom, descripcio, data, autor_id, col_leccio_id))
    conn.commit()
    conn.close()


def afegir_colleccio():
    conn = connect_db()
    cur = conn.cursor()
    nom = input("Nom de la col·lecció: ")
    descripcio = input("Descripció de la col·lecció: ")
    cur.execute("INSERT INTO col_leccions (nom, descripcio) VALUES (%s, %s)", (nom, descripcio))
    conn.commit()
    conn.close()


def llistat_bens_colleccio():
    conn = connect_db()
    cur = conn.cursor()
    col_leccio_id = input("ID de la col·lecció: ")
    cur.execute("SELECT * FROM bens_culturals WHERE id_col_leccio = %s", (col_leccio_id,))
    bens = cur.fetchall()
    conn.close()
    return bens


def llistat_bens_anteriors():
    conn = connect_db()
    cur = conn.cursor()
    data = input("Data (format AAAA-MM-DD): ")
    cur.execute("SELECT * FROM bens_culturals WHERE data_creacio < %s", (data,))
    bens = cur.fetchall()
    conn.close()
    return bens


while True:
    print("+-----------------------------------------+")
    print("|   Gestió de béns culturals del museu    |")
    print("+-----------------------------------------+")
    print("|1. Llistar tots els béns                 |")
    print("|2. Llistar les diferents col·leccions    |")
    print("|3. Afegir un bé a una col·lecció         |")
    print("|4. Afegir una col·lecció                 |")
    print("|5. Llistar els béns d'una col·lecció     |")
    print("|6. Llistar els béns anteriors a una data |")
    print("|0. Sortir                                |")
    print("+-----------------------------------------+")
    opcio = input("Opció: ")

    if opcio == "1":
        bens = llistat_bens()
        print("+-----------------------------------------+")
        for ben in bens:
            print(ben)
        print("+-----------------------------------------+")


    elif opcio == "2":
        colleccions = llistat_colleccions()
        print("+-----------------------------------------+")
        for colleccio in colleccions:
            print(colleccio[1])
        print("+-----------------------------------------+")


    elif opcio == "3":
        afegir_ben()
        print("+-----------------------------------------+")
        print("|        Ben afegit correctament          |")
        print("+-----------------------------------------+")

    elif opcio == "4":
        afegir_colleccio()
        print("+-----------------------------------------+")
        print("|    Col·lecció afegida correctament      |")
        print("+-----------------------------------------+")

    elif opcio == "5":
        bens = llistat_bens_colleccio()
        print("+-----------------------------------------+")
        for ben in bens:
            print(ben)
        print("+-----------------------------------------+")


    elif opcio == "6":
        bens = llistat_bens_anteriors()
        print("+-----------------------------------------+")
        for ben in bens:
            print(ben)
        print("+-----------------------------------------+")



    elif opcio == "0":
        print("+-----------------------------------------+")
        print("|           Programa finalitzat           |")
        print("+-----------------------------------------+")

        break

    else:
        print("Opció no vàlida, si us plau, trieu una altra opció")
