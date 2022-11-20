                                              Projeto em andamento 
'''O objetivo do projeto de Insights
é recomendar soluções para o negócio
através de Insights gerados por uma ótima Análise Exploratória de Dados.'''

mport matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns
import numpy, scipy,statsmodels,zipfile

dados = pd.read_csv('archive.zip',compression='zip')
contador = 0 
n = 10 
preco = dados['price'] # media de preco ==  5.400881
dados['id'].nunique() 
casas_mais_baratas = dados.sort_values('price',ascending=False)
casa_mais_cara = dados.nlargest(n,'price')
# informacao das casas mais caras 
tamanho_casa = casa_mais_cara['sqft_living'],casa_mais_cara['sqft_above'],casa_mais_cara['sqft_living15']
tamanho_terreno = casa_mais_cara['sqft_lot'],casa_mais_cara['sqft_lot15']
lazer_casa = casa_mais_cara['waterfront'],casa_mais_cara['view']
localizacao_casa = casa_mais_cara['lat'],casa_mais_cara['long']
seguranca_casa = casa_mais_cara['condition'],casa_mais_cara['yr_renovated']
# media das casas caras 
media_quatos = casa_mais_cara.groupby('price').bedrooms.mean()
media_banhiros = casa_mais_cara.groupby('price').bathrooms.mean()
media_tamanho = casa_mais_cara.groupby('price').sqft_living.mean()
media_lazer = casa_mais_cara.groupby('price').waterfront.mean()
media_localizacao = casa_mais_cara.groupby('price').lat.mean()
media_localizacaolong = casa_mais_cara.groupby('price').long.mean()
media_seguranca = casa_mais_cara.groupby('price').yr_renovated.mean()
media_de_casa_cara = media_seguranca,media_localizacaolong,media_localizacao,media_lazer,media_tamanho,media_quatos,media_banhiros
