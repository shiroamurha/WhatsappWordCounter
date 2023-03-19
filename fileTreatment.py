import json
import pandas



def main():
    file = open('chat.txt', 'r', encoding='utf-8').read()

    messages_list = file.split('\n')

    for message in range(0, len(messages_list)): 

        double_dot_is_at = messages_list[message].find(':', 19) + 2
        messages_list[message] = messages_list[message][double_dot_is_at:]

        if messages_list[message] == '<Arquivo de mídia oculto>':
            messages_list[message] = ''

    msg_big_str = str(' ').join(messages_list)
    
    global wordlist
    wordlist = msg_big_str.split(' ')

    words_frequency = dict()
    for word in wordlist:

        if words_frequency.get(word) is not None:
            words_frequency[word] += 1
        else:
            words_frequency[word] = 1
    del words_frequency[""]
    sorted_frequencies = list(words_frequency.values())
    sorted_frequencies.sort(reverse=True)

    global sorted_words_frequency
    sorted_words_frequency = dict()

    for frequency in sorted_frequencies:
        for key, value in words_frequency.items():
            if value == frequency:
                sorted_words_frequency[key] = frequency

def dump_frequency():
    json.dump(
        sorted_words_frequency, 
        open('words_frequency.json', 'w', encoding='utf-8'), 
        indent=4,
        ensure_ascii=False
    )

def dump_chat():
    json.dump(
        wordlist, 
        open('handled_chat.json', 'w', encoding='utf-8'), 
        indent=4,
        ensure_ascii=False
    )

def dump_to_xlsx():

    word_dict = json.load(open('words_frequency.json', encoding='utf-8'))

    keys = []
    values = []

    for key, value in word_dict.items():
        keys.append(key)
        values.append(value)

    final_dict = {
        'Palavras': keys,
        'Frequência': values
    }

    frame = pandas.DataFrame(final_dict)
    frame.to_excel('words_frequency.xlsx', index=False, encoding='utf-8')


if __name__ == '__main__':
    main()
    dump_chat()
    dump_frequency()
    dump_to_xlsx()
