programa
{

    inclua biblioteca Matematica --> mat

    inclua biblioteca Tipos --> t

    funcao inicio()

    {

        real numero, raiz

        inteiro raizInteira

        escreva("Digite um número: ")

        leia(numero)

        raiz = mat.raiz(numero, 2.0)

        raizInteira = t.real_para_inteiro(raiz)

        se (mat.potencia(raizInteira, 2.0) == numero){

            escreva("O número é um quadrado perfeito")    

        } senao {

            escreva("O número não é um quadrado perfeito")    

        }

    }

 

}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 12; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */