programa
{
	
	funcao inicio()
	{	
		real peso, pesoLimite
		
		escreva("Digite seu peso: ")
		leia(peso)
		
		escreva("Digite o peso limite da categoria: ")
		leia(pesoLimite)
		
		se(peso<=pesoLimite){
			escreva("O lutador bateu o peso da categoria")

		}senao{
			escreva("O lutador excedeu o peso da categoria")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 258; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */