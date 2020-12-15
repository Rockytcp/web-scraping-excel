from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.cip-bancos.org.br/DadosEstrategicos/EvolPagsMesTot.html"

id_tabela = "oReportCell"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tabela = soup.find('table', atttrs={'id': id_tabela})

df = pd.read_html(str(tabela))
