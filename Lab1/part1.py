#First algorithm for Fibonacci. Recursive algorithm
def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n-1) + fib1(n-2)

#Second algorithm for Fibonacci. Not recursive, instead creates array of
#Fibonacci values from repeated addition operation of previous two fib values.
def fib2(n):
    if n == 0:
        return 0
    nums = [0]*(n+1)
    nums[0] = 0
    nums[1] = 1
    for i in range(2,n+1):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]

if __name__=="__main__":
    import timeit

    #Script to calculate fib number
    #n = input('Enter Fibonacci number to be calculated: ')
    # print "Algorithm 1:" + str(fib1(n))
    # print "Algorithm 2:" + str(fib2(n))


    #Script to demonstrate individual timing
    # fib1Val = '''fib1(n)'''
    # fib2Val = '''fib2(n)'''
    #
    #
    # print(timeit.timeit(stmt = fib1Val,setup="from __main__ import fib1; \
    #         n = input('Enter Fibonacci number to be calculated: ')"))
    #
    # print(timeit.timeit(stmt = fib2Val,setup="from __main__ import fib2; \
    #         n = input('Enter Fibonacci number to be calculated: ')"))

    #Script to plot time difference between the two Algorithm
    def setup(): #Used to give fib number to the timeit module
        return setup_data

    #setup code that is run by timeit module.
    setup_code = """from __main__ import fib1, fib2, setup
data = setup()
    """

    fib1Time = []
    fib2Time = []
    values = [1,5,10,15,20,25,30,35,40,41,42,43]

    #The functions that will be run
    fib1Val = '''fib1(data)'''
    fib2Val = '''fib2(data)'''

    for num in values:
        setup_data = num
        fib1Time.append(timeit.timeit(fib1Val,setup_code))
        fib2Time.append(timeit.timeit(fib2Val,setup_code))

    print fib1Time
    print fib2Time

    ans = input("Do you want to plot data? (y/n)")
    if ans == "y":
        import matplotlib.pyplot as plt
        plt.plot(fib1Time, values, 'r-')
        plt.plot(fib2Time, values, 'b-')
        plt.show()
