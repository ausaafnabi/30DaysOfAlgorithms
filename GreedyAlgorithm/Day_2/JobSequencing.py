from dataclasses import dataclass
import random as r

@dataclass
class Job:
    jobID : int
    deadline : int
    profit : int     
    
    def __lt__(self,other):
        return self.profit < other.profit


def JobScheduling(jobs,t):
    n = len(jobs)

    # Sort all jobs acc. to
    # Decreasing order of the Profit
    #
    jobs.sort(reverse=True)

    result = [False] * t

    jobSq = ['-1'] * t

    for i in range(n):
        #Find a free slot for this job
        # (Start from last possible slot)
        for j in range(min(t-1,jobs[i].deadline-1),-1,-1):
            if result[j] is False:
                result[j] = True
                jobSq[j] = jobs[i].jobID 
                break

    return jobSq 


def main():
    Jobs = []
    for i in range(10):
        Jobs.append(Job(i,r.randrange(7),(r.randrange(70)+10)))
    print("JobID\tDeadline\tProfit")
    for i in range(10):
        print("{0}\t{1}\t{2}".format(Jobs[i].jobID,Jobs[i].deadline,Jobs[i].profit))
    jobsequence = JobScheduling(Jobs,4)
    print(jobsequence)


if __name__  == "__main__":
    main()
