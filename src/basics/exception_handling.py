def log_these_numbers(n): 
    print(n)

def catch_this():
    my_list = [1,2,3,4,5]

    for i in range(7): 
        try: 
            log_these_numbers(my_list[i])
            # Works if you don't specify an error, but will not catch the error if 
            # it's something different than what was specified.
        except IndexError:
            print('Had an error when handling %s index' % i)
            


catch_this()