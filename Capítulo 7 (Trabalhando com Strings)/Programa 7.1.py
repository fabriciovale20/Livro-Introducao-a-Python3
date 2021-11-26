"""
    Programa 7.1 - Pesquisa de todas os ocorrências  
"""

s = 'um tigre, dois tigres, três tigres'
p = 0

while (p > -1):
    p = s.find('tigre', p)

    if p >= 0:
        print(f'Posição: {p}')
        p += 1
