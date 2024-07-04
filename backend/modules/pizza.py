class Pizza:
    def __init__(self,nombre,tamanio,precio):
        self.nombre_ =   nombre 
        self.tamanio = tamanio 
        self.precio = precio
    
    def query_pizza(self, table:str) -> str:
        return f"""
            INSERT INTO {table} 
            (nombre, tamanio, precio) 
            VALUES
            ('{self.nombre}','{self.tamanio}',{self.precio}) ;"""

    def delete_query(self , table:str ) -> str:
        return f"""
        DELETE FROM {table}
        WHERE 
            nombre = '{self.nombre}'
        """

    def update_query(self,table, modified_field, value_field) -> str:
        if modified_field == 'precio':
            return f"""
            UPDATE {table}
                SET {modified_field} = {value_field}
            WHERE 
                nombre = '{self.nombre}'
            """

        return f"""
        UPDATE {table}
            SET {modified_field} = '{value_field}'
        WHERE 
            nombre = '{self.nombre}'
        """