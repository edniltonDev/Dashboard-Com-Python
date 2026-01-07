# 📊 Dashboard de Faturamento das Lojas

Este é um projeto de dashboard interativo desenvolvido em **Python** utilizando a biblioteca **Dash**. O objetivo é visualizar a quantidade de produtos vendidos por diferentes lojas através de uma interface web simples e funcional.

![Preview do Dashboard]<img width="1423" height="625" alt="image" src="https://github.com/user-attachments/assets/a8ea0bbb-21c3-4ba2-8032-a62a1d8cfab4" />


## 🚀 Funcionalidades
* **Visualização Dinâmica**: Gráfico de barras agrupado por produto e loja.
* **Filtros Interativos**: Filtre os dados por uma loja específica ou visualize o faturamento global ("Todas as Lojas") através de um menu suspenso (dropdown).
* **Processamento de Dados**: Integração direta com planilhas Excel para leitura de dados.

## 🛠️ Tecnologias Utilizadas
* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/) (Manipulação de dados)
* [Dash](https://dash.plotly.com/) (Framework web)
* [Plotly Express](https://plotly.com/python/plotly-express/) (Gráficos interativos)
* [Openpyxl](https://openpyxl.readthedocs.io/en/stable/) (Leitura de arquivos Excel)

## 📋 Pré-requisitos
Antes de começar, você precisará ter o Python instalado em sua máquina. Recomenda-se o uso de um ambiente virtual.

### Estrutura do Excel (`vendas.xlsx`)
Para o correto funcionamento, o arquivo Excel deve conter as seguintes colunas:
* `Produto`: Nome do item vendido.
* `Quantidade`: Volume de vendas.
* `ID Loja`: Identificação da unidade de venda.

## 🔧 Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio

2. Crie e ative seu ambiente virtual:
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

3.Instale as dependências:
pip install pandas dash plotly openpyxl

4. Execute a aplicação:
python app.py

5. Acesse no navegador: Abra o link http://127.0.0.1:8050/

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido por [Ednilton]
  
