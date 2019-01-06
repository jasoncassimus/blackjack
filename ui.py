cin = ''
def prompt(message):
    print("> " + message)

def read_input(message):
    prompt(message)
    return(input())

cin = read_input('enter an input')
prompt(cin)
