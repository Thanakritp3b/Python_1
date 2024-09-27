text = input()
key = input()

half_text_len = (len(text)) // 2 

new_text = text[0:half_text_len] + key + text[half_text_len:]
print(new_text)