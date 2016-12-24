import DBConnect
import psycopg2

conn_string = psycopg2.connect("host='83.86.251.189' dbname='postgres' user='postgres' password='postgres' port='5432'")
cur = conn_string.cursor()


def PokemonType():
    cur.execute('SELECT * FROM "PokemonList"')
    for i in cur:
        print (i)


PokemonType()