#номер 1
edinici  = [ "первое" , "второе" , "третье" , "четвертое" , "пятое" , "шестое" , "седьмое" , "восьмое" , "девятое" ]
desyatki  = [ "десятое" , "одиннадцатое" , "двенадцатое" , "тринадцатое" , "четврнадцатое" , "пятнадцатое" , "шестнадцатое" , "семнадцатое" , "восемнадцатое" , "девятнадцатое" , "двадцатое" ]
больше  = [ "двадцать" , "тридцать" ]
mesyac  = [ "января" , "февраля" , "марта" , "апреля" , "мая" , "июня" , "июля" , "августа" , "сентября" , "октября" , "ноября" , "декабря" ]
vvod1  =  интервал ( ввод ())
vvod2  =  интервал ( ввод ())

если  vvod1  <  10 :
    печать ( единицы [ ввод1 - 1 ], месяц [ ввод2 - 1 ])    
elif ( vvod1  >=  10 ) и ( vvod1  <=  20 ):
    печать ( десятки [ ввод1 - 10 ], месяц [ ввод2 - 1 ])    
еще :
    print ( больше [ ввод1 // 10 - 2 ], единички [ ввод1 % 10 - 1 ], месяц [ ввод2 - 1 ])          


#номер 2
напр  =  0
stor  = [ "С" , "В" , "Ю" , "З" , "С" , "З" ]
vvod1  =  ввод ()
если  vvod1  ==  "С" :
    напр  =  0
 Элиф vvod1  == "  В" :
    напр  =  1
 Элиф vvod1  == "  Ю" :
    напр  =  2
еще :
    напр  =  3
vvod2  =  интервал ( ввод ())
если  vvod2  ==  0 :
    печать ( vvod1 )
 Элиф  vvod2 ==  1 :
    печать ( стор [ напр  -  1 ])
 Элиф  vvod2 ==  - 1 :
    печать ( хранить [ напр  +  1 ])


# номер 3
варианты  = [ "учебное задание" , "учебных заданий" , "учебных заданий" ]
odin  = [ "одно" , "два" , "три" , "четыре" , "пять" , "шесть" , "семь" , "восемь" , "девять" ]
два  = [ "десять" , "одиннадцать" , "двенадцать" , "тринадцать" , "четырнадцать" , "пятнадцать" , "шестнадцать" , "семнадцать" , "восемнадцать" , "девятнадцать" , "двадцать" ]
tri  = [ "десять" , "двадцать" , "тридцать" , "сорок" ]
ввод  =  целое ( ввод ())
если  ввод  ==  1 :
    печать ( один [ ввод  -  1 ], варианты [ 0 ])
 Элиф  vvod >  1  и  vvod  <  5 :
    печать ( один [ ввод  -  1 ], варианты [ 1 ])
elif  vvod  >=  5  и  vvod  <  10 :
    печать ( один [ ввод  -  1 ], варианты [ 2 ])
 Элиф vvod  > =  10  и  vvod  <=  20 :
    печать ( два [ ввод  -  10 ], варианты [ 2 ])
elif  vvod  ==  20  или  vvod  ==  30  или  vvod  ==  40 :
    print ( tri [ ввод  //  10  -  1 ], варианты [ 2 ])
 Элиф  vvod ==  21  или  vvod  ==  31 :
    print ( tri [ ввод  //  10  -  1 ], odin [ 0 ], варианты [ 0 ])
elif  vvod  >  21  и ( vvod  %  10  ==  2  или  vvod  %  10  ==  3  или  vvod  %  10  ==  4 ):
    print ( tri [ ввод  //  10-1  ]  , odin [ ввод % 10-1 ] , варианты [ 1 ] ) _    
еще :
    print ( tri [ ввод  //  10-1  ]  , odin [ ввод % 10-1 ] , варианты [ 2 ] ) _    


#номер 4
edinici  = [ "один" , "два" , "три" , "четыре" , "пять" , "шесть" , "семь" , "восемь" , "девять" ]
desyatki  = [ "десять" , "одиннадцать" , "двенадцать" , "тринадцать" , "четвродин" , "пятнадцать" , "шестнадцать" , "семнадцать" , "восемнадцать" , "девятнадцать" , "двадцать" ]
больше  = [ "двадцать" , "тридцать" , "сорок" , "пятьдесят" , "шестьдесят" , "семьдесят" , "водесятсемь" , "девяносто" ]
eshe_bolshe  = [ "сто" , "двести" , "триста" , "четыреста" , "пятьсот" , "шестьсот" , "семьсот" , "восемьсот" , "девятьсот" ]
ввод  =  целое ( ввод ())
если  ввод  %  100  ==  0 :
    print ( еше_больше [ ввод  //  100  -  1 ])
Элиф  вод  %  100  <  10 :
    print ( еше_больше [ ввод  //  100  -  1 ], единички [ ввод  %  10  -  1 ])
elif  vvod  %  100  >=  10  и  vvod  %  100  <  20 :
    print ( еше_больше [ ввод  //  100-1  ]  , десятки [ ввод % 10 ] )  
elif ( vvod  %  10 ) ==  0  и ( vvod  %  100 ) >  19 :
    print ( еше_больше [ ввод  //  100  -  1 ], больше [( ввод  //  10 ) %  10  -  2 ])
еще :
    print ( еше_больше [ ввод  //  100-1  ]  , больше [ ( ввод // 10 ) % 10-2 ] , единичи [ ввод % 10-1 ] ) _ _         


#номер 5
ввод  =  целое ( ввод ())
начало  =  1984
odin  = [ "зеленой" , "красной" , "желтой" , "белой" , "черной" ]
odin_tig  = [ "зеленого" , "красного" , "желтого " , "белого" , "черного" ]
два  = [ "крысы" , "коровы" , "тигра" , " зайца" , "дракона" , "змеи" , "лошади" , "овцы" , "обезьяны" , "курицы" , "собаки" , "свиньи" ]
raznica  =  ввод  -  начало
если (( разница  %  60 ) %  12 ) ==  2  или (( разница  %  60 ) %  12 ) ==  3  или (( разница  %  60 ) %  12 ) ==  4 :
    print ( "Год" , odin_tig [(( разница  %  60 ) //  12 )], два [(( разница  %  60 ) %  12 )])
еще :
    print ( "Год" , odin [(( разница  %  60 ) //  12 )], два [(( разница  %  60 ) %  12 )])