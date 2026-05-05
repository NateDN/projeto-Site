# (O CÉREBRO DO SISTEMA)

import sqlite3  # aqui eu importo o sqlite3, que é o módulo responsável por trabalhar com banco de dados SQLite dentro do Python
from pathlib import Path  # aqui eu importo Path, que é uma forma moderna de lidar com caminhos de arquivos no sistema
import logging  # aqui eu importo logging, que serve para registrar eventos do sistema, tipo um histórico do que aconteceu

DB_PATH = Path("crud_db.db")  # aqui eu crio a variável DB_PATH e defino (=) que o banco de dados será um arquivo chamado "crud_db.db"

# Configuração de logging
logging.basicConfig(  # aqui eu começo a configuração do sistema de logs
    filename="log.txt",  # aqui eu defino (=) que os registros serão salvos no arquivo "log.txt"
    level=logging.INFO,  # aqui eu defino (=) o nível mínimo do log como informação (INFO)
    format="%(asctime)s - %(levelname)s - %(message)s"  # aqui eu defino (=) o formato do log com data, nível e mensagem
)

# Função de conexão
def conectar():  # aqui eu defino a função conectar, que será usada sempre que precisar acessar o banco
    return sqlite3.connect(DB_PATH)  # aqui eu retorno (=) uma conexão com o banco usando o caminho definido

# Criar tabelas
def inicializar_db():  # aqui eu defino a função que cria as tabelas do banco
    conn = conectar()  # aqui eu crio a variável conn e defino (=) que ela recebe a conexão com o banco
    cursor = conn.cursor()  # aqui eu crio a variável cursor e defino (=) o cursor que executa comandos SQL


    cursor.execute("""                               
    CREATE TABLE IF NOT EXISTS clientes (            
        id INTEGER PRIMARY KEY AUTOINCREMENT,        
        nome TEXT NOT NULL,                          
        telefone TEXT,                               
        email TEXT                                   
    )
    """)

# na linha 26: aqui eu executo um comando SQL
# na linha 27: aqui eu mando criar a tabela clientes caso ela ainda não exista
# na linha 28: aqui eu crio o campo id, que é único e auto incrementa automaticamente
# na linha 29: aqui eu crio o campo nome e ele é obrigatório (não pode ser vazio)
# na linha 30: aqui eu crio o campo telefone, que é opcional
# na linha 31: aqui eu crio o campo email, também opcional

    cursor.execute("""                           
    CREATE TABLE IF NOT EXISTS produtos (        
        id INTEGER PRIMARY KEY AUTOINCREMENT,    
        nome TEXT NOT NULL,                      
        preco REAL,                              
        estoque INTEGER                          
    )
    """)

# na linha 42: aqui eu executo outro comando SQL
# na linha 43: aqui eu crio a tabela produtos se ela não existir
# na linha 44: aqui eu crio o id automático
# na linha 45: aqui eu crio o nome do produto, obrigatório
# na linha 46: aqui eu crio o campo preço (valor numérico decimal)
# na linha 47: aqui eu crio o campo estoque (quantidade de itens)

    cursor.execute("""                                    
    CREATE TABLE IF NOT EXISTS vendas (                   
        id INTEGER PRIMARY KEY AUTOINCREMENT,             
        cliente_id INTEGER,                               
        produto_id INTEGER,                               
        quantidade INTEGER,                               
        total REAL,                                       
        data TEXT,                                        
        FOREIGN KEY(cliente_id) REFERENCES clientes(id),  
        FOREIGN KEY(produto_id) REFERENCES produtos(id)   
    )
    """)

# 58: aqui eu executo mais um comando SQL
# 59: aqui eu crio a tabela vendas
# 60: aqui eu crio o id automático
# 61: aqui eu crio o campo cliente_id (referência ao cliente)
# 62: aqui eu crio o campo produto_id (referência ao produto)
# 63: aqui eu crio o campo quantidade vendida
# 64: aqui eu crio o campo total da venda
# 65: aqui eu crio o campo data (armazenado como texto)
# 66: aqui eu defino que cliente_id é uma chave estrangeira ligada à tabela clientes
# 67: aqui eu defino que produto_id é uma chave estrangeira ligada à tabela produtos


    conn.commit()  # aqui eu salvo todas as alterações feitas no banco de dados
    conn.close()  # aqui eu fecho a conexão com o banco
    logging.info("Banco inicializado.")  # aqui eu registro no log que o banco foi inicializado


# CRUD genérico

def inserir(tabela, dados):  # aqui eu defino a função inserir, que recebe o nome da tabela e os dados
    conn = conectar()  # aqui eu crio a variável conn e defino (=) a conexão com o banco
    cursor = conn.cursor()  # aqui eu crio o cursor que executa comandos


    colunas = ", ".join(dados.keys())  # aqui eu crio a variável colunas e defino (=) uma string com os nomes das colunas separados por vírgula
    placeholders = ", ".join(["?"] * len(dados))  # aqui eu crio a variável placeholders e defino (=) vários ? para segurança no SQL


    sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"  
    # aqui eu crio a variável sql e defino (=) o comando SQL de inserção já montado


    cursor.execute(sql, tuple(dados.values()))  
    # aqui eu executo o SQL passando os valores convertidos para tupla


    conn.commit()  # aqui eu salvo os dados no banco
    conn.close()  # aqui eu fecho a conexão
    logging.info(f"Inserido em {tabela}: {dados}")  # aqui eu registro no log o que foi inserido


def selecionar(tabela):  # aqui eu defino a função selecionar, que busca dados da tabela
    conn = conectar()  # aqui eu abro conexão com o banco
    cursor = conn.cursor()  # aqui eu crio o cursor


    cursor.execute(f"SELECT * FROM {tabela}")  
    # aqui eu executo o comando SQL para buscar todos os registros da tabela


    dados = cursor.fetchall()  
    # aqui eu crio a variável dados e defino (=) todos os resultados retornados


    conn.close()  # aqui eu fecho a conexão
    return dados  # aqui eu retorno os dados para quem chamou a função


def deletar(tabela, id):  # aqui eu defino a função deletar, que remove um registro pelo id
    conn = conectar()  # aqui eu abro conexão com o banco
    cursor = conn.cursor()  # aqui eu crio o cursor


    cursor.execute(f"DELETE FROM {tabela} WHERE id=?", (id,))  
    # aqui eu executo o comando SQL de exclusão usando ? para segurança


    conn.commit()  # aqui eu salvo a alteração
    conn.close()  # aqui eu fecho a conexão
    logging.info(f"Deletado {tabela} ID {id}")  # aqui eu registro no log o que foi deletado