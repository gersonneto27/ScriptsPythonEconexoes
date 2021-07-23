import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="eco123",
                                  host="localhost",
                                  port="5432",
                                  database="econexoes")
    cur = connection.cursor()

    orgaos = cur.execute('SELECT descricao,id,operador FROM orgaoemissor')
    orgaos = cur.fetchall()

    for i in range(len(orgaos)):
        for j in range(i+1, len(orgaos)):
            if orgaos[i][0] == orgaos[j][0].upper() and orgaos[i][2] == orgaos[j][2]:
                cur.execute(
                    'Delete from orgaoemissor where id = {}'.format(orgaos[j][1]))
    print("Deletados com Sucesso")
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cur.close()
        connection.close()
        print("PostgreSQL connection is closed")
