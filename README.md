
<h1 align="center">📌  Projeto de Probabilidade e Estatística - Análise dos Microdados do Enem 2018 </h1>

<p align="center">
  <img src="http://img.shields.io/static/v1?label=License&message=MIT%20License&color=A20606&style=for-the-badge"/>
  <img src="http://img.shields.io/static/v1?label=Python&message=3.12.9&color=A20606&style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/static/v1?label=Streamlit&message=GUI&color=A20606&style=for-the-badge&logo=Streamlit"/>
</p>

<p align="center">
  <img src="http://img.shields.io/static/v1?label=Desenvolvido%20por&message=Kalvin%20Klein, Jose%20Bezerra, Pedro Arcoverde e Ronyldo Oliveira&color=A20606&style=for-the-badge"/>
  <img src="http://img.shields.io/static/v1?label=Disciplina&message=Probabilidade%20e%20Estatistica&color=A20606&style=for-the-badge"/>
</p>

---
<p align="center">
Este projeto analisa os microdados do ENEM 2018 e gera visualizações e análises estatísticas utilizando Python. Este projeto foi desenvolvido para a matéria de Probabilidade e Estatística do IFRN.
</p>

---

## Estrutura do Projeto

### Arquivos e Diretórios

- `csv/`: Contém os arquivos de dados utilizados no projeto.
- `Dicionário_Microdados_Enem_2018.ods`: [Dicionário de dados do ENEM 2018](https://download.inep.gov.br/microdados/microdados_enem_2018.zip).
- `MICRODADOS_FILT_ENEM_2018.csv`: [Microdados filtrados do ENEM 2018](https://download.inep.gov.br/microdados/microdados_enem_2018.zip).

- `dashboards.py`: Script para criar dashboards interativos utilizando Streamlit e Plotly.
  - Carrega os dados do ENEM 2018.
  - Calcula a média geral das notas.
  - Mapeia categorias de faixa etária.

- `distribuicao_normal.py`: Script para análise de distribuição normal das notas do ENEM.
  - Carrega os dados do ENEM 2018.
  - Filtra as linhas onde a nota de redação é diferente de 0.
  - Calcula a média e o desvio padrão das notas.
  - Plota um histograma e a curva de distribuição normal.

---

## Requisitos

- Python 3.12.9
- Bibliotecas:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scipy
  - streamlit
  - plotly
  - requests

---

## Como Executar

1. Clone o repositório:
    ```sh
    git clone https://github.com/kakanetwork/Projeto_PE
    cd Projeto_PE
2. Instale as dependências:
    ```sh
    pip install -r requirements.txt
3. Execute o script de dashboards:
    ```sh
    streamlit run dashboards.py
4. Execute o script de distribuição normal:
    ```sh
    python distribuicao_normal.py
**Licença e Autores**

---

## 📝 Licença

Esse projeto está licenciado sob a licença do MIT LICENSE - veja o arquivo de [LICENÇA](LICENSE) para mais detalhes.

---
## 👀 Autores

Para mais informações sobre o projeto presente neste repositório ou para sugerir alterações e correções, entre em contato pelo Github ou Email.<br>

<div>
    <a href="https://github.com/kakanetwork"><img src="https://img.shields.io/badge/-GitHub Kalvin-4d080e?style=for-the-badge&color=A20606&logo=github&logoColor=ffffff"></a>
    <a href="https://github.com/JoJoseB"><img src="https://img.shields.io/badge/-GitHub José-4d080e?style=for-the-badge&color=A20606&logo=github&logoColor=ffffff"></a>
    <a href="https://github.com/ArcoverdePedro"><img src="https://img.shields.io/badge/-GitHub Pedro-4d080e?style=for-the-badge&color=A20606&logo=github&logoColor=ffffff"></a>
    <a href="https://github.com/Ronynetwork"><img src="https://img.shields.io/badge/-GitHub Ronyldo-4d080e?style=for-the-badge&color=A20606&logo=github&logoColor=ffffff"></a>
</div> 
