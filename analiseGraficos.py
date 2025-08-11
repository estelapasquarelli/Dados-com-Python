import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.info())
print(df.describe(include="all"))

mapeamentos = {
    "experience_level": {"SE": "Senior", "MI": "Pleno", "EN": "Junior", "EX": "Executivo"},
    "employment_type": {"FT": "Tempo Integral", "PT": "Tempo Parcial", "FL": "Freelancer", "CT": "Contrato"},
    "company_size": {"S": "Pequena", "M": "Media", "L": "Grande"},
    "remote_ratio": {0: "Presencial", 50: "Híbrido", 100: "Remoto"}
}

df = df.replace(mapeamentos)

print(df.head())
print(df.isnull().sum())

df_limpo = df.dropna()
df_limpo = df_limpo.assign(work_year = df_limpo["work_year"].astype("int64"))
print(df_limpo.info())

import matplotlib.pyplot as plt
import seaborn as sns

(df_limpo["experience_level"].value_counts().plot(kind="bar", title="Nível de Experiência"))
plt.show()

ordem = df_limpo.groupby("experience_level")["salary_in_usd"].mean().sort_values(ascending=False).index
display(ordem)

plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x="experience_level", y="salary_in_usd", order=ordem)
plt.title("Salário médio por nível de senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salário médio anual (USD)")
plt.show()

plt.figure(figsize=(8,4))
sns.histplot(df_limpo["salary_in_usd"], bins=50, kde=True)
plt.title("Distribuição dos salário anuis")
plt.xlabel("Salário (USD)")
plt.ylabel("Frequência")
plt.show()

plt.figure(figsize=(8,4))
sns.boxplot(x=df_limpo["salary_in_usd"])
plt.title("Boxplot salário")
plt.xlabel("Salário (USD)")
plt.show()

ordem_senioridade = ["Junior", "Pleno", "Senior", "Executivo"]
plt.figure(figsize=(8,4))
sns.boxplot(x="experience_level", y="salary_in_usd", data=df_limpo, order=ordem_senioridade, palette="Set2", hue="experience_level")
plt.title("Distribuição salarial por nível de experiência")
plt.ylabel("Salário (USD)")
plt.xlabel("Nível de experiência")
plt.show()

import plotly.express as px
fig = px.bar(
    df_limpo.groupby("experience_level")["salary_in_usd"].mean().loc[ordem].reset_index(),
    x="experience_level",
    y="salary_in_usd",
    title="Salário médio por nível de senioridade",
    labels={"experience_level": "Senioridade", "salary_in_usd": "Salário médio anual (USD)"}
)
fig.show()


remoto_contagem = df_limpo["remote_ratio"].value_counts().reset_index()
remoto_contagem.columns = ["tipo_trabalho", "quantidade"]

fig = px.pie(remoto_contagem,
             names="tipo_trabalho",
             values="quantidade",
             title="Porporção dos tipo de trabalho",
             hole=0.5
             )

fig.update_traces(textinfo="percent+label")
fig.show()