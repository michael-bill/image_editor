import numpy as np
import cv2
from PIL import Image
np.seterr(invalid='ignore')

def get_ndarray_from_image(path: str):
    """Возвращает numpy массив для дальнейшей обработки изображения

    Args:
        path (srt): Путь к файлу

    Returns:
        numpy.ndarray: Изображение в формате numpy массива
    """
    image = Image.open(path)
    array = np.asarray(image).copy()
    array.setflags(write=True)
    return array

def save_image_from_ndarray(image: np.ndarray, path: str):
    """Сохраняет изображение в png формате из numpy массива

    Args:
        image (numpy.ndarray): Изображение в формате numpy массива
        path (str): Путь для сохранения файла
    """
    res = Image.fromarray(image)
    res.save(path, format=='png')

def resize(image: np.ndarray, x: int, y: int):
    """Делает ресайз изображения

    Args:
        image (numpy.ndarray): Изображение в формате numpy массива
        x (int): ширина в пикселях
        y (int): высота в пикселях

    Returns:
        numpy.ndarray: Измененное изображение в формате numpy массива
    """
    return cv2.resize(image, dsize=(x, y), interpolation=cv2.INTER_LINEAR)

def light_alignment(image: np.ndarray):
    """Выравнивает освещение на изображении

    Args:
        image (numpy.ndarray): Изображение в формате numpy массива

    Returns:
        numpy.ndarray: Измененное изображение в формате numpy массива
    """
    light_map = None
    if image.shape[2] == 4:
        light_map = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)
        light_map = cv2.cvtColor(light_map, cv2.COLOR_GRAY2RGBA)
    else:
        light_map = cv2.cvtColor(light_map, cv2.COLOR_RGB2GRAY)
        light_map = cv2.cvtColor(light_map, cv2.COLOR_GRAY2RGB)
    light_map = cv2.GaussianBlur(light_map, (399, 399), 0)
    avg = sum(np.mean(np.mean(image, axis=1), axis=0)[:-1]) / 3
    res = np.divide(image, light_map, dtype=np.float64) * avg
    res = np.where(res > 255, 255, res)
    res = res.astype(np.uint8)
    if image.shape[2] == 4:
        res[:,:,3] = image[:,:,3]
    return res

def threshold_binarization(image: np.ndarray):
    """Бинаризация по Трешолду изображения

    Args:
        image (numpy.ndarray): Изображение в формате numpy массива

    Returns:
        numpy.ndarray: Измененное изображение в формате numpy массива
    """
    res = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    res = cv2.adaptiveThreshold(res, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                cv2.THRESH_BINARY, 11, 2)
    return res

def invert(image: np.ndarray):
    """Инвертирование изображения

    Args:
        image (numpy.ndarray): Изображение в формате numpy массива

    Returns:
        numpy.ndarray: Измененное изображение в формате numpy массива
    """
    res = None
    if (image.shape[2] == 4):
        res = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        res = cv2.bitwise_not(image)
        res[:,:,3] = image[:,:,3]
    else:
        res = cv2.bitwise_not(image)
    return res