# Finding all the prime numbers from 0 to 100 using fumctions 

def foo(): # Creating the function
    for num in range(1, 101): # Defining range
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)

foo()
