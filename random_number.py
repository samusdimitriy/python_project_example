import random


def get_random_number():
    return random.randrange(1, 1000)

if __name__ == "__main__":
    res = get_random_number()
    print(res)

    def text_scope():
        print("asd")