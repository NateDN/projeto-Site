import streamlit as st # Importa o Streamlit (criação da interface web)
import pandas as pd # Importa o Pandas (usado para manipular dados em formato de tabela)
import crud_db # Importa seu módulo de banco de dados (CRUD)

nome = st.text_input("Nome do Produto")  
# aqui eu crio a variável nome e defino (=) que ela recebe o valor digitado pelo usuário no campo de texto "Nome do Produto"

preco = st.number_input("Preço", min_value=40.0)  
# aqui eu crio a variável preco e defino (=) que ela recebe um valor numérico digitado pelo usuário
# min_value = define (=) que o valor mínimo permitido para o preço é 40.0

estoque = st.number_input("Estoque", min_value=10.000)  
# aqui eu crio a variável estoque e defino (=) que ela recebe um valor numérico digitado
# min_value = define (=) que o valor mínimo permitido é 10.000
# observação: como está com ponto decimal, isso vira número com vírgula (float), não inteiro


if st.button("Cadastrar Produto"):  
# aqui eu crio um botão com o nome "Cadastrar Produto"
# quando o usuário clicar, o código abaixo será executado

    crud_db.inserir("produtos", {  
    # aqui eu chamo a função inserir do banco de dados
    # "produtos" é o nome da tabela onde os dados serão salvos

        "nome": nome,       # aqui eu envio o valor da variável nome para a coluna "nome" no banco
        "preco": preco,     # aqui eu envio o valor da variável preco para a coluna "preco"
        "estoque": estoque  # aqui eu envio o valor da variável estoque para a coluna "estoque"

    })

    st.success("Produto cadastrado!") # aqui eu mostro uma mensagem de sucesso na tela informando que o produto foi cadastrado


dados = crud_db.selecionar("produtos") # aqui eu crio a variável dados e defino (=) que ela recebe todos os registros da tabela "produtos" do banco


df = pd.DataFrame(dados, columns=["ID", "Nome", "Preço", "Estoque"])  
# aqui eu crio a variável df e defino (=) um DataFrame (tabela organizada)
# eu passo os dados vindos do banco e defino os nomes das colunas

st.dataframe(df) # aqui eu exibo o DataFrame (tabela) na tela de forma interativa