import pandas as pd

#criar uma lista de dicionário com dados fictícios 
dados = [
    {"work_year": 2025, "experience_level": "Sênior", "employment_type": "Integral", "job_title": "Assistente de Sala", "salary": 5000, "salary_currency": "Real", "residence": "Brasil", "remote_rate": 0, "company_size": "Pequena"},
    {"work_year": 2025, "experience_level": "Junior", "employment_type": "Parcial", "job_title": "Monitor", "salary": 2000, "salary_currency": "Real", "residence": "Brasil", "remote_rate": 0, "company_size": "Média"},
    {"work_year": 2025, "experience_level": "Pleno", "employment_type": "Integral", "job_title": "Professor", "salary": 7000, "salary_currency": "Real", "residence": "Brasil", "remote_rate": 0, "company_size": "Pequena"},
    {"work_year": 2025, "experience_level": "Junior", "employment_type": "Integral", "job_title": "Assistente de Sala", "salary": 2000, "salary_currency": "Dolar", "residence": "USA", "remote_rate": 0, "company_size": "Média"},
    {"work_year": 2025, "experience_level": "Sênior", "employment_type": "Freelance", "job_title": "Coordenador", "salary": 10000, "salary_currency": "Dolar", "residence": "Argentina", "remote_rate": 100, "company_size": "Grande"},
    {"work_year": 2025, "experience_level": "Junior", "employment_type": "Integral", "job_title": "Monitor", "salary": 1500, "salary_currency": "Real", "residence": "Brasil", "remote_rate": 50, "company_size": "Pequena"},
    {"work_year": 2025, "experience_level": "Pleno", "employment_type": "Parcial", "job_title": "Professor", "salary": 5000, "salary_currency": "Real", "residence": "Chile", "remote_rate": 0, "company_size": "Pequena"},
    {"work_year": 2025, "experience_level": "Executivo", "employment_type": "Integral", "job_title": "Diretor", "salary": 15000, "salary_currency": "Dolar", "residence": "USA", "remote_rate": 50, "company_size": "Pequena"},
    {"work_year": 2025, "experience_level": "Sênior", "employment_type": "Integral", "job_title": "Assistente de Sala", "salary": 4500, "salary_currency": "Real", "residence": "Brasil", "remote_rate": 0, "company_size": "Pequena"},
    {"work_year": 2025, "experience_level": "Junior", "employment_type": "Parcial", "job_title": "Assistente de RH", "salary": 2600, "salary_currency": "Real", "residence": "Chile", "remote_rate": 100, "company_size": "Grande"},
    {"work_year": 2025, "experience_level": "Pleno", "employment_type": "Freelance", "job_title": "Professor", "salary": 6700, "salary_currency": "Euro", "residence": "Italia", "remote_rate": 100, "company_size": "Grande"},
    {"work_year": 2025, "experience_level": "Sênior", "employment_type": "Integral", "job_title": "Professor", "salary": 9000, "salary_currency": "Euro", "residence": "Brasil", "remote_rate": 100, "company_size": "Grande"},
    {"work_year": 2025, "experience_level": "Sênior", "employment_type": "Parcial", "job_title": "Assistente de Sala", "salary": 4000, "salary_currency": "Euro", "residence": "Italia", "remote_rate": 0, "company_size": "Pequena"},
    {"work_year": 2025, "experience_level": "Junior", "employment_type": "Freelance", "job_title": "Enfermeiro", "salary": 3000, "salary_currency": "Real", "residence": "Brasil", "remote_rate": 0, "company_size": "Pequena"},
    {"work_year": 2025, "experience_level": "Pleno", "employment_type": "Integral", "job_title": "Professor", "salary": 7800, "salary_currency": "Real", "residence": "Brasil", "remote_rate": 50, "company_size": "Média"},
    {"work_year": 2025, "experience_level": "Executivo", "employment_type": "Integral", "job_title": "Gerente de RH", "salary": 10000, "salary_currency": "Euro", "residence": "Brasil", "remote_rate": 100, "company_size": "Grande"},
    {"work_year": 2025, "experience_level": "Sênior", "employment_type": "Freelance", "job_title": "Coordenador", "salary": 10500, "salary_currency": "Real", "residence": "Brasil", "remote_rate": 50, "company_size": "Média"},
    {"work_year": 2025, "experience_level": "Junior", "employment_type": "Integral", "job_title": "Monitor", "salary": 3000, "salary_currency": "Real", "residence": "Brasil", "remote_rate": 0, "company_size": "Pequena"},
    {"work_year": 2025, "experience_level": "Pleno", "employment_type": "Integral", "job_title": "Assistente de RH", "salary": 5000, "salary_currency": "Dolar", "residence": "Brasil", "remote_rate": 100, "company_size": "Pequena"},
    {"work_year": 2025, "experience_level": "Junior", "employment_type": "Integral", "job_title": "Assistente de Sala", "salary": 4000, "salary_currency": "Euro", "residence": "Espanha", "remote_rate": 0, "company_size": "Média"},
]

df = pd.DataFrame(dados)

#renomear colunas para português
rename_columns = {
    "work_year": "ano_referência",
    "experience_level": "senioridade",
    "employment_type": "contrato",
    "job_title": "cargo",
    "salary": "salário",
    "salary_currency": "moeda",
    "residence": "país",
    "remote_rate": "modelo_trabalho",
    "company_size": "tamanho_empresa"
}

df = df.rename(columns = rename_columns)

#renomear modelos de trabalho
rename_modelo_trabalho = {
    0: "Presencial",
    50: "Híbrido",
    100: "Remoto"
}

df["modelo_trabalho"] = df["modelo_trabalho"].replace(rename_modelo_trabalho)

#prints para visualização de resultados no terminal

#dimensão do DataFrame (linhas, colunas)
rows, columns = df.shape
print("Linhas: ", rows)
print("Colunas: ", columns)

#informações dos 20 primeiros registros
print(df.head(20))

#informações gerais do DataFrame
print(df.info())

#estatísticas descritivas de salário
print(df["salário"].describe())

#frequência de cada elemento
print(df["senioridade"].value_counts()) 
print(df["contrato"].value_counts()) 
print(df["país"].value_counts()) 
print(df["moeda"].value_counts()) 
print(df["cargo"].value_counts())
print(df["ano_referência"].value_counts())
print(df["salário"].value_counts()) 
print(df["modelo_trabalho"].value_counts()) 