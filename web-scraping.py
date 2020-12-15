from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.cip-bancos.org.br/DadosEstrategicos/EvolPagsMesTot.html"

id_tabela = "oReportCell"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tabela = soup.find(atttrs={'id': id_tabela})

df = pd.read_html(str(tabela))

print(df)


#df = pd.DataFrame(tabela, columns = ['Mês', 'D.U', 'Quantidade Média Diária', 'Valor em R$ mil Média Diária', 'Quantidade Consolidado', 'Valor em R$ mil Consolidado'])

#df.to_excel (r'C:\Users\gbp\Desktop\Trabalho\Web Scraping\export_dataframe.xlsx', index = False, header=True)
