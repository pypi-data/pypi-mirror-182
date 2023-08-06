from viggocore.common import exception
from decimal import Decimal


# verifica se um número é par
def se_e_par(n):
    n = int(n)
    if (n % 2) == 0:
        return True
    else:
        return False

# função criada para arredondar um valor usando a norma ABNT 5891/77
# onde valor=o valor a ser arredondado
# n=limitador da quantidade de casas
def round_abnt(valor, n: int):
    try:
        vl_str = str(valor)
        if '.' in vl_str:
            inteira, decimal = str(valor).split('.')
        else:
            inteira = str(valor)
            decimal = '00'
    except Exception:
        print('Erro na conversão do valor!')

    decimal = (decimal + ('0' * n))
    if len(decimal) > (n+2):
        prox = int(decimal[n])
        pos_prox = int(decimal[n+1])
        if ((prox >= 5 and pos_prox != 0) or
           (prox == 5 and pos_prox == 0 and se_e_par(decimal[n]) is False)):
            aux = int(decimal[n-1]) + 1
            decimal = decimal[:n-1] + str(aux) + decimal[n:]
    decimal = decimal[:n]
    return Decimal(f'{inteira}.{decimal}')