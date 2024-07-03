from sqlalchemy import create_engine , text

class SqliteDataBase:
    def __init__(self, path_cnx: str, table:str = 'pizza'):

        path_cnx = f'sqlite:///{path_cnx}'

        self.engine = create_engine(path_cnx)
        self.table = table
        query  = f"""
        CREATE TABLE IF NOT EXISTS {self.table} (
            id_pizza INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(254),
            tamanio VARCHAR(254),
            precio INT
        )
        """
        self._query_runner(query)

    def _query_runner(self, query) -> None:
        with self.engine.connect() as conn:
            result = conn.execute( text(query))
            conn.commit()
        print("sucess! the database is created")

    

    def get_all_pizza(self):
        query = f"SELECT * FROM {self.table}"

        with self.engine.connect() as conn:
            result = conn.execute(text(query)).fetchall()

        return result

    def get_one_pizza(self, nombre_pizza):
        query = f"""
        SELECT
            *
        FROM {self.table}
        WHERE 
            nombre LIKE '%{nombre_pizza}%'
        """

        with self.engine.connect() as conn:
            result = conn.execute(text(query)).fetchone()

        return result


    def insert_one_pizza(self, pizza):
        query_insertar:str = pizza.query_pizza(self.table)
        self._query_runner(query_insertar)
    