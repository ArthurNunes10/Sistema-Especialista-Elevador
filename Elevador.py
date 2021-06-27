from motorInferencia import inferencia 
import time

class Elevador():
	"""
	#Atributos do objeto elevador
	Por convenção, foi definido inicialmente que o elevador encontra-se parado no 1º andar
	"""
	def __init__(self):
		self.andar_atual = 1
		self.destino_atual = None
		self.fila_requisicoes = []
		self.em_movimento = False
	
	"""
	#Método requisicao()
	Esta função recebe o andar ou uma sequência de andares 
	onde o botão do elevador foi acionado e guarda em uma fila de requisições
	A prioridade é definida pela ordem em que o botão foi acionado
	"""
	def requisicao(self, andar_botao):
		self.fila_requisicoes.extend(andar_botao.strip().split(' '))
	
	"""
	#Método status()
	Faz uma consulta a base de regras fazendo uma inferencia para saber qual
	a próxima ação a ser tomada
	"""
	def status(self):
		return inferencia(str(self.andar_atual), str(self.destino_atual))

	"""
	#Método operacao()
	Define a interface com o usuário e as operações do elevador, 
	mantendo o usuário informado sobre as operações e o status 
	em que o elevador se encontra
	"""
	def operacao(self):
		while self.fila_requisicoes:

			#Atende o andar que solicitou primeiro o elevador
			self.destino_atual = int(self.fila_requisicoes.pop(0))

			#Analise a base de regras e imprime o status do elavador
			print('>> Status do elevador: {} \n'.format(self.status()))

			if self.andar_atual != self.destino_atual:
				print(">> Elevador em movimento...")
				self.em_movimento = True
				time.sleep(3)
				self.andar_atual = self.destino_atual
				print('>> Andar atual do elevador: {}º\n'.format(self.andar_atual))
