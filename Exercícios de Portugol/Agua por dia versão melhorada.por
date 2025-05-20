programa
{
    funcao inicio()
    {
        real peso, agua_ml, agua_litro
        inteiro arredonda

        escreva("Digite seu peso: ")
        leia(peso)

        agua_ml = peso * 35
        // Arredondando para 2 casas decimais e convertendo para inteiro
        arredonda = (agua_ml + 0.5) // Arredondamento para 1 casa decimal

        agua_litro = arredonda / 1000.0 // Converte o valor para litros

        escreva("A quantidade de água recomendada para você baseada no seu peso informado é de: ", agua_litro, "L por dia!")
    }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 522; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */