из  математического  импорта  sqrt

#номер 1
a  =  int ( input ( "Введите число А:" ))
b  =  int ( input ( "Введите число В:" ))
если  а  !=  б :
    а знак  равно  б знак  равно  максимум ( а , б )
еще :
    а  =  б  =  0
напечатать ( "А=" , а , "В=" , б )


#номер 2
a  =  int ( input ( "Введите число А:" ))
b  =  int ( input ( "Введите число В:" ))
c  =  int ( input ( "Введите число С:" ))
print ( "Сумма двух многочисленных чисел a, b, c:" , a  +  b  +  c  -  min ( a , b , c ))


# номер 3
x1  =  int ( input ( "Координата X точки А:" ))
y1  =  int ( input ( "Координата точки зрения А:" ))
x2  =  int ( input ( "Координата X точки В:" ))
y2  =  int ( input ( "Координата с точки зрения В:" ))
x3  =  int ( input ( "Координата X точки С:" ))
y3  =  int ( input ( "Координата точки зрения С:" ))
rast1  =  sqrt (( x2  -  x1 ) ** 2  + ( y2  -  y1 ) ** 2 )
rast2  =  sqrt (( x3  -  x1 ) ** 2  + ( y3  -  y1 ) ** 2 )
если  раст1  <  раст2 :
    print ( "Точка В расположении ближе к А, и ее расстояние до А:" , rast1 )
 Элиф  раст2 <  раст1 :
    print ( "Точка С расположена ближе к А, и ее расстояние до А:" , rast2 )
еще :
    print ( "Точки В и С считаются особо близкими к восприятию А, их расстоянием до А:" , rast1 )


#номер 4
x  =  int ( input ( "Координата X:" ))
y  =  int ( input ( "Координата У:" ))
если  х  >  0 :
    если  у  >  0 :
        print ( "Точка (" , x , "," , y , ") лежит в 1 координатной четверти." )
    еще :
        print ( "Точка (" , x , "," , y , ") лежит в 4 координатной четверти." )
еще :
    если  у  >  0 :
        print ( "Точка (" , x , "," , y , ") лежит в 2 координатной четверти." )
    еще :
        print ( "Точка (" , x , "," , y , ") лежит в 3 координатной четверти." )


#номер 5
a  =  int ( ввод ( "Введите число" ))
если  а  ==  0 :
    печать ( "Нулевое число" )
Элиф  а  %  2  ==  0 :
    если  а  >  0 :
        print ( "Положительное четное число" )
    еще :
        print ( "Отрицательное четное число" )
еще :
    если  а  >  0 :
        print ( "Положительное нечетное число" )
    еще :
        print ( "Отрицательное нечетное число" )


#номер 6
a  =  int ( ввод ( "Введите число" ))
если  а  !=  0 :
    если  а  >=  100 :
        har2  =  "Трехзначное"
    Элиф ( а  <  100 ) и ( а  >=  10 ):
        har2  =  "Двузначное"
    еще :
        har2  =  "Однозначное"
    если  % 2 == 0 : _    
        har1  =  "Четное"
    еще :
        har1  =  "Нечетное"
    print ( a , "-" , har1 , har2 , "число" )