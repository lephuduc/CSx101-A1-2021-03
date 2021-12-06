def nhap_so():
    team = {'goal':0,'lost':0,'yellow':0}
    score = 0
    against = 0
    for i in range(3):
        gf,ga,yc = map(int,input().split())
        if gf>ga:
            score += 3
        elif gf == ga:
            score += 1
        team['goal'] += gf
        team['lost'] += ga
        team['yellow'] += yc
    against +=  (team['goal']-team['lost']) #against = hieu so ban thang
    return team,score,against
def printTeam(team,score,against):
    print(f"{score} {against} {team['goal']} {team['yellow']}")
team1,score1,against1 = nhap_so()
team2,score2,against2 = nhap_so()
team1_win = True
# so sanh
if score1 == score2:
    if against1<against2:
        team1_win = False
    elif against1==against2:
        if team1['goal']<team2['goal']:
            team1_win = False
        elif team1['score']==team2['score']:
            if team1['yellow']>team2['yellow']:
                team1_win = False
if score1 < score2:
    team1_win = False
if team1_win:
    printTeam(team1,score1,against1)
else:
    printTeam(team2,score2,against2)