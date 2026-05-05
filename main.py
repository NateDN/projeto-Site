# (O CONTROLE CENTRAL)

import streamlit as st   # aqui eu importo o streamlit e dou o apelido st, ele é usado para criar a interface web (interface do usuário)
from pathlib import Path # aqui eu importo Path, que serve para trabalhar com caminhos de arquivos e verificar se eles existem
import crud_db           # aqui eu importo o módulo crud_db, que é responsável pelo banco de dados


REQUIRED = [  # aqui eu crio a variável REQUIRED e defino (=) uma lista com os arquivos obrigatórios do sistema
    "home.py",  # aqui eu coloco o arquivo da página inicial
    "crud_db.py",  # aqui eu coloco o arquivo do banco de dados
    "pages/Clientes.py",  # aqui eu coloco o arquivo da página de clientes
    "pages/Produtos.py",  # aqui eu coloco o arquivo da página de produtos
    "pages/Vendas.py"  # aqui eu coloco o arquivo da página de vendas
]


def check():  # aqui eu defino a função check, que serve para verificar se os arquivos existem
    faltando = [f for f in REQUIRED if not Path(f).exists()]
 # aqui eu crio a variável faltando e defino (=) uma lista com os arquivos que NÃO existem no sistema

    if faltando:  # aqui eu verifico se existe algum arquivo faltando
        st.error(f"Arquivos faltando: {faltando}")  # aqui eu mostro uma mensagem de erro na tela com os arquivos que estão faltando

        st.stop()  # aqui eu paro o sistema para evitar erro maior


check()  # aqui eu executo a função check assim que o sistema inicia


crud_db.inicializar_db()  
# aqui eu chamo a função inicializar_db do módulo crud_db para garantir que o banco e as tabelas sejam criados


st.set_page_config(page_title="Controle Comercial", layout="wide")  
# aqui eu configuro a página do sistema
# page_title = define (=) o título da aba do navegador como "Controle Comercial"
# layout = define (=) o tipo de layout como "wide" (tela larga estilo painel)


st.title("📊 Controle Comercial")  
# aqui eu mostro o título principal da página na interface


st.image("logo.jpg", width=500)  
# aqui eu mostro uma imagem chamada "logo.jpg"
# width = define (=) a largura da imagem como 500 pixels


st.markdown("""
Use o menu lateral para navegar entre as páginas.
""")  
# aqui eu mostro um texto simples orientando o usuário a usar o menu lateral


st.markdown("""
<style>

</style>
""", unsafe_allow_html=True)  
# aqui eu uso markdown para inserir código HTML/CSS
# unsafe_allow_html = True → aqui eu defino (=) que o Streamlit pode aceitar código HTML (customização visual)


st.markdown("""
<style>
""")