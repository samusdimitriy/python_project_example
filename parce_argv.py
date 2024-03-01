import sys


def parse_args():
    args_list = sys.argv[1:]
    args_str = ' '.join(args_list) 
        
    return args_str

print(parse_args())

s = 'Some words'
print(s.find('o'))