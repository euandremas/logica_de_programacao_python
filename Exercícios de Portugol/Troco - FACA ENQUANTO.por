programa
{
	funcao inicio()
	{
		real valorCompra, valorDinheiro, troco
		caracter resposta

		faca {
			escreva("Digite o valor da compra: ")
			leia(valorCompra)

			escreva("Digite o valor em dinheiro recebido: ")
			leia(valorDinheiro)

			se (valorDinheiro >= valorCompra) {
				troco = valorDinheiro - valorCompra
				escreva("\nTroco: ", troco, " \n")
				escreva("\n\nPróximo cliente? s para Sim e n para Não: ")
				leia(resposta) // Lê apenas uma variável

				se (resposta == 'n') {
					escreva("Sistema encerrado")
				}
			} senao {
				escreva("\nValor em dinheiro insuficiente.\n\n")
				resposta = 's' // Para continuar o loop em caso de valor insuficiente
			}
		} enquanto (resposta == 's')
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 354; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */