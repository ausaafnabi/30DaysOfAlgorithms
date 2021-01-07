import random as r

class Transport:
    def __init__(self,arr,dep):
        self.arr = arr
        self.dep = dep
    def __lt__(self,other):
        return self.arr < other.arr

def findPlatform(Station):
    n = len(Station)
    Station.sort()
    plat_needed = 1
    result = 1
    i=1 
    j=0
    while(i<n and j<n):
        if (Station[i].arr<=Station[j].dep):
            plat_needed +=1
            i +=1
        elif(Station[i].arr > Station[j].dep):
            plat_needed -= 1
            j += 1
        
        if (plat_needed > result):
            result = plat_needed
    return result


def main():
    Station = []
    print("Station : ")
    print("Arrival\tDeparture")
    for i in range(10):
        arr = r.randrange(1100)+900
        Station.append(Transport(arr,r.randrange(200)+arr))
        print(" {0}\t\t{1} ".format(Station[i].arr,Station[i].dep))
    print("Minimum Platform Required :",findPlatform(Station))

if __name__=="__main__":
    main()
