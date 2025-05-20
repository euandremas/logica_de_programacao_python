programa
{
	
	funcao inicio()
	{
		inteiro N, contador, qtdPares = 0
			escreva("Digite um número inteiro positivo N: ")
				leia(N)
			escreva("Números pares de 0 até ", N, ":\n")
		
		para (contador = 0; contador <= N; contador = contador + 2) {
			escreva(contador, " ")
			qtdPares = qtdPares + 1
		}

		escreva("\n\nQuantidade total de números pares encontrados: ", qtdPares)
	}
}

/*programa // Declara o início do programa. Todo o código dentro deste bloco pertence ao programa principal.
{

	funcao inicio() // Declara a função principal do programa, onde a execução começa.
	{
		inteiro N, contador, quantidadePares = 0 // Declara três variáveis do tipo inteiro:
		                                        // - N: armazenará o número limite digitado pelo usuário.
		                                        // - contador: será usado para percorrer os números de 0 até N.
		                                        // - quantidadePares: armazenará a contagem de números pares encontrados, inicializada com 0.

		escreva("Digite um número inteiro positivo N: ") // Exibe uma mensagem na tela pedindo para o usuário digitar um número inteiro positivo e armazená-lo em N.
		leia(N) // Lê o número inteiro que o usuário digitar e armazena esse valor na variável N.

		escreva("Números pares de 0 até ", N, ":\n") // Exibe uma mensagem informando o intervalo dos números pares que serão mostrados. O "\n" pula uma linha.

		para (contador = 0; contador <= N; contador = contador + 2) { // Inicia uma estrutura de repetição "para":
		                                                              // - Inicializa a variável 'contador' com o valor 0.
		                                                              // - A condição para continuar o loop é que 'contador' seja menor ou igual a N.
		                                                              // - A cada iteração do loop, 'contador' é incrementado em 2, garantindo que apenas números pares sejam considerados.
			escreva(contador, " ") // Exibe o valor atual da variável 'contador' (que é um número par) seguido de um espaço.
			quantidadePares = quantidadePares + 1 // Incrementa a variável 'quantidadePares' em 1 a cada número par encontrado.
		} // Fim da estrutura de repetição "para".

		escreva("\n\nQuantidade total de números pares encontrados: ", quantidadePares) // Exibe a mensagem com a quantidade total de números pares encontrados. Os "\n\n" pulam duas linhas antes da mensagem.
	} // Fim da função "inicio".

} // Fim do programa.*/
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2511; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */