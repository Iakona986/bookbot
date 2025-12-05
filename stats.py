def wordcount(content):
    text = content
    words = text.split()
    count = len(words)
    return count

def sort_on(d):
    return d["num"]

def letter_count(content):
    text = content
    low_text = text.lower()
    letter_count = {}
    for c in low_text:
        letter_count[c] = letter_count.setdefault(c, 0)+1

    return letter_count

def sorted_count(letter_count):
    final_list = []
    for char, count in letter_count.items():
        if char.isalpha():
            final_list.append({
                "char": char,
                "num": count
            })

    final_list.sort(reverse=True, key=sort_on)
    #print (final_list)
    return final_list
