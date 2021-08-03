import webbrowser, sys, pyperclip as pc

def main():
    # check for cmd args
    if len(sys.argv) > 1:   # args exist
        address = ' '.join(sys.argv[1:])
    else:   # args do not exist
        address = pc.paste()

    webbrowser.open(f'https://www.google.com/maps/place/{address}')

if __name__ == '__main__':
    main()
