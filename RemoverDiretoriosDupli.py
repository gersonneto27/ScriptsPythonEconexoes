import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="eco123",
                                  host="localhost",
                                  port="5432",
                                  database="econexoes")
    cur = connection.cursor()

    clientes = cur.execute('SELECT id FROM cliente')
    clientes = cur.fetchall()

    for cliente in clientes:
        diretorios = cur.execute(
            "SELECT id,nome,cliente_id FROM diretorio where cliente_id = {}".format(cliente[0]))
        diretorios = cur.fetchall()
        for i in range(len(diretorios)):
            for j in range(i+1, len(diretorios)):
                if diretorios[i][1] == diretorios[j][1]:
                    cur.execute(
                        'Delete from diretorio where id = {}'.format(diretorios[j][0]))
    print("Deletados com Sucesso!!!!!")
    connection.commit()
except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cur.close()
        connection.close()
        print("PostgreSQL connection is closed")
