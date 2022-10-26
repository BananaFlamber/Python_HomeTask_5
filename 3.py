print("\033c")

text = "Однажды в студёную абвзимнюю пору я из лесу вышел абвалку был сильный абвал мороз. "
print(text)
del_set = "абв"

print(str(" ".join(filter(lambda word: del_set not in word, text.split()))))
