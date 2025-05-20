programa
{
	
	funcao inicio()
	{
		real salarioBruto, previdencia = 0.12, valeTransporte = 0.06, descontoTotal, valorLiquido, calculoDescontos
		
		escreva("Digite seu salário bruto: ")
		leia(salarioBruto)
		
		calculoDescontos = (salarioBruto * previdencia) + (salarioBruto * valeTransporte)
		
		descontoTotal = calculoDescontos
		
		valorLiquido = salarioBruto - descontoTotal
		
		escreva ("O total de descontos no seu salário é de: R$", descontoTotal, " e o valor líquido que você irá receber é de: R$", valorLiquido)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 386; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */