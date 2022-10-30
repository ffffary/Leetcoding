# *********to keep track of time on reading question, coding and testing*********
# reading question: 2m
# coding: 33m
# test code successfully: 2m

# thoughts: 
# initialize a hashTable to store each team and its corresponding points
# loop through all the competions, and update the hashTable at each iteration(if team name in it, add 3 points, otherwise add a new entry)
# keep track of scores in the hashTable, compare and return team with the highest score

# O(N) time | O(K) space
# N: #of competitions; K: #of teams

HOME_TEAM_WON = 1
def tournamentWinner(competitions, results):
    currentWinner = ""
    totalScores = {currentWinner: 0}
    for idx, competition in enumerate(competitions):
        result = results[idx]
        # split the inner array(competition) into 2 components
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScore(winningTeam, 3, totalScores)

        if totalScores[winningTeam] > totalScores[currentWinner]:
            currentWinner = winningTeam
    return currentWinner

def updateScore(team, points, totalScores):
    if team not in totalScores:
        totalScores[team] = 0
    totalScores[team] += points




