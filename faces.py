def main():
    text = input("")
    print(convert(text))

def convert(a):
    return a.replace(":)", '🙂').replace(":(", '🙁')

main()