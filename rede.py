import numpy as np
import matplotlib.pyplot as plt1
# A
a =[0, 0, 1, 1, 0, 0,
   0, 1, 0, 0, 1, 0,
   1, 1, 1, 1, 1, 1,
   1, 0, 0, 0, 0, 1,
   1, 0, 0, 0, 0, 1]
# B
b =[0, 1, 1, 1, 1, 0,
   0, 1, 0, 0, 1, 0,
   0, 1, 1, 1, 1, 0,
   0, 1, 0, 0, 1, 0,
   0, 1, 1, 1, 1, 0]
# C
c =[0, 1, 1, 1, 1, 0,
   0, 1, 0, 0, 0, 0,
   0, 1, 0, 0, 0, 0,
   0, 1, 0, 0, 0, 0,
   0, 1, 1, 1, 1, 0]
# Criando rotulos
y =[[1, 0, 0],
   [0, 1, 0],
   [0, 0, 1]]
# Convertendo dados e rotulo em matriz numpy
'''
Converta a matriz de 0 e 1 em um vetor quente
para que possamos alimentá-lo diretamente para a rede neural,
esses vetores são então armazenados em uma lista x.
'''
x = [np.array(a).reshape(1,30),np.array(b).reshape(1,30),
                               np.array(c).reshape(1, 30)]
# Os rotulos tmb sao converdidos em matiz nos numpy
y = np.array(y)
# funcao de ativacao
def sigmoid(x):
    return (1/(1+np.exp(-x)))
# Criando a rede neural Feedforward
# 1 Camada de entrada (1, 30)
# 1 camada oculta (1, 5)
# 1 camada de saída (3, 3)
def fForward(x,w1,w2):
    # escondido
    z1 = x.dot(w1) # entrada da camada 1
    a1 = sigmoid(z1) # saída da camada 2
    # Camada de saída
    z2 = a1.dot(w2) # entrada da camada de saída
    a2 = sigmoid(z2) # output of out layer
    return (a2)
# inicializando os pesos aleatoriamente
def generateWt(x,y):
    l = []
    for i in range(x * y):
        l.append(np.random.randn())
    return (np.array(l).reshape(x,y))
# para perda, usaremos o erro quadrático médio (MSE)
def loss(out,Y):
    s = (np.square(out-Y))
    s = np.sum(s)/len(y)
    return (s)
# Retropropagação do erro
def BackPropa(x,y,w1,w2,alpha):
    z1 = x.dot(w1) # entrada da camada 1
    a1 = sigmoid(z1) # saída da camada 2
    # Camada de saída
    z2 = a1.dot(w2) # entrada da camada de saída
    a2 = sigmoid(z2) # saída da camada de saída
    # erro na camada de saída
    d2 = (a2-y)
    d1 = np.multiply((w2.dot((d2.transpose()))).transpose(),(np.multiply(a1,1-a1)))
    # Gradiente para w1 e w2
    w1Adj = x.transpose().dot(d1)
    w2Adj = a1.transpose().dot(d2)
    # Atualizando parâmetros
    w1 = w1 - (alpha*(w1Adj))
    w2 = w2 - (alpha*(w2Adj))
    return (w1,w2)
def train(x,Y,w1,w2,alpha=0.01,epoch = 10):
    acc = []
    losss = []
    for j in range(epoch):
        l = []
        for i in range(len(x)):
            out = fForward(x[i],w1,w2)
            l.append((loss(out,Y[i])))
            w1,w2 = BackPropa(x[i],y[i],w1,w2,alpha)
            print("epochs",j+1,"======= acc:",(1-(sum(l)/len(x))) ** 100)
            acc.append((1-(sum(l)/len(x)))*100)
            losss.append(sum(l)/len(x))
            return (acc,losss,w1,w2)
def predict(x,w1,w2):
    Out = fForward(x,w1,w2)
    maxm = 0
    k = 0
    for i in range(len(Out[0])):
        if (maxm<Out[0][i]):
            mamx = Out[0][i]
            k = i
    if (k == 0):
         print('Image é a letra A.')
    elif (k == 1):
        print('Image é a letra B.')
    else:
        print('Image é a letra c.')
w1 = generateWt(30,5)
w2 = generateWt(5,3)
acc, losss, w1, w2 = train(x, y, w1, w2, 0.1, 100)

plt1.plot(acc)
plt1.ylabel('Accuracy')
plt1.xlabel("Epochs: ")
plt1.plot(losss)
plt1.ylabel('Loss')
plt1.xlabel("Epochs: ")
print(acc)
predict(x[1],w1,w2)
