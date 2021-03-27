#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset='utf8')

    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities JOIN states ON cities.state_id = states.id\
                    WHERE states.name = (%s)", [argv[4]])
    query_rows = cur.fetchall()
    
    lt1 = []
    for i in query_rows:
        lt1.append(i[0])
    for i in range(len(lt1)):
        if i + 1 == len(lt1):
            print(lt1[i])
        else:
            print("{}, ".format(lt1[i]), end="")
        #print(lista[i][0], end=" ", sep=', ')
    cur.close()
    db.close()
