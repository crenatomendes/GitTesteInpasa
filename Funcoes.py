def calcular_inss(salario_bruto):

    if salario_bruto <= 1412:
        inss = salario_bruto*0.075
    elif salario_bruto > 1412 and salario_bruto <= 2666.68:
        inss = salario_bruto*0.09
        inss = inss - 21.18
    elif salario_bruto > 2666.68 and salario_bruto <= 4000.03:
        inss = salario_bruto*0.12
        inss = inss - 101.18
    elif salario_bruto > 4000.03 and salario_bruto <= 7786.02:
        inss = salario_bruto*0.14
        inss = inss - 101.18
    else:
        inss = 7786.02*0.14
        inss = inss - 181.18

    return round(inss, 2)

def calcular_ir(salario_bruto):

    inss = calcular_inss(salario_bruto)
    salario_desc = salario_bruto - inss

    if salario_desc <= 2259.20:
        ir = 0
    elif salario_desc > 2259.20 and salario_desc <= 2826.65:
        ir = salario_desc*0.075
        ir = ir - 169,44
    elif salario_desc > 2826.65 and salario_desc <= 3751.05:
        ir = salario_desc*0.15
        ir = inss - 381.44
    elif salario_desc > 3751.05 and salario_desc <= 4664.68:
        ir = salario_desc*0.225
        ir = ir - 662.77
    else:
        ir = salario_desc*0.275
        ir = ir - 896.00

    return round(ir, 2)

def calcular_salario(salario_bruto):

    inss = calcular_inss(salario_bruto)
    ir = calcular_ir(salario_bruto)
    salario = salario_bruto - inss - ir

    return round(salario, 2)
