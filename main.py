from motorInferencia import inferencia
from Elevador import Elevador

def main():
	elevador = Elevador()

	print('>> Andar atual do elevador: 1º')
	while True:
		andar_botao = input('Digite o número de um andar ou uma sequência de andares: ')
		elevador.requisicao(andar_botao) 
		elevador.operacao()
if __name__ == '__main__':
	main()

