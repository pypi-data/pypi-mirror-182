import sys
import mysql.connector
from mysql.connector import errorcode

class DB:    
    
    def __init__(self, config_file, **kwargs):
        """_summary_

        Args:
            config_file (str, optional): _description_. Defaults to ''.
        """
        
        self.config_file = ''
        self.__set_config_file(config_file)
        
        self.config = {}
        self.__set_config()
        
        self.db_name = {}
        self.__set_db_name()
        
        self.connection = {}                
        self.cursors = {}    
        
        self.query_operation = ''
        self.query_statement = ''
        self.query_data = {}
        self.query_results = {}
    
    
    def set_db_name(self, db_name=None):
        self.db_name = self.config['database'] if db_name is None else db_name
        return self       
    
    __set_db_name = set_db_name    
    
    def get_db_name(self):
        return self.db_name
    
    def read_config_file(self):
        c = []
        with open(self.config_file, 'r') as fh:
            for line in fh:
                c.append(line.strip().split(':'))
        return c        
    
    def set_config(self):
        self.config = {'host':'','user':'','password':'', 'database':''}
        configs = self.read_config_file()
        for config in configs:
            if config[0] in self.config:
                self.config[config[0]] = config[1]
    
    
    
    def get_config(self):
        
        return self.config
    
    __set_config = set_config
    
    __get_config = get_config
        
        
        
    def set_config_file(self, config_file):
        self.config_file = config_file
    
    def get_config_file(self):
        return self.config_file
    
    __set_config_file = set_config_file
    
    __get_config_file = get_config_file
        
        
    
    def connect(self, db_name=None):
        
        try:
            
            self.config['database'] = self.db_name if db_name is None else db_name
            
            connection = mysql.connector.connect(**self.config)
            
            self.connection[self.db_name] = connection
            
            self.cursors[self.db_name] = connection.cursor(buffered=True)
            
            return self
        
        except mysql.connector.Error as err:
            
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                
                print('Error: Something wrong with your username or password')    
                            
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                
                print(f"Error: Database {self.config['database']} does not exists")
                
            else:
                
                print(err)
                
            exit()
            
    __connect = connect        
    
    
    
    def execute(self, operation, params=None, cursor=None):
        
        db_name = self.get_db_name()
        conn = self.connection[db_name]
        cursor = self.cursors[db_name] = conn.cursor(buffered=True, dictionary=True)
        self.query_operation = operation
        self.query_data = params
        
        opword = operation.strip().split(' ')[0].lower()        
        
        
        if 'select' in opword:
            self.query_operation = 'select'
            self.query_statement = operation
            cursor.execute(operation, params)
            
            cursor.execute(operation) if params is None else cursor.execute(operation, params)
            rows = self.query_results = cursor.fetchall()
            conn.commit()
            return rows
        
        elif 'insert' in opword or 'update' in opword :
            self.query_operation = 'insert or update'
            self.query_statement = operation
            
            cursor.execute(operation) if params is None else cursor.execute(operation, params)
            conn.commit()
            self.query_results = 'executed successfully'
            return True
        
        
        
    def new_cursor(self, cursor_name='default', buffered=True, dictionary=True):
        """Create new mysql cursor

        Args:
            cursor_name (str, optional): if not specified, name will be 'default'. Defaults to 'default'.
            buffered (bool, optional): _description_. Defaults to True.

        Returns:
            _type_: mysql cursor
        """
        db_name=self.get_db_name()
        
        if cursor_name == 'default':
            cursor = self.connection[db_name].cursor(buffered = buffered, dictionary=dictionary)
            self.cursors[cursor_name] = cursor            
        else:
            self.cursors[cursor_name] = self.connection.cursor(buffered = buffered, dictionary=dictionary)
        
        return self.cursors[cursor_name]
        
        
        
    def get_cursor(self, cursor_name='default'):
        """If cursor name not specified it will create a default cursor and return it

        Args:
            cursor_name (str, optional): _description_. Defaults to 'default'.

        Returns:
            _type_: _description_
        """
        
        # if cursor name not specified, then return first cursor available        
        if len(self.cursors) == 0:
            # if no name specified, create a default one
            if cursor_name == 'default':
                cursor = self.new_cursor()            
            else:
                new_cursor = self.new_cursor(cursor_name)
                cursor = new_cursor            
        else:
            # check from list of available cursors if name available
            if cursor_name == 'default':
                cursor = self.new_cursor()
            elif cursor_name not in self.__dict__['cursors'].keys():
                #cursor = self.new_cursor(cursor_name)
                raise Exception(f'Undefined cursor: {cursor_name}')
            else :
                cursor = self.cursor[cursor_name]
            
        return cursor
            
    

    def run_query(self, query=str, cursor=None, *kwargs)  :
        
        cursor = self.get_cursor() if not cursor else self.get_cursor(cursor)
        #raise Exception('Cursor is not defined. It is require to run query')
        
        if not query:
            raise Exception('Unspecified query')            
            
        cursor.execute(query)
        rows = cursor.fetchall()
        self.query_results = rows
        return self.query_results                
        
        
        
    def get_connection(self):
        
        return self.connection    
        

    
    def get_attributes(self):
        
        return self.__dict__
    