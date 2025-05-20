programa
{
    funcao inicio()
    {
        inteiro numero, i, contDivisores

        escreva("Digite um número: ")
        leia(numero)

        contDivisores = 0

        para (i = 1; i <= numero; i++) 
        {
            se (numero % i == 0) 
            {
                contDivisores = contDivisores + 1
            }
        }

        se (contDivisores == 2) 
        {
            escreva("O número é primo.")
        } senao 
        {
            escreva("O número não é primo.")
        }
    }
}


/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 295; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */