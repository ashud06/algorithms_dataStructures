def func1(word):
    i=0
    j=0
    length=len(word)
    print(i)
    print(j)
    print(word)
    i+=length
    j+=length
    yield (i,j)
    print('coming back to yield')
    print(i)
    print(j)


def func2(words):
    if len(words)==0:
        return
    word=words.pop()
    for dir in func1(word):
        print(dir)
        func2(words)


words=['india','pakistan','nepali']
func2(words)