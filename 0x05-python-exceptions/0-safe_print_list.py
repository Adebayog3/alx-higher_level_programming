#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
   try:
        count = 0
        for element in my_list:
           print(element, end= ' ')
           count += 1
           if count == x:
               break
        print()
        return count
    except IndexError:
        print('Error: Index out of range!')
        return 0
