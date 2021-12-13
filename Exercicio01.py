'''
Exercício: Formulário
nome, CPF, endereço, idade, altura e telefone
Obs.: Imprimir em um relatório
'''

nome = input("Digite seu nome completo: ")
cpf = input("Digite seu CPF (Obs.: Somente números): ")
cargo = input("Digite o cargo em que fez a solicitação da insenção: ")
cidade = input("Digite a cidade: ")
uf = input("Digite a unidade da federação: ")
dia = input("Digite o dia: ")
mes = input("Digite o mês (escrito): ")
ano = input("Digite o ano: ")

print("Eu,",nome,", inscrito(a) no CPF sob o número", cpf,
", declaro, para fins de isenção de pagamento de taxa de inscrição no concurso público para provimento de cargo de",
      cargo, ", ser membro de família de baixa renda, nos termos do Decreto nº 6.135, de 26 de junho de 2007, e que," +
      " em função de minha condição finaceira, não posso pagar a taxa de inscrição")
print("Declaro estar ciente de que, de acordo com o inciso I do art. 4º do referido decreto, família é a unidade nuclear" +
" composta por um ou mais indivíduos, eventualmente ampliada por outros indivíduos que contribuam para o rendimento" +
      " ou tenham suas despesas atendidas por aquela unidade familiar, todos moradores em um mesmo domicílio, definido" +
      " como o local que serve de moradia à família")
print("Declaro, ainda, saber que, de acordo com o inciso II do art. 4º do Decreto nº 6.135, de 2007, família" +
      " de baixa renda, sem prejuízo do disposto no inciso I, é aquela com renda familiar mensal per capita de" +
      " até meio salário mínimo; ou a que possua renda familiar mensal de até três salários mínimos.")
print("Declaro, também, ter conhecimento de que a renda familiar mensal é a soma dos rendimentos brutos auferidos" +
      " por todos os membros da família, não sendo incluídos no cálculo aqueles percebidos dos programas descritos" +
      " no inciso IV do art. 4º do Decreto nº 6.135, de 2007.")
print("Declaro saber que renda familiar per capita é obtida pela razão entre a renda familiar mensal e o total" +
      " de indivíduos na família.")
print("Declaro, por fim, que, em função de minha condição financeira, não posso pagar a taxa de inscrição em" +
      " concurso público e estar ciente das penalidades por emitir declaração falsa previstas no parágrafo único" +
      " do art. 10 do Decreto no 83.936, de 6 de setembro de 1979.")
print("Por ser verdade, firmo o presente para que surtam seus efeitos legais")

print(cidade, "/", uf, dia, "de", mes,"de", ano)

print(""""______________________________________________________
            Assinatura completa do declarante""")