class bot_class:
	def __init__(self):
		self.name='Dennis'
		self.game_counter=0

	def play(self):
		if self.game_counter>10:
			return 'rock'
		else:
			return 'paper'

	def update(self,my_hand,opponent_hand,result):
		self.game_counter+=1
