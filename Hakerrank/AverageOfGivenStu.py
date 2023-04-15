if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    add = 0
    for x in student_marks:
        if x == query_name:
            for each_ele in student_marks[x]:
                add += each_ele
            avg = add / len(scores)
            add = 0
            print(f"{avg:.2f}")
