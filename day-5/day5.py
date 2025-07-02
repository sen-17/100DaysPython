# For Loops
fruits = ['Apple', 'Peach', 'Pear']

for fruit in fruits:
    print(fruit)

student_scores = [150,124,165,123,189,169,146]
total_score = sum(student_scores)
print(total_score)

print(max(student_scores))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

# Range
sum = 0
for number in range(1,101):
    sum += number

print(sum)
    

    


    

