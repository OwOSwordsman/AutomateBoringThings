def main():
    string = input("Enter string: ")
    charCt = dict()
    for char in string.upper():
        charCt.setdefault(char, 0)
        charCt[char] += 1
    for i, j in charCt.items():
        print(i, ':', j)


if __name__ == '__main__':
    main()
