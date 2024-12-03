#O(n^2) time | O(n) space
def tournamentWinner_v1(competitions, results):
    scoreMap = {}
    for idx, x in enumerate(competitions):
        if results[idx] == 0:
            if x[1] not in scoreMap:
                scoreMap[x[1]] = 3
            else:
                scoreMap[x[1]] = scoreMap[x[1]] + 3
            if x[0] not in scoreMap:
                scoreMap[x[0]] = 0
            else:
                scoreMap[x[0]] = scoreMap[x[0]] + 0
        else:
            if x[1] not in scoreMap:
                scoreMap[x[1]] = 0
            else:
                scoreMap[x[1]] = scoreMap[x[1]] + 0
            if x[0] not in scoreMap:
                scoreMap[x[0]] = 3
            else:
                scoreMap[x[0]] = scoreMap[x[0]] + 3

    winner = ''
    currVal = 0
    for key, value in scoreMap.items():
        if value > currVal:
            currVal = value
            winner = key
            print(winner)
    return winner




# competitions = [
#   ["HTML", "C#"],
#   ["C#", "Python"],
#   ["Python", "HTML"]
# ]

# results = [0, 0, 1]


# tournamentWinner(competitions, results)

competitions = [
  ["HTML", "Java"],
  ["Java", "Python"],
  ["Python", "HTML"]
]

results = [0, 1, 1]


print(tournamentWinner_v1(competitions, results))


# O(n) time | O(n) space
def tournamentWinner_v2(competitions, results):
    scoreMap = {}
    winningScore = 0
    winnerName = ''
    for idx, c in enumerate(competitions):
        # define winner
        tourWinnerName = c[1] if results[idx] == 0 else c[0]
        # init dict key
        if tourWinnerName not in scoreMap:
            scoreMap.setdefault(tourWinnerName, 0)
        # update one's score
        scoreMap[tourWinnerName] = scoreMap[tourWinnerName] + 3
        #compare the score with the winningScore
        if scoreMap[tourWinnerName] > winningScore:
            winningScore = scoreMap[tourWinnerName]
            winnerName = tourWinnerName 
    return winnerName


#O(n) time | O(n) space
# improved version of tournamentWinner_v2
def tournamentWinner_v3(competitions, results):
    currBestTeam = ''
    scoreMap = {'': 0}
    for idx, c in enumerate(competitions):
        # define winner
        tourWinnerName = c[1] if results[idx] == 0 else c[0]
        # update winner's score
        if tourWinnerName not in scoreMap:
            scoreMap.setdefault(tourWinnerName, 3)
        else:
            scoreMap[tourWinnerName] = scoreMap[tourWinnerName] + 3
        # compare the tour winner's score with the current best team's score
        if scoreMap[tourWinnerName] > scoreMap[currBestTeam]:
            currBestTeam = tourWinnerName 
    return currBestTeam