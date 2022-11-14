                                              Projeto em andamento 
'''O objetivo do projeto de Insights
é recomendar soluções para o negócio
através de Insights gerados por uma ótima Análise Exploratória de Dados.'''
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sn
import numpy, scipy,statsmodels,zipfile

dados = pd.read_csv('archive.zip',compression='zip')
n = 10
dados_altos = dados.nlargest(n,'price')
dados_baixos = dados.sort_values(['price']).head(n)
todos_dados = dados_baixos,dados_altos
for k in range(n):
	localizacao_alta = dados_altos[["long","lat"]]
	planta_alto = dados_altos[["bedrooms","bathrooms"]]
	estrutura_alto = dados_altos[["sqft_living","sqft_lot","sqft_basement","sqft_above"]] 
	acabamento_alto = dados_altos[["yr_built","yr_renovated"]]
	areas_de_lazer_alto = dados_altos[["view","waterfront"]]
	seguranca_alto = dados_altos[["condition"]]
	avaliacao_alto = dados_altos[["grade"]]		
	infomacao_alta = localizacao_alta,planta_alto,estrutura_alto,acabamento_alto,areas_de_lazer_alto,seguranca_alto,avaliacao_alto
preco = dados_altos['price']
# Calculando a correlação do df 
p = dados_altos.corr()
print(p)
# COdigo para ver se o correlacao e positiva negativa ou inesistente 
if ps == 0.9 and 1 or -0.9 and-1:
	print('Correlação muito forte')
elif p == 0.7 and 0.9 or -0.7 and -0.9:
	print('Correlação forte')
elif p == 0.5 and 0.7 or -0.5 and -0.7:
	print('Correlação moderada')
elif p == 0.3 and 0.5 or -0.3 and -0.5:
	print('Correlação fraca')
else:
	print('Não a Correlação')
# nome das colunas
for c in dados:
	pass 

                                               Projeto em andamento 
