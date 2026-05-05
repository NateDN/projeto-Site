import streamlit as st  # Importa o Streamlit (framework para interface web)
import pandas as pd     # Importa o Pandas (manipulação de dados em tabelas)
import crud_db          # Importa seu módulo de banco de dados (CRUD)

st.set_page_config(layout="wide")  
# aqui eu configuro a página
# layout = define (=) o tipo de layout como "wide", ou seja, tela larga estilo painel (dashboard)


# 🎨 CSS PRO (cards + animação)
st.markdown("""
<style>

.card {                                       
    background-color: #0F172A;               
    padding: 20px;                           
    border-radius: 12px;                      
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3); 
    transition: all 0.3s ease-in-out;        
    text-align: center;                    
}
            
/* 16: aqui eu crio a classe .card (estilo dos cartões do sistema) */
/* 17: background-color = define (=) a cor de fundo do card */
/* 18: padding = define (=) o espaçamento interno */
/* 19: border-radius = define (=) o arredondamento das bordas */
/* 20: box-shadow = define (=) a sombra do card */
/* 21: transition = define (=) a animação suave */
/* 22: text-align = define (=) o alinhamento do texto (centralizado) */

.card:hover {                                 
    transform: scale(1.05);                   
    box-shadow: 0px 6px 25px rgba(0,0,0,0.5);
}

/* 33: aqui eu defino o efeito quando o mouse passa por cima do card */
/* 34:transform = define (=) que o card aumenta de tamanho */
/* 35: box-shadow = define (=) uma sombra mais forte */

.card-title {        
    font-size: 14px;
    color: #94A3B8;
}

/* 42: aqui eu estilizo o título do card */
/* 43: font-size = define (=) o tamanho da fonte */
/* 44: color = define (=) a cor do texto */

.card-value {        
    font-size: 28px;
    font-weight: bold;
    color: #22C55E;
}
            
/* 51: aqui eu estilizo o valor principal do card */
/* 52: font-size = define (=) o tamanho da fonte */
/* 53: font-weight = define (=) o peso da fonte (negrito) */
/* 54: color = define (=) a cor do valor */

.divider {          
    margin: 30px 0;
}
            
/* 62: aqui eu crio um espaçamento entre seções */
/* 63: margin = define (=) o espaço externo */

</style>
""", unsafe_allow_html=True)  # aqui eu fecho o CSS
# unsafe_allow_html = define (=) que o streamlit pode aceitar HTML/CSS personalizado

st.title("📊 Dashboard Comercial")# aqui eu mostro o título principal da página

# 🔹 Dados (busca do banco)
vendas = crud_db.selecionar("vendas")       # aqui eu crio a variável vendas e defino (=) que ela recebe os dados da tabela vendas
clientes = crud_db.selecionar("clientes")   # aqui eu crio a variável clientes e defino (=) os dados da tabela clientes
produtos = crud_db.selecionar("produtos")   # aqui eu crio a variável produtos e defino (=) os dados da tabela produtos

# Converte dados em DataFrames
df_vendas = pd.DataFrame(vendas, columns=["ID", "cliente_id", "produto_id", "Qtd", "Total", "Data"])
# aqui eu crio a variável df_vendas e defino (=) uma tabela organizada com os dados de vendas
df_clientes = pd.DataFrame(clientes, columns=["ID", "Nome", "Telefone", "Email"])   # aqui eu crio a tabela de clientes
df_produtos = pd.DataFrame(produtos, columns=["ID", "Produto", "Preco", "Estoque"]) # aqui eu crio a tabela de produtos

# Verifica se há vendas
if df_vendas.empty:
    st.warning("⚠️ Ainda não há vendas registradas.")   # aqui eu mostro um aviso
    st.stop()    # aqui eu paro o sistema para evitar erro

# 🔹 Tratamento de dados
df_vendas["Data"] = pd.to_datetime(df_vendas["Data"]) # aqui eu pego a coluna Data e defino (=) que ela será convertida para formato de data

