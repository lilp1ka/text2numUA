
numdict = {
    'нуль':'0','один':'1','два':'2','три':'3','чотири':'4',"п'ять":'5',
    'шість':'6','сім':'7','вісім':'8',"дев'ять":'9','десять':'10',
    'одинадцять':'11','дванадцять':'12','тринадцять':'13','чотирнадцять':'14',"п'ятнадцять":'15',
    'шістнадцять':'16','сімнадцять':'17','вісімнадцять':'18',"дев'ятнадцять":'19',
    'двадцять':'20','тридцять':'30','сорок':'40',"п'ятдесят":'50',
    'шістдесят':'60','сімдесят':'70','вісімдесят':'80',"дев'яносто":'90',
    'сто':'100','двісті':'200','триста':'300','чотириста':'400',"п'ятсот":'500','шістсот':'600','сімсот':'700','вісімсот':'800',
    "дев'ятсот":'900',
    'тисяча':'1000','тисяч':'*1000','мільйон':'1000000','мільйонів':'*1000000',
    'мільярд':'1000000000','мільярдів':'*1000000000'
}
def text2num(sentence):
    """
    закоментуйте лініку №43 якщо вам потрібна тільки конвертація
    
    Args:
        sentence <class 'str'>: число в текстовому форматі

    Returns:
        <class 'int'>: повертає число в форматі 'int'
    """

    """"""
    intsentencelist = []
    sentence = sentence.split()
    for i in sentence:
        [intsentencelist.append(value) for key,value in numdict.items() if i==key]

    prime = 0
    for index,value in enumerate(intsentencelist):
        if '*' in value:
            intsentencelist[index] = value.replace(value,f'){value}(')
            prime = 1
    try:            
        if intsentencelist[0] != '(' and prime == 1:
            intsentencelist.insert(0,'(')
        if intsentencelist[-1] != ')' and prime == 1:
            intsentencelist.append(')')  
    except IndexError:
        print('Такого слова не існує,спробуйте будь ласка ще раз.')
        run() #видаліть цю лінійку якщо використовуєте цю функцію в свому коді через import 
    
    intsentencestr = '+'.join(intsentencelist)
    intsentencestr = intsentencestr.replace('(+)','')
    intsentencestr = intsentencestr.replace('(+','+(')
    intsentencestr = intsentencestr.replace('+)',')')
    print(intsentencestr)
    print(eval(intsentencestr))
    return eval(intsentencestr)

def run():
    p = True    
    while p:
        sentence = input("Щоб вийти напишіть натисніть Ctrl + C.\nВведіть будь ласка текст: ")
        if p == 'вихід':
            quit
        else:
            text2num(sentence)
            
run()