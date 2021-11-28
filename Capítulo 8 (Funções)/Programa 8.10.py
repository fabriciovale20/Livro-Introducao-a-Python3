"""
    Programa 8.10 - Função soma com parâmetros obrigatórios e opcionais
"""
# Os campos obrigatórios como a e b, devem vir primeiro que o opcional. Se vier depois, está incorreto como no exemplo abaixo:
# def soma(imprime=False, a, b): → Dessa forma está incorreto, pois o campo opcional está no início.

def soma(a, b, imprime=False):
    s = a + b
    if imprime:
        print(s)
    return s