# 🔗 Merge (junção de tabelas)
df = df_vendas.merge(df_clientes, left_on="cliente_id", right_on="ID") # aqui eu crio a variável df e defino (=) a junção das vendas com clientes
df = df.merge(df_produtos, left_on="produto_id", right_on="ID")        # aqui eu atualizo df e defino (=) a junção com produtos

# 🔹 KPIs (indicadores)
faturamento = df["Total"].sum()            # aqui eu crio a variável faturamento e defino (=) a soma de todas as vendas
total_vendas = len(df)                     # aqui eu crio a variável total_vendas e defino (=) a quantidade de vendas
produtos_vendidos = df["Qtd"].sum()        # aqui eu crio a variável produtos_vendidos e defino (=) a soma das quantidades
ticket_medio = faturamento / total_vendas  # aqui eu crio a variável ticket_medio e defino (=) o valor médio por venda

# 🎯 CARDS (indicadores visuais)
st.subheader("📌 Indicadores")  # aqui eu mostro um subtítulo

col1, col2, col3, col4 = st.columns(4) # aqui eu crio 4 colunas lado a lado

with col1: # aqui eu uso a coluna 1
    st.markdown(f"""
    <div class="card"> 
        <div class="card-title">Faturamento</div>
        <div class="card-value">R$ {faturamento:.2f}</div>
    </div>
    """, unsafe_allow_html=True)
# 111: aqui eu crio um card visual
# 112: faturamento:.2f = define (=) que o valor terá 2 casas decimais
# (os outros cards seguem exatamente a mesma lógica)  

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">Vendas</div>
        <div class="card-value">{total_vendas}</div>
    </div>
    """, unsafe_allow_html=True)  # Card total de vendas

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">Itens Vendidos</div>
        <div class="card-value">{produtos_vendidos}</div>
    </div>
    """, unsafe_allow_html=True)  # Card itens vendidos

with col4:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">Ticket Médio</div>
        <div class="card-value">R$ {ticket_medio:.2f}</div>
    </div>
    """, unsafe_allow_html=True)  # Card ticket médio

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)  # Linha separadora

# 📊 GRÁFICOS (layout profissional)
col_g1, col_g2 = st.columns(2)  # aqui eu crio duas colunas para gráficos

with col_g1:
    st.subheader("📈 Vendas no Tempo")                           # Título do gráfico
    vendas_tempo = df.groupby(df["Data"].dt.date)["Total"].sum() # aqui eu crio a variável vendas_tempo e defino (=) o agrupamento das vendas por data
    st.line_chart(vendas_tempo)                                  # aqui eu mostro o gráfico de linha

with col_g2:
    st.subheader("📊 Receita por Produto")
    produtos_venda = df.groupby("Produto")["Total"].sum().sort_values(ascending=False) # aqui eu crio a variável produtos_venda e defino (=) a soma por produto ordenada
    st.bar_chart(produtos_venda) # aqui eu mostro gráfico de barras      
                                                    

col_g3, col_g4 = st.columns(2)  # Nova linha de gráficos

with col_g3:
    st.subheader("🧑‍💼 Top Clientes")
    clientes_top = df.groupby("Nome")["Total"].sum().sort_values(ascending=False)  # aqui eu crio ranking de clientes
    st.bar_chart(clientes_top)                                                     # gráfico de barras

with col_g4:
    st.subheader("🔥 Volume de Itens")
    qtd_produto = df.groupby("Produto")["Qtd"].sum() # aqui eu crio a variável qtd_produto e defino (=) quantidade vendida por produto
    st.area_chart(qtd_produto)                       # aqui eu mostro gráfico de área

#______________________________________________________
#Esse código é um dashboard empresarial completo, com:

#🔹 Backend
#Integração com banco SQLite
#Uso de DataFrames para análise
#________________________________________________
#🔹 Processamento
#JOIN entre tabelas (clientes + produtos + vendas)
#Cálculo de KPIs
#________________________________________________
#🔹 Frontend (UI/UX)
#Cards animados
#Layout em colunas
#Gráficos interativos
#_________________________________________________