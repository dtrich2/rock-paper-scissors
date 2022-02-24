def rps_decide(hand_1,hand_2):
	if hand_1 == hand_2:
		return ('tie','tie')
	elif hand_1 == "rock":
		if hand_2 == "scissors":
			return ('win','lose')
		else:
			return ('lose','win')
	elif hand_1 == "paper":
		if hand_2 == "rock":
			return ('win','lose')
		else:
			return ('lose','win')
	elif hand_1 == "scissors":
		if hand_2 == "paper":
			return ('win','lose')
		else:
			return ('lose','win')
