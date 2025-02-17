import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Carregar o DataFrame com delimitador ;
df = pd.read_csv('./csv/MICRODADOS_FILT_ENEM_2018.csv', sep=';')

# Filtrar as linhas onde NU_NOTA_REDACAO é diferente de 0
df_filtered = df[df['NU_NOTA_REDACAO'] != 0]

# Somar as notas de cada linha e calcular a média das 5 áreas
df_filtered['TOTAL_NOTAS'] = (df_filtered[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].sum(axis=1) / 5)

# Calcular a média e o desvio padrão
media_total = df_filtered['TOTAL_NOTAS'].mean()
desvio_padrao = df_filtered['TOTAL_NOTAS'].std()

# Criar um range de valores para a curva normal
x = np.linspace(df_filtered['TOTAL_NOTAS'].min(), df_filtered['TOTAL_NOTAS'].max(), 100)
y = norm.pdf(x, media_total, desvio_padrao)

# Criar o gráfico
plt.figure(figsize=(10, 5))

# Plotar histograma das notas
sns.histplot(df_filtered['TOTAL_NOTAS'], bins=50, kde=True, color='skyblue', stat='density', label='Dados Reais')

# Plotar a curva de distribuição normal teórica
plt.plot(x, y, 'r', label='Distribuição Normal')

# Configurações do gráfico
plt.axvline(media_total, color='green', linestyle='dashed', label=f'Média: {media_total:.2f}')
plt.axvline(media_total + desvio_padrao, color='purple', linestyle='dashed', label=f'Média + 1σ')
plt.axvline(media_total - desvio_padrao, color='purple', linestyle='dashed', label=f'Média - 1σ')

plt.title('Distribuição Normal das Notas do ENEM')
plt.xlabel('Nota Média')
plt.ylabel('Densidade')
plt.legend()
plt.grid()

# Exibir o gráfico
plt.show()
