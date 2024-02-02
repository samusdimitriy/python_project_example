import sys

def say_hello(name):
    print(f'Привет, {name}')

def main():
    print("Вы импортировали hello.py")
    say_hello('пользователь')

if __name__ == '__main__':
    main()