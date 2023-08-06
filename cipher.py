text = input("Please enter a sentence:")
text = text.lower()
cyphered_text = text

dictionary = {
"a": "f",
"b": "g",
"c": "h",
"d": "i",
"e": "j",
"f": "k",
"g": "l",
"h": "m",
"i": "n",
"j": "o",
"k": "p",
"l": "q",
"m": "r",
"n": "s",
"o": "t",
"p": "u",
"q": "v",
"r": "w",
"s": "x",
"t": "y",
"u": "z",
"v": "a",
"w": "b",
"x": "c",
"y": "d",
"z": "e"
}

for i in text:
    if i in dictionary:
        cyphered_text = cyphered_text.replace(i, dictionary[i].upper()) #Temporarily changing the cyphered letter to uppercase so the loop won't rediscover the same letter multiple times

cyphered_text = cyphered_text.lower()
print(f"The encrypted sentence is: {cyphered_text}")