def menu(choices):
    while True:
        text = input(f'Choose ({choices}): ').strip()
    
        if text in choices:
            return text
    
        print(f'{text} is not valid; try again')

if __name__ == '__main__':    # only ask interactively if we're not being imported
    s = menu(['apple', 'peach', 'strawberry'])
    print(f'User chose "{s}".')
