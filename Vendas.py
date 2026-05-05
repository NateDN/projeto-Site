import streamlit as st         # Importa o Streamlit (interface web)
import crud_db                 # Importa seu módulo de banco de dados (CRUD)
from datetime import datetime  # Importa para trabalhar com data e hora

st.title("Vendas") # aqui eu mostro o título da página como "Vendas"

clientes = crud_db.selecionar("clientes") # aqui eu crio a variável clientes e defino (=) que ela recebe todos os dados da tabela clientes do banco

produtos = crud_db.selecionar("produtos") # aqui eu crio a variável produtos e defino (=) que ela recebe todos os dados da tabela produtos do banco

cliente_dict = {c[1]: c[0] for c in clientes}  
# aqui eu crio a variável cliente_dict e defino (=) um dicionário
# para cada cliente (c), eu pego:
# c[1] = nome do cliente → vira a chave
# c[0] = id do cliente → vira o valor
# resultado: {nome_cliente: id_cliente}


produto_dict = {p[1]: (p[0], p[2]) for p in produtos}  
# aqui eu crio a variável produto_dict e defino (=) um dicionário
# p[1] = nome do produto → chave
# p[0] = id do produto
# p[2] = preço do produto
# resultado: {nome_produto: (id_produto, preco)}


# 🔒 Proteção: listas vazias
if not cliente_dict:  
# aqui eu verifico se o dicionário de clientes está vazio

    st.warning("Nenhum cliente cadastrado.")  
    # aqui eu mostro uma mensagem de aviso

    st.stop()  
    # aqui eu paro a execução para evitar erro


if not produto_dict:  
# aqui eu verifico se o dicionário de produtos está vazio

    st.warning("Nenhum produto cadastrado.")  
    # aqui eu mostro um aviso

    st.stop()  
    # aqui eu paro a execução


cliente = st.selectbox("Cliente", list(cliente_dict.keys()))  
# aqui eu crio a variável cliente e defino (=) um campo de seleção
# list(cliente_dict.keys()) = pega todos os nomes dos clientes


produto = st.selectbox("Produto", list(produto_dict.keys()))  
# aqui eu crio a variável produto e defino (=) um campo de seleção
# lista com nomes dos produtos


qtd = st.number_input("Quantidade", min_value=1)  
# aqui eu crio a variável qtd e defino (=) um campo numérico
# min_value = define (=) que o mínimo permitido é 1


# ✅ Agora sempre seguro
produto_id, preco = produto_dict[produto]  
# aqui eu pego o produto selecionado e defino (=) duas variáveis:
# produto_id = id do produto
# preco = preço do produto


# ✅ cálculo do total (ANTES de usar)
total = preco * qtd  
# aqui eu crio a variável total e defino (=) o resultado da multiplicação do preço pela quantidade


st.write(f"💰 Total: R$ {total:.2f}")  
# aqui eu mostro o valor total na tela
# :.2f = define (=) que o número terá 2 casas decimais


if st.button("Registrar Venda"):  
# aqui eu crio um botão chamado "Registrar Venda"
# quando clicado, executa o código abaixo

    crud_db.inserir("vendas", {  
    # aqui eu chamo a função inserir do banco
    # "vendas" é o nome da tabela onde será salvo

        "cliente_id": cliente_dict[cliente],  
        # aqui eu envio o id do cliente baseado no nome selecionado

        "produto_id": produto_id,  
        # aqui eu envio o id do produto

        "quantidade": qtd,  
        # aqui eu envio a quantidade digitada

        "total": total,  
        # aqui eu envio o valor total calculado

        "data": datetime.now().strftime("%Y-%m-%d %H:%M")  
        # aqui eu envio a data atual
        # datetime.now() = pega data e hora atual
        # strftime = define (=) o formato da data (ano-mês-dia hora:minuto)

    })
    st.success("Venda registrada!")  
    # aqui eu mostro uma mensagem de sucesso na tela
    
#_________________________________________
#✔ Integração entre tabelas
#Clientes
#Produtos
#Vendas
#_________________________________________
#✔ Lógica inteligente
#Usa dicionários para mapear nome → ID
#Evita erros de referência
#_________________________________________
#✔ Segurança
#Bloqueia execução se não houver dados
#Evita erro de produto inexistente
#_________________________________________