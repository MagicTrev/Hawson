def wellness():
    y = input('How are you?\n==>').lower()
    if y == 'well' or y == 'good' or y == 'alright'or y == 'ok' or y == 'okay':
        print('That\'s good :).')
    elif y == 'meh' or y == 'so so':
        print('That bad, huh? ;)') 
    elif y == 'bad' or y == 'shit' or y == 'crap':
        print('That\'s no good :(')
    else:
        print('Huh?\n==>')

wellness()
