                                              Projeto em andamento 
'''O objetivo do projeto de Insights
é recomendar soluções para o negócio
através de Insights gerados por uma ótima Análise Exploratória de Dados.'''
from matplotlib import *
import pandas as pd
import matplotlib as plt 
import zipfile 
#Abrindo o arquivo .zip 
dados = pd.read_csv('archive.zip',compression='zip')
dados.rename(columns={'price':'Preço','bedrooms':'Quartos','bathrooms':'Banheiros','yr_renovated':'Ano renovado'},inplace=True)
n = 10
casas_mais_caras = dados.nlargest(n,'Preço')
# Análisar o pq as casa são caras e identificar um padrão
# Preço 
def casas_preco():
        # Sempre que for chamar a váriavel lambrar de chamar a função tbm 
        global casa_barata
        global casa_media
        global casa_cara 
        preco = dados['Preço']
        casa_barata = preco.min()
        casa_media = preco.mean()
        casa_cara = preco.max()
        # Pagando as 5 casas mais caras 
dados_decresente = dados.sort_values(['Preço'],ascending=False)
'''print(dados_decresente.head(100))
print(dados.max())'''
# Pegar as informações da casas limpo sem nenhum dado 
def infomacao():
        latitude = dados_decresente['lat']
        longitude = dados_decresente['long']
        numeros_quartos = dados_decresente['Quartos']
        banheiros = dados_decresente['Banheiros']
        ano_contruido = dados_decresente['yr_built']
        renovado = dados_decresente['Ano renovado']
        for i in dados_decresente:
                informacao = i 
                #print(informacao)
        return casas_mais_caras
# Agora é precisso pagar as 10 casas mais caras e ver o que elas tem em comum 
def reconhecimento_padrao():
        pass
if __name__ == "__main__":
        casas_preco()
        infomacao()
        comparacao()
                                               Projeto em andamento 
