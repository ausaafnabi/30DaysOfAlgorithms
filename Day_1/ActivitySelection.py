
class activity:
    def __init__(self,start,finish):
        self.start = start
        self.finish = finish


def getActivityObjects(strt,end):
    lst = []
    strt.sort()
    end.sort()
    for i in range(len(strt)):
        lst.append(activity(strt[i],end[i]))
    return lst


def maxActivities(activities):
    num = len(activities)

    # First activity would be selected always
    i=0
    actnum = []             # list to store activity number
    actnum.append(i)
    selectedActivity = []   # list to store the activities
    selectedActivity.append(activities[i])

    # Considering the rest of the activities:
    for j in range(num):
        # if start time >= finish time then add the activity 
        # and make i to j
        if activities[j].start >= activities[i].finish:
            selectedActivity.append(activities[j])
            actnum.append(j)
            i=j

    return actnum , selectedActivity


def main():
    st = [1, 3, 0, 5, 8, 5]
    en = [2, 4, 6, 7, 9, 9]
    activities = getActivityObjects(st,en)
    print("Activities are ::")
    print("(Start,finish)")
    for i in activities:
        print("( {0} , {1} )".format(i.start,i.finish))

    actNumber, selectedActivities = maxActivities(activities)
    
    print("The Following activities are selected:")
    for i in range(len(actNumber)):
        print(str(actNumber[i]+1), " -> \n ","\tstart: ", selectedActivities[i].start, "\t Finish:", selectedActivities[i].finish)


if __name__ == "__main__":
    main()
