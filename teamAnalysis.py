"""
Team Stats to track from FBRef:
    Season Stats:
        - Matches Played (MP)
        - Wins (W)
        - Draws (D)
        - Losses (L)
        - Goals For (GF)
        - Goals Against (GA)
        - Goal Difference (GD)
        - Points (Pts)
        - Points per Match (Pts/MP)
        - Expected Goals For (xGF)
        - Expected Goals Against (xGA)
        - Expected Goal Difference (xGD)

    Squad Stats:
        - Number of Players Used (#Pl)
        - Average Age of Players Used (Age)
        - Average Possession (Poss)
        - Matches Played (MP)
        - Assists (Ast)
        - Goals + Assists (G+A)
        - Penalty Kick Goals (PK)
        - Goals - Penalty Goals (G-PK)
        - Penalty Attempts (PKAtt)
        - Yellow Cards (CrdY)
        - Red Cards (CrdR)
        - Non-Penalty Expected Goals (NPxG)
        - Expected Assisted Goals (xAG)
        - Non-Penalty xG + xAG (NPxG + xAG)
        - Progressive Carries (PrgC)
        - Progressive Passes (PrgP)

    Squad Goalkeeping:

    Squad Shooting:

    Squad Passing:

    Squad Defensive Actions:

    Squad Possession:

    Squad Playing Time:
        
"""    
"""
    Teams:
        Arsenal (ARS)
        Aston Villa (AVL)
        Bournemouth (BOU)
        Brentford (BRE)
        Brighton (BRI)
        Burnley (BUR)
        Chelsea (CHE)
        Crystal Palace (CRY)
        Everton (EVE)
        Fulham (FUL)
        Liverpool (LIV)
        Luton Town (LTN)
        Manchester City (MCI)
        Manchester United (MUN)
        Newcastle United (NEW)
        Nottingham Forrest (NFO)
        Sheffield United (SHE)
        Tottenham (TOT)
        West Ham (WHU)
        Wolves (WOL)
"""


class Team:
    def __init__(self, name, wins, draws, losses, gf, ga, xgf, xga):
        #Team Info
        self.name = name

        #Wins, Draws, Losses and Points
        self.wins = wins
        self.draws = draws
        self.losses = losses
        mp = wins + draws + losses
        self.mp = mp
        self.points = 3*wins + 1*draws

        #Goals For, Against & Difference
        self.gf = gf
        self.gf90 = gf / mp
        self.ga = ga
        self.ga90 = ga / mp
        gd = round(gf - ga, 2)
        self.gd = gd
        self.gd90 = gd / mp

        #Expected Goals For, Against & Difference
        self.xgf = xgf
        self.xgf90 = xgf / mp
        self.xga = xga
        self.xga90 = xga / mp
        xgd = round(xgf - xga, 2)
        self.xgd = xgd
        self.xgd90 = xgd / mp

Arsenal = Team('Arsenal',   #Name
               3,           #Wins 
               1,           #Draws
               0,           #Loses
               11,          #Goals For
               2,           #Goals Against  
               8.3,         #xGoals For
               3.7)         #xGoals Against

Everton = Team('Everton',   #Name
               0,           #Wins 
               1,           #Draws
               3,           #Loses
               2,          #Goals For
               8,           #Goals Against  
               7.2,         #xGoals For
               6.7)         #xGoals Against

print(Arsenal.name, Arsenal.points, Arsenal.mp, Arsenal.gd, Arsenal.xgd, Arsenal.gd90, Arsenal.xgd90)

print(Everton.name, Everton.points, Everton.mp, Everton.gd, Everton.xgd, Everton.gd90, Everton.xgd90)