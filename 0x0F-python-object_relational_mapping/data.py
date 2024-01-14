#!/usr/bin/python3

import MySQLdb
import sys


def check_database_existence(username, password, database_name):
    cursor = None
    db = None
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                user=username, passwd=password, db=database_name)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the query to check for database existence
        query = "SHOW DATABASES LIKE %s"
        cursor.execute(query, (database_name,))

        # Fetch the result
        result = cursor.fetchone()

        # Display the result
        if result:
            print(f"The database '{database_name}' exists.")
        else:
            print(f"The database '{database_name}' does not exist.")

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to check database existence
    check_database_existence(username, password, database)
