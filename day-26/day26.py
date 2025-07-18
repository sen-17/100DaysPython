# List Comprehension
# new_list = [new_item for item in list]

numbers = [1,2,3]

new_numbers = [n + 1 for n in numbers]
print(new_numbers)

# list , range , string , tuples (python sequences)

double_num = [n*2 for n in range(1,5)]
print(double_num)

# Conditional List Comprehension
# new_list = [new_item for item in list if test]

names = ["alex", "beth" , "caroline", "dave", "Freddy", "Elanor"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_name = [name.upper() for name in names if len(name) > 5]
print(long_name)

# Dictionary Comprehension
# new_dict = {new_key : new_value for item in list}
# new_dict = {new_key : new_value for (key, value) in dict.items() if test}
import random

student_scores = {student: random.randint(1,100) for student in names}
print(student_scores)

passed_students = {student: value for (student , value) in student_scores.items() if value > 60}
print(passed_students)


student_dict = {
    "student" : ["angela", "james", "lily"],
    "score" : [56,76,98]
}
# for(key, value) in student_dict.items():   
#     print(value)

# Iterate over pandas dataframe
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# for (key,value) in student_data_frame.items():
#     print(key)
#     print(value)

for (index , row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)