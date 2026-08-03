def menu(choices):
    while True:
        text = input(f'Choose ({choices}): ').strip()
    
        if text in choices:
            return text
    
        print(f'{text} is not valid; try again')