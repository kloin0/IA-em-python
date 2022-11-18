                                              Projeto em andamento 
'''O objetivo do projeto de Insights
é recomendar soluções para o negócio
através de Insights gerados por uma ótima Análise Exploratória de Dados.'''
import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns
import numpy, scipy,statsmodels,zipfile

dados = pd.read_csv('archive.zip',compression='zip')
n = 10 
dados['id'].nunique()
casa_mais_cara = dados.nlargest(n,'price')
tamanho_casa = casa_mais_cara['sqft_living'],casa_mais_cara['sqft_above'],casa_mais_cara['sqft_living15']
tamanho_terreno = casa_mais_cara['sqft_lot'],casa_mais_cara['sqft_lot15']
lazer_casa = casa_mais_cara['waterfront'],casa_mais_cara['view']
localizacao_casa = casa_mais_cara['lat'],casa_mais_cara['long']
seguranca_casa = casa_mais_cara['condition'],casa_mais_cara['yr_renovated']
def media(media_casas_caras):
        media_quatos = casa_mais_cara.groupby('price').bedrooms.mean()
        media_banhiros = casa_mais_cara.groupby('price').bathrooms.mean()
        media_tamanho = casa_mais_cara.groupby('price').tamanho_terreno.mean()  
        media_lazer = casa_mais_cara.groupby('price').lazer_casa.mean()
        media_localizacao = casa_mais_cara.groupby('price').localizacao_casa.mean()
        media_seguranca = casa_mais_cara.groupby('price').seguranca_casa.mean()
        media_casas_caras = media_seguranca,media_localizacao,media_lazer,media_banhiros,media_quatos
~
