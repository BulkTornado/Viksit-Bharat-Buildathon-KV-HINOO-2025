import mysql.connector as _mysql
import sys
from tabulate import tabulate
"""try:

    ...
except Exception as error:
    print(
        "Database connection failed. Refer to following error report for more:\n"
    )

    self.show_exception_traceback(error)

    print("\nTerminating script early.")
    sys.exit()"""

class ConnectToMySQL:
    def __init__(self, host: str, user: str, passwd: str):
        self._host = host
        self._user = user
        self._passwd = passwd
        self._db_connection = _mysql.connect(
            host=self._host,
            user=self._user,
            passwd=self._passwd
        )
        self._cursor_object = self._db_connection.cursor()


    #connect_to_database
    def __enter__(self):
        return self


    def execute_sql_query(self, sql_query: str) -> None:
        try:
            #print(f"[DEV MODE] Executing SQL Query: \n{sql_query}\n")
            self._cursor_object.execute(sql_query)
        except Exception as error:
            self.show_exception_traceback(error)
            self.close_connection()

    def fetch_data(self):
        return self._cursor_object.fetchall()

    def close_connection(self) -> None:
        self._db_connection.close()

    def check_connection(self) -> bool:
        return self._db_connection.is_connected()

    def check_result_set(self):
        return self._cursor_object.description

    def get_column_name(self):
        return self._cursor_object.description

    def rows_retrieved(self) -> int:
        return self._cursor_object.rowcount

    def show_exception_traceback(self, e: Exception) -> None:

        print("[DEV MODE] Showing full exception traceback:\n")
        print(repr(e))
        print('\n')
        print(e)

        return

    def __str__(self) -> str:
        return f"ConnectToMySQL"

    def __repr__(self) -> str:
        return f"{__name__}"

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        self._db_connection.close()
        print('Connection closed.')


if __name__ == "__main__":
    print("You are not supposed to run this program by itself.")
    #sys.exit()
    with ConnectToMySQL('localhost', 'root', 'tks@123?') as c:
        c.execute_sql_query('USE Amazon;')
        c.execute_sql_query('SELECT * FROM customer_information WHERE customer_email_address = \'roy982shruti@gmail.com\';')

        _ = c.fetch_data()
        print(_[0][0]) # type: ignore
        column = [desc[0] for desc in c.get_column_name()] # type: ignore

        #with open('t.txt', 'w') as f:
        print(tabulate(_, headers=column, tablefmt='simple'))
