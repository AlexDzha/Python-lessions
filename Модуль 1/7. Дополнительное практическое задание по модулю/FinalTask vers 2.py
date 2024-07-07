grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_mark =[sum(sub_list) / len(sub_list) for sub_list in grades]
students_average_mark = dict(zip(sorted(students),average_mark))
print(students_average_mark)
