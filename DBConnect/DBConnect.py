import psycopg2
import sys


conn_string = "host='83.86.251.189' dbname='postgres' user='postgres' password='postgres' port='5432'" \
              # % (host, dbname, user, password, port)


    # print the connection string we will use to connect
print(
"Connecting to database\n ->%s" % (conn_string))

try:
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print(
    "Connected!\n")
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
