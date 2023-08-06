import sqlite3

# нужно сделать  delete, select 

class Database:
    name : str 
    db_type : str
    cursor : str
    conn : str
    debug : bool

    def __init__(self, name : str, db_type : str, debug : bool = False) -> None:
        self.debug = debug
        self.name = name
        self.db_type = db_type
        self.conn = sqlite3.connect(f"./{self.name}.{self.db_type}")
        self.cursor = self.conn.cursor()
    
    def debuger(self, sql_command : str):
        if self.debug:
            print(sql_command)
        else:
            print("")

    
    def create_table(self, tabel_name : str, table_structure : dict = {}):
        query = ""
        for name, type in table_structure.items():
            query += f"{name} {type}, "
        query = f"CREATE TABLE {tabel_name} (id integer PRIMARY KEY, {query[:-2]})"
        self.debuger(query)
        self.cursor.execute(query)

    def insert(self, table_name : str = "", field_and_values : dict = {}):
        try:
            field = ", ".join(field_and_values.keys())
            values = ", ".join(field_and_values.values())
            query= f"INSERT INTO {table_name} ({field}) VALUES({values})"
            self.debuger(query)
            self.cursor.execute(query) 
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("in this table colum must be unique ")

    def update(self, table_name : str, field_and_value : dict )
        field_1 =  field_and_value.keys[1]
        value_1 =  field_and_value.values()[1]
        field_2 =  field_and_value.keys[2]
        value_2 =  field_and_value.values()[2]

        query = f"Update {table_name}  set {field_1} = {value_1} where {field_2} = {value_2} "
        self.debuger(query)
        self.cursor.execute(query)
        self.conn.commit()

    def get_warning(self, table_name : str, user_id : str):
        query = f"SELECT warnings from {table_name} where user_id = {user_id}"         
        self.cursor.execute(query) 
        self.conn.commit()
        self.debuger(query)
        print(self.cursor.execute(query).fetchall())
        warnings = self.cursor.execute(query).fetchall()[-1][-1]
        print(warnings)
        return int(warnings)

   
