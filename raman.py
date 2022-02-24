class bot_class:
	def __init__(self):
		self.name='Raman'
		self.game_counter=0

	def play(self):
		if self.game_counter>20:
			return 'scissors'
		else:
			return 'paper'

	def update(self,my_hand,opponent_hand,result):
		self.game_counter+=1
