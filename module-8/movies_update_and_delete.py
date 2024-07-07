import mysql.connector
from mysql.connector import errorcode

# Method from the assignment instructions
def show_films(cursor, title):
    # method to execute an inner join on all tables,
    #   iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id;")

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # iterate over the film dataset and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))


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

    show_films(cursor, "DISPLAYING FILMS")

    ## Insert a new movie record (NOT STAR WARS) ##
    insertQuery = "INSERT INTO film(film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES(4, 'Raiders of the Lost Ark', 1981, 115, 'Steven Spielberg', 4, 4);"
    cursor.execute(insertQuery)
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    ## Update Aliens to be Horror ##
    updateQuery = "UPDATE film SET genre_id=1 WHERE film_name='Alien';"
    cursor.execute(updateQuery)
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    ## Delete Gladiator from the films list ##
    deleteQuery = "DELETE FROM film WHERE film_name='Gladiator';"
    cursor.execute(deleteQuery)
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


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


