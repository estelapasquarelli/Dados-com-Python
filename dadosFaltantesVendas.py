# Tratamento de Dados Faltantes em um DataFrame de Vendas
import pandas as pd
import numpy as np

#criação do DataFrame
df_vendas = pd.DataFrame ({
    "produto": ["Teclado", "Mouse", "Monitor", "Headphone", "Notebook"],
    "preço": [200, np.nan, 2000, 300, 4500],
    "quantidade":[ 50, 100, np.nan, 80, 20],
    "ano": [2023, 2024, 2023, 2025, np.nan]
})

# Exibição do DataFrame original
print(df_vendas.isnull().sum())

# Preenchimento de valores ausentes
df_vendas["mediana_preço"] = df_vendas["preço"].fillna(df_vendas["preço"]).median().round(2)
df_vendas["media_quantidade"] = df_vendas["quantidade"].fillna(df_vendas["quantidade"]).mean().round(2)

# Exclusão de linhas com valores ausentes na coluna 'ano'
df_limpo = df_vendas.dropna(subset=["ano"]) # 
df_limpo = df_limpo.assign(ano=df_limpo["ano"].astype(int)) # Converte "ano" para int 

print(df_limpo)

