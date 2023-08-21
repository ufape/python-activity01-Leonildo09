# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 1 - Problem 3
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Programa Simples de Pagamento

Informe quantas horas você trabalhou: 5

Processes:
Fornecida a quantidade de horas trabalhadas, calcule e forneça as informações conforme saída.

valor da hora trabalhada: 25
imposto: 0.125
salario bruto: valor da hora trabalhada * horas trabalhadas
impostos a cobrar: salario bruto * impostos a cobrar
salario liquido: salario bruto - impostos a cobrar

Output(s):
Programa Simples de Pagamento

Informe quantas horas você trabalhou: 5

Contracheque
        Horas trabalhadas: 5
        Valor da Hora: R$25.00
        Salário Bruto: R$125.00
        Imposto: R$15.62
        Salário Líquido: R$109.38 
"""


def main():
     main()def main():
    print("Programa Simples de Pagamento")
    
    horas_trabalhadas = float(input("Informe quantas horas você trabalhou: "))
    valor_hora = 25.00
    imposto = 0.125
    
    salario_bruto = valor_hora * horas_trabalhadas
    impostos_a_cobrar = salario_bruto * imposto
    salario_liquido = salario_bruto - impostos_a_cobrar
    
    print("Contra cheque")
    print(f"    Horas trabalhadas: {horas_trabalhadas}")
    print(f"    Valor da Hora: R${valor_hora:.2f}")
    print(f"    Salário Bruto: R${salario_bruto:.2f}")
    print(f"    Imposto: R${impostos_a_cobrar:.2f}")
    print(f"    Salário Líquido: R${salario_liquido:.2f}")


if __name__ == '__main__':
    main()
