def isPanlindrome(src):
    if len(src) == 0:
        return True
    src = src.lower()
    print(src)
    src_li = list(src)
    result_li = []
    for c in src_li:
        if c.isalpha():
            result_li.append(c)
    print(result_li)

    return result_li == result_li[::-1]


li = list('src')
print(type(li[0]))
help(str)
print(isPanlindrome('A d..@#$%@ dA'))
