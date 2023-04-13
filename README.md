# image_editor
Программа способная выполнять некоторые преобразования над изображениями

img_examples - тестовые изображения, на которых можно проверить работу приложения<br/>
image_editor.py - модуль преобработки, фильтрации и улучшений изображений<br/>
main.py - простой консольный интерпретатор для работы с модулем

Список доступных команд интерпретатора:

open {path}: Указать путь к изображению для преобразований. (в png, jpg/jpeg форматах)<br/>
save {path}: Указать путь для сохранения измененного изображения. (в png формате)<br/>
resize {x} {y}: Ресайз изображения (x - ширина, y - высота в пикселях)<br/>
light_alignment: Выравнивание изображения<br/>
threshold_binarization: Бинаризация по Трешолду изображения<br/>
invert: Инвертирование изображения<br/>
exit: Выход
