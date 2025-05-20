programa
{
	
	funcao inicio()
	{
		inteiro numero, qtd = 0
		escreva("Digite um número inteiro: ")
		leia(numero)
		qtd++
		enquanto(numero>0){
			escreva("Digite um novo número inteiro: ")
			leia(numero)
			qtd++
		}
		escreva("Você digitou ", qtd, " número(s)")
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