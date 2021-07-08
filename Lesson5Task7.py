#lesson5Task7


from json import dump

with open('firma.txt','r', encoding='utf-8') as read_file:
    with open('firma_c.json', 'w', encoding='utf-8') as write_file:
        dictionary = {string.split()[0]: int(string.split()[2])-int(string.split()[3])for string in read_file}
        average_profit_list = []
        for n in dictionary.values():
            if n >0:
              average_profit_list.append(n)
        dump([dictionary, {'average_profit': sum(average_profit_list)/ len(average_profit_list)}], write_file, ensure_ascii=False, indent=4)