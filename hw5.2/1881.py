h, w, n = map(int, input().split())

pages = 0
strings = 1 # число строк в тексте
characters_in_strings = 0 # число символов в строке

for i in range(n):
    word = len(input()) #длина введённого слова
    if characters_in_strings == 0:
        characters_in_strings = word
    else:
        if characters_in_strings + word + 1 <= w: # добавление слова к строке с учётом пробела
            characters_in_strings += word + 1
        else:
            characters_in_strings = word
            strings+=1
    

pages = (strings // h) if (strings / h) == int(strings / h) else (strings // h) + 1

print(pages)