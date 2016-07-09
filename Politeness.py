def wellness():
	x = False
	while x == False:
		y = input('How are you?\n==>').lower()
		if y == 'well' or y == 'good' or y == 'alright'or y == 'ok' or y == 'okay':
			print('That\'s good :).')
			x = True
		elif y == 'meh' or y == 'so so':
			print('That bad, huh? ;)') 
			x = True
		elif y == 'bad' or y == 'shit' or y == 'crap':
			('That\'s no good :(')
			x = True
		else:
			print('Huh?')
		


