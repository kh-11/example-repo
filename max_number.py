student_scores = [10, 34,  12,  35, 40 ]

max = 0
for score in student_scores:
    if max < score:
        max = score
        print(max)
print(f"\n{max}")

