                                              Projeto em andamento 
'''O objetivo do projeto de Insights
é recomendar soluções para o negócio
através de Insights gerados por uma ótima Análise Exploratória de Dados.'''

import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns
import numpy as np  
import scipy,statsmodels,zipfile,random

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
#Criar um percptron 
class Percptron:
	def __init__(self,saida,pesos,amostra,epocas=1000):
		self.amostras = amostras
		self.saidas = saidas 
		self.epocas = epocas
		self.primeira_amostra = len(amostras)
		self.segunda_amostra = len(amostras[0])
		self.pesos = pesos
	def sinal(self,u):
		return 1 if u >= 0 else -1 
	def treinar(self):
		for amostra in self.amostras:
			amostra.insert(0,-1)
		for i in range(self.segunda_amostra):
			self.pesos.append(random.random()) # Talvez trocar pela media_casa ou qualquer outra váriavel 
		num_epocas = 0 
		while True:
			error = False
			for i in range(self.primeira_amostra):
				u = 0 
				for j in range(self.segunda_amostra + 1):
					u += self.pesos[j] * self.amostras[i][j]
				y = self.sinal(u)
				if y != self.saidas[i]:
					erro_aux = self.saidas[i] - y 
					for j in range(self.segunda_amostra + 1):
						self.pesos[j] = self.pesos[j] + erro_aux * self.amostras[i][j]
					erro = True 
			num_epocas += 1 
			if num_epocas > self.epocas or not erro:
				break 
	def testar(self,u):
		amostra.insert(0,-1)
		u = 0 
		for i in range(self.segunda_amostra + 1):
			u += self.pesos[i] * amostra[i]
		y = self.sinal(u)
		if y == -1:
			print('-1')
		else:
			print('+1')
amostras = media_de_casa_cara
saidas = [1,-1,-1,1]
rede = Perceptron(amostras=amostras,saidas=saidas,epocas=epocas)
rede.treinar()
