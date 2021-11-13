"""
    Exercício 06

    Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todoas as médias do aluno deve ser maiores
que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.
"""

matéria1 = 8.6
matéria2 = 7.9
matéria3 = 9.3

média = (matéria1 + matéria2 + matéria3) / 3

print(f'As três notas do aluno foram: {matéria1} - {matéria2} - {matéria3}, com média final de {média:.2f}.')
print(f'Aluno foi aprovado? {média > 7}')
