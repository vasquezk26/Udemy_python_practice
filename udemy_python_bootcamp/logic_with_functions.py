def even_check(number):
   return number % 2 == 0

print(even_check(20))
print(even_check(21))


#return tru if any number is even inside a list

def check_even_list(num_list):

    for i in num_list:
        if i % 2 == 0:
            return True
        else:
            pass
print(check_even_list([1,3,5]))
#check_even_list([1,3,5])
print(check_even_list([2,4,6]))
#check_even_list([2,4,5])

def check_even_list2(num_list):

    for i in num_list:
        if i % 2 == 0:
            return True
        else:
            pass
    return False

print(check_even_list2([1,3,5]))
#check_even_list([1,3,5])


def check_even_list3(num_list):
    #return all the even numbers in a list
    even_numbers = []
    for i in num_list:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            pass
    return even_numbers

print(check_even_list3([1,2,3,4,5,6,7]))



