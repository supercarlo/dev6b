import DBConnect
import psycopg2

conn_string = psycopg2.connect("host='83.86.251.189' dbname='postgres' user='postgres' password='postgres' port='5432'")
cur = conn_string.cursor()


def Username():
    cur.execute('SELECT "Username" FROM "User"')
    for i in cur:
        print (i)


