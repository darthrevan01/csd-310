import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "7#x2X_p?q35x6!X",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n  Press any key to continue...")

    cursor = db.cursor()

    ## Step One: Set up the query statements ##

    # First query for all fields in studio
    query1 = "SELECT * FROM studio;"

    # Second query for all fields in genre
    query2 = "SELECT * FROM genre"
    
    # Third query is to select movie names with a run time of less than 2 hours
    query3 = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;"

    # Fourth query is to get a list of film names, and its director grouped by director
    query4 = "SELECT  film_name, film_director FROM film ORDER BY film_director"


    ## Step Two/Three: Execute the Queries/Print the Results ##
    
    # Execute Query 1 and print the results
    cursor.execute(query1)
    studioResults = cursor.fetchall()

    print("\n-- DISPLAYING Studio RECORDS --")
    for studio in studioResults:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))
    
    # Execute Query 2 and print the results
    cursor.execute(query2)
    genreResults = cursor.fetchall()

    print("\n-- DISPLAYING Genre RECORDS --")
    for genre in genreResults:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))
    
    # Execute Query 3 and print the results
    cursor.execute(query3)
    filmResults = cursor.fetchall()

    print("\n-- DISPLAYING Short Film RECORDS --")
    for shortFilm in filmResults:
        print("Film Name: {}\nRuntime: {}\n".format(shortFilm[0], shortFilm[1]))
    
    # Execute Query 4 and print the results
    cursor.execute(query4)
    directorResults = cursor.fetchall()
    # print(directorResults)

    print("\n-- DISPLAYING Director RECORDS in Order --")
    for director in directorResults:
        print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

finally:
    cursor.close()
    db.close()