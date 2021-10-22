dict = {"apple":"qua tao", "orange":"qua cam", "dog": "con cho", "cat":"con meo", "lion":"sư tử", "table":"cai ban"}

def input_word(text):
    return input(text)

def is_in_dict(text, dict):
    for key in dict:
        if key == text:
            return True
            break
    else:
        return False

if __name__ == '__main__':
    word = input_word("Enter the word to be translated into Vietnamese: ").lower()
    if is_in_dict(word, dict):
        print(f"'{word}' : '{dict[word]}'")
    else:
        print(f"'{word}' is not in English dictionary")