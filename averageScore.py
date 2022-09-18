n = int(input("Enter the number of records: "))
student_marks = {}
for x in range(n):
    name, *line = input(f"Enter Name and score of the Student {x+1}: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("Enter the Student Name: ")

li=student_marks[query_name]
total=count=0
for num in li:
    total += num
    print(total,num)
    count +=1
print(count)
avg = total/count
print(f'{avg:.2f}')
