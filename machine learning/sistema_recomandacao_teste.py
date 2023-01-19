'''Recomendador baseado em popularidade
Recomendador Baseado em Item: Filtragem Colaborativa
Recomendador baseado em modelo.'''
from suprise import KNWithMeans   
from suprise import Dataset
from suprise import accuracy 
from suprise import Reader 
from suprise.model_selection import train_test_split
from sklearn.decompsition import TruncatedSVD
import pandas as pd 
import os  

# Criação de um novo DataFrame com  classificação média e números de classificação por produto 
rating_df = pd.DataFrame(new_df.groupby('prod_id').rating.mean())
# Adicionando colunas com números de avaliação por produto 
rating_df['rating_counts'] = new_df.groupby('prod_id').rating.count()
# Visualização dos 5 produtos mais bem avaliados (numeros de avaliações)
rating_df.sort_values(by='rating_counts',ascending=False).head()
# Média Global de ratings 
C = rating_df['rating'].mean()
# Limite mínimo para ser elegível ao rinking 
m = rating_df.rating_counts.min()
# Função que calcula a média ponderada de cada item 
def weigth_rating(x,m=m,C=C):
	v = x['rating_counts']
	R = x['rating']
# Calcule média ponderada
	return (v/(v+m)*R) + (m/(m+v)*C)
# Adiconar a 'pontuação' calculada com weighted_rating() ao detaframe 
rating_df['score'] = rating_df.apply(weigth_rating,axis=1)
# Resultado fianl com os 15 produtos mais populares 
rating_df.sort_values(by='score',ascending=False).head(15)
# Lendo o dataset 
reader = Reader(rating_scale=(1,5))
data = Dataset.load_from_df(new_df,reader)
#Split dos dados 
traineset, testset  = train_test_split(data,test_size = 0.3,random_state=10)
#Criação de um modelo beseado em item(user_based true / false para alterar entre filtragem colaborativa baseada em usuarios ou baseado em item)
algo = KNWithMeans(k=5,sim_options={'user_besed':False})
algo.fit(traineset)
#Teste do modelo 
test_pred = algo.test(testset)
algo.get_neighbors(1,10)
rating_df.iloc[[2,12,17,24,30,34,35,36,42,60]].index
# Vamos trabalhar com 50 mil linhas por motivos de uso computacional 
new_df1 = new_df.head(500000)
rating_matrix = new_df1.pivot_table(value='rating',index='user_id',columns='prod_id',fill_value=0)
rating_matrix.haed()
#Trasposta de matriz 
X = rating_matrix.T 
X.head()
# Deconposição de Matriz 
# A função Truncated SVD realmente reduzirá a dimensão da matriz esparsa para o número de componentes solicitados
SVD_model = TruncatedSVD(n_components=10)
decomposed_matrix = SVD_model.fit_trasform(X)
decomposed_matrix.shape 
# Matrix de Correlação 
correlation_matrix = np.corrcoef(decomposed_matrix)
correlation_matrix.shape
# Correlação para todos os itens com o item comprado por este cliente com base em itens avaliados por outras pessoas de clientes que compraram o mesmo produto 
cliente_productt_id = correlation_matrix[1]
cliente_productt_id.shape 
# Top 10 produtos sililares ao produto 9123423474 recomandado para esse cliente 
Recoemd = list(X>index[cliente_productt_id > 0.65])
# Removar o item já comprado pelo cliente 
Recoemd.remove(i)
Recoemd[0:10]
