from keyword import kwlist, softlist

def keywords()->None:
    print("keywords: ")
    for i, kw in enumerate(kwlist, start=1):
        print(f'{i:2} :{kw}')

    print('soft keywords: ')
    for i, skw in enumerate(softlist, start=1):
        print(f'{i:2} : {skw}')

def main()-> None:
    keywords()

if __name__ == '__main__':
    main()
    