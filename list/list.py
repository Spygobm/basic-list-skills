marks = [1,9,6,4,33,6,4,2,4]
print(marks)
print(marks[0])
print(marks[6])

#exessing the individual items of our list using for loop

for item in marks:
    print(item)

#finding the number number of items in a list (len of list)

number_of_items = len(marks)
print("This list has {} numbers".format(number_of_items))

#2d list - 2d is also called a list of lists,each row is one individual list
#creating a 2d list 
matrix = [
    [56,327,72],
    [36,78,120],
    [27,18,90]
]
print("printing 2d list")
print(matrix)
#accessing individual items from 2d list
print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][0])

#finding the number of rows in a 2d list
number_rows_in_list = len(matrix)
print("This list has {} rows".format(number_rows_in_list))

#printng number of collums in a list
number_of_columns = len(matrix[0])
print("this list has {} columns".format(number_of_columns)) 