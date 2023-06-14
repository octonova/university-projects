def soundex(w):
    subst_dict = {1:['a','b','p','v'], 2:['c','g','j','k','q','s','x','z'],
                  3:['d','t'], 4:['l'], 5:['m','n'], 6:['r']}
    code_to_return = w[0]
    for letter in w[1:]:
        for number, code_letters in subst_dict.items():
            if str(number) != code_to_return[-1] and letter.lower() in code_letters:
                code_to_return += str(number)
    if len(code_to_return) >= 4:
        return code_to_return[:4]
    else:
        return code_to_return + '0'*(4 - len(code_to_return))


word = input()
print(soundex(word))