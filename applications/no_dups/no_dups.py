def no_dups(s):
    # Your code here

    map = {}
    new_str = ''
    for word in s.split():
        count =  map.get(word)
        if count is None:
            map[word]  = 1

            #append space when itsnot the first word
            if len(new_str) > 0:
                new_str += ' '

            new_str += word
    
    return new_str
        

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))