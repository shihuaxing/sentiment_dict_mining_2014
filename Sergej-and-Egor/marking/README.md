####delete_neg.py
Скрипт принимает на вход:
* Имя файла с положительными словами
* Имя файла с отрицательными словами 
* Имя файла с нейтральными словами
На выходе получается 3 файла, так же с положительными, отрицательными и нейтральными словами, которые получились удалением приставки "не" из исходных слов (с учётом грамматической правильности результата).
Пример: слово "нехороший" было в файле с отрицательными словами, а на выходе, в файле с положительными словами будет слово "хороший" вместо него.
###marker.py
Скрипт для разметки новых слов в ручную.
###splitfile.py
Скрипт, который разбивает файл, каждая строка в котором: [слово] [+ or - or 0] разбивает на три файла, в одном все слова, справа от которых был "+" итп.