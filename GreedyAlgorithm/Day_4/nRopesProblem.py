import heapq

def minCost(ropes):
    # Create a priority Queue out of list
    #
    heapq.heapify(ropes)

    #initialize result
    result = 0

    while(len(ropes) > 1):
        #Extract shortest of 2 ropes
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)

        # Connect the ropes : update the result
        # Insert a new rope
        result += first + second
        heapq.heappush(ropes,first+second)
    return result 

if __name__ == "__main__":
    length = [4,3,6,2,1,3,9,5,6,7,8,2,1]
    print("Total cost for connecting ropes is " + str(minCost(length) ))


