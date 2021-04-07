#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/nested-list/problem
#
# Title: Nested Lists
#


if __name__ == '__main__':

    alunos = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        alunos.append([name, score])
    
    alunosAlfab = sorted(alunos)
    #print(alunosAlfab)

    mn = 1000
    seg_mn = 1000

    for i in alunos:
        print(i)
        nota = i[1]

        if nota < mn:
            seg_mn = mn
            mn = nota     
        if nota < seg_mn and nota > mn:
            seg_mn = nota
        if nota < mn and nota < seg_mn:
            seg_mn = mn
            mn = nota
    print('Segunda pontuacao mais baixa:', seg_mn)

    nomes_segmn = list(filter(lambda x: (x[1] == seg_mn), alunos))
    print(nomes_segmn)

    nomes = list(map(lambda x: x[0], nomes_segmn))
    print(nomes)
    nomes.sort()
    for i in nomes:
        print(i)

    