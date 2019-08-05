from math import factorial


def fact_find(num):
    if num <= 0:
        print('The Number is not valid, Please Enter again')
        getnum()

    else:
        # if num == 1:
        #     print('The Factorial of', num, 'is 1')
        # else:
        #     fact = 1
        #     for i in range(1, 1+num):
        #         fact = fact*i
        #     print('The factorial of', num, ' is', fact)
        #     print('Thanks')
        #via library
        print(factorial(num))
def getnum():

        num = int(input('Enter the Number: '))
        fact_find(num)

getnum()
