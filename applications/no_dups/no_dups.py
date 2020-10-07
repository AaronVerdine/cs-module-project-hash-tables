def no_dups(s):
    # Your code here
    used_words = set()
    result = ''
    words = s.split()
    for word in words:
        if word not in used_words:
            result += word + ' '
            used_words.add(word)

    if result.endswith(' '):
        result = result[:-1]
    return result


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))