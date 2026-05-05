import streamlit as st  # Importa o Streamlit (interface web)

st.title("📌 Sobre o Sistema")

st.markdown("""
### 🧠 Controle Comercial - Sistema de Gestão

Este sistema foi desenvolvido para realizar o gerenciamento completo de um pequeno negócio, utilizando tecnologias modernas com Python.

---           

### 🚀 Funcionalidades

- 👤 Cadastro e gerenciamento de clientes  
- 📦 Cadastro de produtos com controle de estoque  
- 💰 Registro de vendas com cálculo automático  
- 📊 Dashboard com indicadores e gráficos em tempo real  

---

### 🧩 Estrutura do Sistema

O sistema é dividido em módulos:

- **Home** → Página inicial com navegação  
- **Clientes** → CRUD completo de clientes  
- **Produtos** → Cadastro e controle de estoque  
- **Vendas** → Registro de vendas com integração entre tabelas  
- **Dashboard** → Visualização de métricas e desempenho  

---

### 🛠️ Tecnologias Utilizadas

- 🐍 Python 3.10.  
- 🎨 Streamlit (interface web)
- 🗄️ SQLite (banco de dados local)  
- 📊 Pandas (análise de dados)

---

### 📈 Recursos Técnicos

- Arquitetura modular  
- CRUD genérico reutilizável  
- Relacionamento entre tabelas (clientes, produtos, vendas)  
- Cálculo de indicadores (KPIs)  
- Interface customizada com CSS  
- Registro de logs do sistema  

---

### 🎯 Objetivo

Fornecer uma solução simples, rápida e eficiente para controle comercial, permitindo melhor organização, análise de dados e tomada de decisão.

---

### 💡 Possíveis Evoluções

- 🔐 Sistema de login e autenticação  
- ☁️ Deploy em nuvem  
- 📄 Exportação de relatórios (PDF/Excel)  
- 📉 Gráficos avançados e filtros  
- 🏢 Suporte a múltiplas empresas  

---

### 👨‍💻 Desenvolvido com foco em aprendizado e aplicação prática de desenvolvimento de sistemas reais.
            
Autor: Daniel Pereira da Silva 
""")