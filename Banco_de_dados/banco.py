#Conectando com banco de dados
def conectar_banco():
    return mysql.connector.connect(
        host='localhost', 
        user = 'root', 
        password = '', 
        database = 'pins', 
        charset = 'utf8'
    )