# ls = [1,2,3,5,6]

# new_ls = [] 
# for item in ls:
#     new_ls.append(item+1)

# new_ls = [num+1 for num in ls]

# name = 'Aditya'.lower()

# letters = [character for character in name]

# range_num = [num*2 for num in range(1,6)]

# names = ['Eleanor','Dave','Olive','Steve','Caroline']

# long_names = [name.upper() for name in names if len(name)>=5]
# print(long_names)
from random import randint
import pandas
 
names = ['Eleanor','Dave','Olive','Steve','Caroline']

student_dict = {
    'student': ['Eleanor','Dave','Olive','Steve','Caroline'],
    'score' : [56,34,65,67,87]
}
print(student_dict)

# iterating over a pandas dataframe
new_df = pandas.DataFrame(student_dict)

for (index,row) in new_df.iterrows():
    print(row.student)



