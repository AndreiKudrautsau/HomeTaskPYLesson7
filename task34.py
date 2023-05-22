# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке

def rithm (lst):
    word_lst = lst.split()
    rslt = []
    for word in word_lst:
        count = 0
        for i in word:
            if i in 'ауеыоэяию':
                count +=1
        rslt.append(count)
    return len(set(rslt))

phrase = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

if rithm(phrase) == 1:
    print ("Парам пам-пам")
else:
    print ("Пам парам")

    
