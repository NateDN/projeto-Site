import streamlit as st # Importa o Streamlit (criação da interface web)
import pandas as pd # Importa o Pandas (manipulação de dados em tabela)
import crud_db # Importa seu módulo de banco de dados (CRUD)

st.title("Clientes") # Título da página

nome = st.text_input("Nome") # Campo de entrada de texto para o nome do cliente
telefone = st.text_input("Telefone") # Campo para telefone
email = st.text_input("Email") # Campo para email

if st.button("Cadastrar"):        # Cria um botão; quando clicado, executa o bloco abaixo
    crud_db.inserir("clientes", { # Chama função para inserir dados na tabela "clientes"
        "nome": nome,             # aqui eu envio o valor da variável nome para a coluna "nome" no banco
        "telefone": telefone,     # aqui eu envio o valor da variável telefone para a coluna "telefone"
        "email": email            # aqui eu envio o valor da variável email para a coluna "email"
    })
    st.success("Cliente cadastrado!") # Mostra mensagem de sucesso na tela

dados = crud_db.selecionar("clientes") # Busca todos os registros da tabela "clientes"

df = pd.DataFrame(dados, columns=["ID", "Nome", "Telefone", "Email"]) 
# Converte os dados (lista de tuplas) em DataFrame (tabela organizada)

st.dataframe(df) # Exibe a tabela interativa no Streamlit

id_delete = st.number_input("ID para deletar", min_value=0) 
# Campo numérico para o usuário informar o ID que deseja excluir

if st.button("Excluir"):                   # Botão para deletar cliente
    crud_db.deletar("clientes", id_delete) # Remove o cliente com o ID informado
    st.warning("Cliente removido!")        # Mostra aviso de remoção