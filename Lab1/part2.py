def fib2(n):
    if n == 0:
        return 0
    num = [0]*(n+1)
    num[1] = 1
    for i in range(2,n+1):
        num[i] = num[i-1] + num[i-2]
    return num[n]

if __name__=="__main__":
    import timeit
    import matplotlib as plt

    values = [2**10,2**12,2**14,2**16]#,2**18,2**19]
    timeValues = []
    for value in values:
        print "started: " + str(value)
        startTime = timeit.default_timer()
        fib2(value)
        finTime = timeit.default_timer()
        timeValues.append(finTime - startTime)
        print "finished: " + str(value)
        
    ans = raw_input("Do you want to plot data? (y/n) ")
    if ans == "y":
        import matplotlib.pyplot as plt
        plt.plot(values, timeValues, marker='o')
        plt.show()    
