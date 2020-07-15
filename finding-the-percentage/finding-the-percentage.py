



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks)

    notas = student_marks[query_name]
    somaNotas = sum(notas)
    numNotas = float(len(notas))
    media = somaNotas/numNotas
    mdFinal = ("%0.2f" % (media))
    print(mdFinal)