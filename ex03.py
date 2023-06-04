def calcular_opcoes_emprestimo():
    nome = input("Digite o nome do colaborador: ")
    data_admissao = input("Digite a data de admissão do colaborador (formato: dd/mm/aaaa): ")
    salario = float(input("Digite o salário atual do colaborador: "))
    valor_emprestimo = float(input("Digite o valor desejado para o empréstimo: "))

    tempo_casa = calcular_tempo_casa(data_admissao)
    if tempo_casa <= 5:
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
        return

    if valor_emprestimo % 2 != 0:
        print("Insira um valor válido (múltiplo de 2).")
        return

    notas_maiores = [100, 50]
    notas_menores = [20, 10, 5, 2]

    notas_maiores_retirada = []
    valor_restante = valor_emprestimo

    for nota in notas_maiores:
        quantidade = int(valor_restante // nota)
        if quantidade > 0:
            notas_maiores_retirada.append((quantidade, nota))
            valor_restante -= quantidade * nota

    notas_menores_retirada = []
    valor_restante = valor_emprestimo

    for nota in notas_menores:
        quantidade = int(valor_restante // nota)
        if quantidade > 0:
            notas_menores_retirada.append((quantidade, nota))
            valor_restante -= quantidade * nota

    valor_maiores = int(valor_emprestimo // 2)
    valor_menores = valor_emprestimo - valor_maiores

    notas_maiores_meio_meio = []
    notas_menores_meio_meio = []

    for nota in notas_maiores:
        quantidade = int(valor_maiores // nota)
        if quantidade > 0:
            notas_maiores_meio_meio.append((quantidade, nota))
            valor_maiores -= quantidade * nota

    for nota in notas_menores:
        quantidade = int(valor_menores // nota)
        if quantidade > 0:
            notas_menores_meio_meio.append((quantidade, nota))
            valor_menores -= quantidade * nota

print(f"Valor empréstimo: {valor_emprestimo} reais")
print("Notas de maior valor:")
for quantidade, nota in notas_maiores_retirada:
    print(f"{quantidade} x {nota} reais")

print("Notas de menor valor:")
for quantidade, nota in notas_menores_retirada:
    print(f"{quantidade} x {nota} reais")

print("Notas meio a meio:")
print(f"{valor_emprestimo} reais em notas de maior valor:")
for quantidade, nota in notas_maiores_meio_meio:
    print(f"{quantidade} x {nota} reais")

for quantidade, nota in notas_menores_meio_meio:
    print(f"{quantidade} x {nota} reais")