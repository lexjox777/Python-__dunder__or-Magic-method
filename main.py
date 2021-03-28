# # dunder or magic method


from todo import Todo

# x= [1,2,3,4]

# print (len(x))

# # the above code can be written in dunder method below and achieve the same result Thus:

# print(x.__len__())

#=========================


k_todo = Todo(name='Kingsley')

e_todo= Todo(name= 'Emmanuel')

k_todo.add('buy milk')
k_todo.add('code python')
k_todo.add('cook dinner')

print(k_todo > e_todo)