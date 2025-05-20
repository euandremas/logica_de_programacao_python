programa
{
	
	funcao inicio()
	{
		inteiro qtdAcai, qtdTapioca
		real valorAcai = 12.00, valorTapioca = 18.00, total
		caracter formaPgto
		escreva("Digite a quantidade de açaí: ")
		leia(qtdAcai)
		escreva("Digite a quantidade de tapioca: ")
		leia(qtdTapioca)
		total = (qtdAcai * valorAcai) + (qtdTapioca * valorTapioca)
		se(total>= 100){
			
			escreva("Digite D para pagamento em dinheiro, P para pagamento em PIX e O para outras formas de pagamento: ")
			leia(formaPgto)
			
			se(formaPgto == 'D' ou formaPgto == 'P'){
				escreva("Valor era de: R$", total, ", mas com o desconto de 10%, seu pedido saiu por: R$", total*0.90)
			}senao{
				escreva("Valor era de: R$", total, ", mas com o desconto de 5%, seu pedido saiu por: R$", total*0.95)
			}

			escreva("\nMuito obrigado, volte sempre!!!") // "\n" pula linha.
		}senao{
			escreva("Valor total sem desconto: R$", total)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 825; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */