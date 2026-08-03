if __name__ == '__main__':
    print(f'Hello, and welcome to {__name__}!')   # only print when run directly, not when imported

x = 100

y = [10, 20, 30]

def hello(name):
    return f'Hello, {name}, from mymod!'

if __name__ == '__main__':
    # from here and down, the code only runs when the program is run directly
    # this will never run when the program/module is imported.
    print(f'Goodbye -- thanks for visiting {__name__}!')
