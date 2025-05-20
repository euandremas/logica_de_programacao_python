programa
{
	
	funcao inicio()
	{
		inteiro maiorIdade = 0, menorIdade = 0, idade, jogadorMaisVelho = 0, jogadorMaisNovo = 0
		para(inteiro i=1; i <= 6; i++){
			escreva("Digite a idade do jogador ", i,": ")
			leia(idade)
			se(i == 1){
				maiorIdade = idade
				menorIdade = idade
				jogadorMaisNovo = i
				jogadorMaisVelho = i
				
			} senao{
				
				se (idade > maiorIdade){
					jogadorMaisVelho = i
					maiorIdade = idade
				}
				se (idade < menorIdade){
					jogadorMaisNovo = i
					menorIdade = idade
			}
		
		}	
			
		}
		escreva("A maior idade do time é: ", maiorIdade, " e a menor idade do time é: ", menorIdade, "\n")
		escreva("O jogador mais velho do time é: ", jogadorMaisVelho, " e o jogador mais novo do time é: ", jogadorMaisNovo)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 763; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */