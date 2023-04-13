from image_editor import *

def image_editor_help():
    print("Список доступных команд:")
    print("""
    open {path}: Указать путь к изображению для преобразований. (в png, jpg/jpeg форматах)
    save {path}: Указать путь для сохранения измененного изображения. (в png формате)
    resize {x} {y}: Ресайз изображения (x - ширина, y - высота в пикселях)
    light_alignment: Выравнивание изображения
    threshold_binarization: Бинаризация по Трешолду изображения
    invert: Инвертирование изображения
    exit: Выход
    """)

command = ''
path = ''
output_path = ''
image = None


print('Напишите "help" для просмотра доступных команд.')
while command != 'exit':
    command = input('> ').strip()
    if command.strip() == '': continue
    s_command = command.split()
    if command == 'help': image_editor_help()
    elif s_command[0] == 'open':
        try:
            image = get_ndarray_from_image(s_command[1])
        except Exception as ex:
            print("Ошибка при загрузке файла.")
            print(ex)
    elif s_command[0] == 'save':
        try:
            if len(s_command[1]) > 0:
                save_image_from_ndarray(image, s_command[1])
            else:
                print("Укажите путь для сохранения файла командой set_path {path}")
        except Exception as ex:
            print("Ошибка при сохранении файла. Проверьте путь и попробуйте еще раз.")
            print(ex)
    elif s_command[0] == 'resize':
        try:
            x, y = map(int, s_command[1:])
            image = resize(image, x, y)
        except  Exception as ex:
            print("Ошибка при ресайзе, проверите вернно ли вы ввели числовые значения и попробуйте еще раз.")
            print(ex)
    elif command == 'light_alignment':
        try:
            image = light_alignment(image)
        except Exception as ex:
            print("Ошибка при выравнивании освещения.")
            print(ex)
    elif command == 'threshold_binarization':
        try:
            image = threshold_binarization(image)
        except Exception as ex:
            print("Ошибка при бинаризации Трешолдом файла.")
            print(ex)
    elif command == 'invert':
        try:
            image = invert(image)
        except Exception as ex:
            print("Ошибка при инвертировании изображения.")
            print(ex)
    elif command == 'exit':
        exit()
    else:
        print("Команда " + command + " мне неизвестна.")
        print('Напишите "help" для просмотра доступных команд.')