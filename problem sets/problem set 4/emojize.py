import emoji

text = input("Input: ")

result = emoji.emojize(text, language="alias")

print("Output:", result)