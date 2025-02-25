import yadisk
import os

token = os.environ["YADISK_TOKEN"]

y = yadisk.YaDisk(token=token)

def info_10():
    try:
        y.publish('/10 класс/10 информатика.pdf')
        url = y.get_meta('/10 класс/10 информатика.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def info_11():
    try:
        y.publish('/11 класс/11 информатика.pdf')
        url = y.get_meta('/11 класс/11 информатика.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def english_10():
    try:
        y.publish('/10 класс/10 английский.pdf')
        url = y.get_meta('/10 класс/10 английский.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def english_11():
    try:
        y.publish('/11 класс/11 английский.pdf')
        url = y.get_meta('/11 класс/11 английский.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"

def social_10():
    try:
        y.publish('/10 класс/10 общество.pdf')
        url = y.get_meta('/10 класс/10 общество.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def social_11():
    try:
        y.publish('/11 класс/11 общество.pdf')
        url = y.get_meta('/11 класс/11 общество.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def physics_10():
    try:
        y.publish('/10 класс/10 физика.pdf')
        url = y.get_meta('/10 класс/10 физика.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def physics_11():
    try:
        y.publish('/11 класс/11 физика.pdf')
        url = y.get_meta('/11 класс/11 физика.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def chemistry_10():
    try:
        y.publish('/10 класс/10 химия.pdf')
        url = y.get_meta('/10 класс/10 химия.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def chemistry_11():
    try:
        y.publish('/11 класс/11 химия.pdf')
        url = y.get_meta('/11 класс/11 химия.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def algebra():
    try:
        y.publish('/общие/алгебра.pdf')
        url = y.get_meta('/общие/алгебра.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def biology():
    try:
        y.publish('/общие/биология.pdf')
        url = y.get_meta('/общие/биология.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def geog():
    try:
        y.publish('/общие/география.pdf')
        url = y.get_meta('/общие/география.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def geom():
    try:
        y.publish('/общие/геометрия.pdf')
        url = y.get_meta('/общие/геометрия.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def russian():
    try:
        y.publish('/общие/русский.pdf')
        url = y.get_meta('/общие/русский.pdf').public_url
        text = url
    except Exception as ex:
        text = "еррор 404"
    return text

def get_all_books():
    s = y.get_files()
    msg = 'Все учебники в каталоге:\n\n'
    for elem in s:
        msg = msg + elem.name + '\n\n'
    return msg