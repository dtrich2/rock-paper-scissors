import dennis
import raman
import helper

def rps_compete(n_games, bot_1, bot_2):
	bot_1_wins=0
	bot_2_wins=0
	for _ in range(n_games):
		hand_1=bot_1.play()
		hand_2=bot_2.play()
		win_1, win_2=helper.rps_decide(hand_1, hand_2) #returns the result of hand_1: 'win', 'lose', 'tie'
		print(f"{hand_1},{hand_2},{win_1},{win_2}")
		bot_1.update(hand_1,hand_2,win_1)
		bot_2.update(hand_2,hand_1,win_2)
		if win_1=='win':
			bot_1_wins+=1
		elif win_2=='win':
			bot_2_wins+=1
	print(f"""{bot_1.name} wins {100*bot_1_wins/n_games}% of games.
{bot_2.name} wins {100*bot_2_wins/n_games}% of games.""")
	if bot_1_wins>bot_2_wins:
		return True
	elif bot_2_wins>bot_1_wins:
		return False
	else:
		print("Playing again.")
		return rps_compete(n_games,bot_1,bot_2)

if __name__=="__main__":
	bot_1=dennis.bot_class()
	bot_2=raman.bot_class()
	rps_compete(10,bot_1,bot_2)
