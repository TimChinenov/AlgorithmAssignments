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
    #n = int(raw_input('Enter Fibonacci number to be calculated: '))
    #startTime = timeit.default_timer()
    #fib2(n)
    #finTime = timeit.default_timer()
    #print "iterative: " + str(finTime - startTime)
    
    
    #startTime = timeit.default_timer()
    #fib1(n)
    #finTime = timeit.default_timer()
    #print "Recursive: " + str(finTime - startTime)

    #Script to plot time difference between the two Algorithm
    #setup code that is run by timeit module.
    fib1Time = []
    fib2Time = []
    values = [1,5,10,15,20,25,30,35,40]#,41,42,43]

    #The functions that will be run
    for n in values:
        startTime = timeit.default_timer()
        fib1(n)
        finTime = timeit.default_timer()
        fib1Time.append(finTime - startTime)
        
        startTime = timeit.default_timer()
        fib2(n)
        finTime = timeit.default_timer()
        fib2Time.append(finTime - startTime)
        
    ans = raw_input("Do you want to plot data? (y/n) ")
    if ans == "y":
        import matplotlib.pyplot as plt
        plt.plot(values, fib1Time, marker='o', label='Recursive')
        plt.plot(values, fib2Time, marker='o', label='Iterative')
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        plt.show()
