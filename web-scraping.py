from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv


def exportar(url):
    url = url

    id_tabela = "oReportCell"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    tabela = soup.find(attrs={'id': id_tabela})

    df = pd.read_html(str(tabela))[0]
    #print(df)
    pd.DataFrame(tabela)
    df.to_excel ("teste.xlsx")

    

tabela1 = exportar("https://www.cip-bancos.org.br/DadosEstrategicos/EvolPagsMesTot.html")
#tabela2 = exportar("https://www.cip-bancos.org.br/DadosEstrategicos/EvolPags.html")
