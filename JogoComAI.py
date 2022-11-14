from time import sleep
import random
import os
def GetLine(posicao):
	global pa, pb, pc
	posicao *= 2
	# Tabuleiro
	z = '48021476852645360'
	pa = int(z[posicao + 0])
	pb = int(z[posicao + 1])
	pc = int(z[posicao + 2])
	return board[pa] + board[pb] + board[pc]
def pcJoga():
	for x in (2,18):
		for n in range(8):
			if GetLine(n) == x:
				if board[pa] == vazio:
					pos = pa
				elif board[pb] == vazio:
					pos = pb
				else:
					pos = pc
				board[pos] = 1
				print(f'{BLUE} {"Posição Pc: "} {pos+1} {REST}')
				sleep(2)
				return
		while True:
			pos = random.randint(0,8)
			if board[pos] == vazio:
				board[pos] = 1
				break
		print(f'{BLUE} {"Posição Pc:"} {pos+1} {RST}')
		sleep(2)
		return
def UserJoga():
	while True:
		x = input(f'{GREEN} {"Posição User"} {RST}')
		if x in ('q','Q','o'):
			print('Jogo Abortado')
			exit(0)
		try:
			pos = int(x) - 1
			if board[pos] != vazio:
				print('Posição já ocupada')
			else:
				board[pos] = 9
				break
		except:
			pass
def display():
	global empate,micro,user
	os.system('clear')
	mk = []
	for i, v in enumerate(board):
		if v == 0:
			mk.append(f'{YELLOW} {str(i+1)} {RST}')
		elif v == 1:
			mk.append(f'{BLUE} {"O"} {RST}')
		else:
			mk.append(f'{GREEN} {"X"} {RST}')
	print(f'{WHITE} {"Empate = "} {empate} {RST}')
	print(f'{BLUE} {"Micro = "} {micro} {RST}')
	print(f'{GREEN} {"Usuário =  "} {user} {RST}')
	print()
	print('%s | %s | %s' % tuple(mk[0:3]))
	print('---+---+---')
	print('%s | %s | %s' % tuple(mk[3:6]))
	print('---+---+---')
	print('%s | %s | %s' % tuple(mk[6:9]))
	print()
def verif():
	global empate,micro,user
	for n in range(8):
		if GetLine(n) == 3:
			print(f'{BLUE} {"Computador Ganhou"} {RST}')
			micro += 1
			sleep(2)
			return True
		if not vazio in board:
			print('Empate...')
			empate += 1
			sleep(2)
			return True
	return False
if __name__ == '__main__':

   # Define variáveis usadas para mostrar cores no terminal
   RST     = '\033[00m'
   GRAY    = '\033[30m'
   RED     = '\033[31m'
   GREEN   = '\033[32m'
   YELLOW  = '\033[33m'
   BLUE    = '\033[34m'
   VIOLET  = '\033[35m'
   VERDAO  = '\033[36m'
   WHITE   = '\033[37m'

   empate = 0
   micro  = 0
   user   = 0
   vazio  = 0

   while True:

      board = [vazio] * 9

      Flag = random.choice([True, False])

      display()

      while True:

         Flag = not Flag

         if Flag: pcJoga()

         else:    UserJoga()

         display()

         if verif(): break

      display()
      key = input('Quer jogar de Novo? (S/N)')

      if key not in ('S', 's'):
         break

   print('\nFim de Jogo')
