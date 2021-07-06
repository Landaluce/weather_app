from sqlite3 import Error, connect


def create_connection(path):
    connection = None
    try:
        connection = connect(path)
    except Error as e:
        print(f"Error: '{e}' ")
    return connection, connection.cursor()
