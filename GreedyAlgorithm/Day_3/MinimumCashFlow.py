def getMin(arr):
    minInd = 0
    for i in range(1,N):
        if(arr[i] < arr[minInd]):
            minInd = i
    return minInd

def getMax(arr):
    maxInd =0
    for i in range(1,N):
        if (arr[i] > arr[maxInd]):
            maxInd = i
    return maxInd

def minOf2(x,y):
    return x if x<y else y

def minCashFlowRec(amount): 
  
    # Find the indexes of minimum 
    # and maximum values in amount[] 
    # amount[mxCredit] indicates the maximum 
    # amount to be given(or credited) to any person. 
    mxCredit = getMax(amount) 
    mxDebit = getMin(amount) 
  
    # If both amounts are 0,  
    # then all amounts are settled 
    if (amount[mxCredit] == 0 and amount[mxDebit] == 0): 
        return 0
  
    # Find the minimum of two amounts 
    min = minOf2(-amount[mxDebit], amount[mxCredit]) 
    amount[mxCredit] -=min
    amount[mxDebit] += min
  
    # If minimum is the maximum amount to be 
    print("Person " , mxDebit , " pays " , min
        , " to " , "Person " , mxCredit) 
    # Recur for the amount array. Note that 
    minCashFlowRec(amount) 


# Function to calculate the min Cash Flow
def minCashFlow(graph): 
  
    # Create an array amount[], 
    # initialize all value in it as 0. 
    amount = [0 for i in range(N)] 
  
    # Calculate the net amount to be paid 
    # to person 'p', and stores it in amount[p]. 
    # The value of amount[p] can be calculated by 
    # subtracting debts of 'p' from credits of 'p' 
    for p in range(N): 
        for i in range(N): 
            amount[p] += (graph[i][p] - graph[p][i]) 
  
    minCashFlowRec(amount) 


if __name__ == "__main__":
    graph = [   [0,1000,2000],
                [0,0,5000],
                [0,0,0] ]
    N = 3
    minCashFlow(graph)
