# functions with outputs
def my_func():
    result = 3/2
    return result

output = my_func()
print(output)

def format_name(f_name,l_name):
    '''takes first name and last name as input and returns a
    single string formatted in a titled manner '''

    return (f_name+" "+l_name).title()

name = format_name("adiTYa","moHIte")
print(name)