def calcular_pagamento(salario_hora, horas_regulares, horas_extras):
    pagamento_regular = salario_hora * horas_regulares
    pagamento_extras = horas_extras * salario_hora * 1.5
    pagamento_total = pagamento_regular + pagamento_extras
    return pagamento_total

if __name__ == "__main__":
    salario_hora = float(input("Digite o salário por hora: "))
    horas_regulares = float(input("Digite o total de horas regulares: "))
    horas_extras = float(input("Digite o total de horas extras: "))
    
    pagamento = calcular_pagamento(salario_hora, horas_regulares, horas_extras)
    print(f"O pagamento semanal total é: R$ {pagamento:.2f}")
