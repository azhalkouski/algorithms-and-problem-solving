# O(nlog(n)) time | O(1) space
def optimalFreelancing(jobs):
    WORKING_DAYS = 7
    workLoad = [False] * WORKING_DAYS
    profit = 0
    jobs.sort(key=lambda job: job["payment"], reverse=True)

    for job in jobs:
        # latestStartDay = WORKING_DAYS if job["deadline"] > WORKING_DAYS else job["deadline"]
        latestStartDay = min(job["deadline"], WORKING_DAYS)
        for startDay in reversed(range(latestStartDay)):
            if workLoad[startDay] == False:
                workLoad[startDay] = True
                profit += job["payment"]
                break
        
    return profit

arg2 = [
  { "deadline": 2, "payment": 2 },
  { "deadline": 4, "payment": 3 },
  { "deadline": 5, "payment": 1 },
  { "deadline": 7, "payment": 2 },
  { "deadline": 3, "payment": 1 },
  { "deadline": 3, "payment": 2 },
  { "deadline": 1, "payment": 3 }
]

arg3 = [
    { "deadline": 2, "payment": 1 },
    { "deadline": 2, "payment": 2 },
    { "deadline": 2, "payment": 3 },
    { "deadline": 2, "payment": 4 },
    { "deadline": 2, "payment": 5 },
    { "deadline": 2, "payment": 6 },
    { "deadline": 2, "payment": 7 }
  ]

print(optimalFreelancing([]) == 0)
print(optimalFreelancing(arg2) == 13)
print(optimalFreelancing(arg3) == 13)
