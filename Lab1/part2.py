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
    #import matplotlib as plt

    def setup():
        return setup_data

    setup_code='''from __main__ import fib2, setup
data = setup()'''
    func_code = '''fib2(data)'''

    values = [2**10,2**12,2**14,2**16,2**18]#,2**19]
    timeValues = []
    for value in values:
        setup_data = value
        timeValues.append(timeit.timeit(func_code,setup_code))

    print timeValues
