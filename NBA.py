#defining class 1
class Player:
  def __init__(self, fn, ln, pts, reb, assist, steal):
    self.fn = fn
    self.ln = ln
    self.pts = pts
    self.reb = reb
    self.assist = assist
    self.steal = steal

#creating the players 2
JHarden = Player("James", "Harden", 2818, 518, 586, 158)
KDurant = Player("Kevin", "Durant", 2027, 497, 457, 58)
LJames = Player("Lebron", "James", 2154, 644, 498, 74)
SCurry = Player("Stephen", "Curry", 2264, 490, 708, 102)
KLeonard = Player("Kawhi", "Leonard", 2326, 614, 445, 86)

#Create a dictionary to match names to players
player_dict = {
  "harden": JHarden,
  "durant": KDurant,
  "james" : LJames,
  "curry" : SCurry,
  "leonard" : KLeonard,
}

#Getting the user to enter a player 3
playerLastName = input("Enter a lastname of a player(Harden, Durant, James, Curry, Leonard): ")
playerLastName = playerLastName.lower()

if player_dict.get(playerLastName) == None:
  print("The name you entered is not valid")
else:
  used_player = player_dict[playerLastName]
  stat = input("Enter the stat you want to check for " + used_player.fn + " " + used_player.ln + ": (Points, Rebounds, Assists, Steals): ")
  stat = stat.lower()
  if stat == "points":
    print(used_player.fn + " " + used_player.ln + " has " + str(used_player.pts) + " " + stat.capitalize() + ".")
  elif stat == "rebounds":
    print(used_player.fn + " " + used_player.ln + " has " + str(used_player.reb) + " " + stat.capitalize() + ".")
  elif stat == "assists":
    print(used_player.fn + " " + used_player.ln + " has " + str(used_player.assist) + " " + stat.capitalize() + ".")
  elif stat == "steals":
    print(used_player.fn + " " + used_player.ln + " has " + str(used_player.steal) + " " + stat.capitalize() + ".")
  else:
    print("The stat you entered is not valid.")