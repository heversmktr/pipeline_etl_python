import streamlit as st
import pandas as pd
import sqlite3



# Conectar ao banco de dados SQlite
conn = sqlite3.connect('../data/quotes.db')

# Carregar os dados da tabela 'mercadolivre_items' em um DataFrame pandas
df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)