#Fibonacci Series:
#problem we are going to work is the position were given and we need to find the 
#fibonacci series.

#bottom-up-approach


def fibo(n):
    dp = [0]*n
    dp[0] = 1
    dp[1] = 1

    if(n<2):
        print("1")
        return

    for i in range(2,n):
        dp[i] = (dp[i-1]) + (dp[i-2])

    print(f"fibanocci of position{n}-->{dp[n]}")


#Top - Down - Approach:
    

    def fibo1(pos,mem):

        for pos in mem:
            return mem[pos]
        
        if pos<=2:
            return 1
        
        mem[pos] = fibo1(pos-1,mem) + fibo(pos-2,mem)

        return mem[pos]


    