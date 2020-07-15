





if __name__ == '__main__':
#    n = int(input())
#    student_marks = {}

    n = 3
    student_marks = {'Krishna': (67, 68, 69), 'Arjun': (70, 98, 63), 'Malika': (52, 56, 60)}
    for _ in range(n):

#        name, *line = input().split()
#        scores = list(map(float, line))
#        student_marks[name] = scores
#    query_name = input()
        name = {'Krishna': (67, 68, 69), 'Arjun': (70, 98, 63), 'Malika': (52, 56, 60)}
    query_name = 'Arjun'
    print(student_marks)

    notas = student_marks[query_name]
    somaNotas = sum(notas)
    numNotas = float(len(notas))
    media = somaNotas/numNotas
    mdFinal = ("%0.2f" % (media))
    print(mdFinal)