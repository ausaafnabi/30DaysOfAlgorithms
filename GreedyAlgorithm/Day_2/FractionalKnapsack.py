from dataclasses import dataclass

class ItemValue:
    def __init__(self,wt,val,ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt
    
    def __lt__(self,other):
        return self.cost < other.cost


class FractionalKnapSack:
    @staticmethod
    def getMaxValue(wt,val,capacity):
        '''function to get maximum value'''
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i],val[i],i))
        
        #sort in reverse by value
        iVal.sort(reverse=True)

        totalVal = 0
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity -= curWt
                totalVal += curVal
            else:
                fraction = capacity/curWt
                totalVal += curVal * fraction
                capacity = int(capacity - (curWt*fraction))
                break
        return totalVal 

def main():
    wt = [10,40,20,30]
    val = [60,40,100,120]
    capacity =50
    print("Weight : {0} \t Value : {1} \t capacity : {2}".format(wt,val,capacity))
    maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue) 

if __name__ == "__main__":
    main()

