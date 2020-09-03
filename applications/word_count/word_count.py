def word_count(s):
    # Your code here
    count_words =  {}
    words = s.split()
    for w in words:
        word = w.lower().strip('":;,.-+=/\|[]{}()*^&')
        
        if len(word) == 0:
            continue

        count = count_words.get(word)
        if count is None:
             count_words[word] = 1
        else:
            count_words[word] = count+1

    return count_words




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))