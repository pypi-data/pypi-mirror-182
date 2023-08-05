# matreshka


Matresha - программа распаковывает *tar.gz архив вложенный как матрешка.




## Старт
Установка
```angular2html
pip install matreshka
```
Удаление пакета
```angular2html
pip uninstall matreshka
```

#  Работа с пакетом

### Подключение 
```angular2html
import matreshka as mt
```


## Шаблон для архива
Принцип в том, что каждый архив внутри следующего, имеет свой номер и этот 
шаблон может быть любым, лишь число ведущих нулей может быть разным.

* %(number)0<здесь количество нулей>d.tar.gz - не изменяемая часть шаблона.

#### Шаблон архива

```angular2html
archive-%(number)03d.tar.gz
```
#### Имя архива
Всегда начинается отсчет с 1 не с нуля.
```angular2html
archive-001.tar.gz
```

### Использование
 100 - глубина вложенности, на ваше усмотрение. Файл архива должен лежать в 
 той же директории, где и код mt.py.

Скопируйте код в файл mt.py
```
from matreshka import bum

tmp = 'archive-%(number)03d.tar.gz'
bum(tmp, 100)
```

##### Запуск из консоли
```angular2html
python3 mt.py
```
