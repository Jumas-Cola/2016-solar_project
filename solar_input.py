# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
import math


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line.strip()[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    R, color, m, x, y, Vx, Vy = line.split()[1:]
    star.R = int(R)
    star.color = color
    star.m = float(m)
    star.x = float(x)
    star.y = float(y)
    star.Vx = float(Vx)
    star.Vy = float(Vy)


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    R, color, m, x, y, Vx, Vy = line.split()[1:]
    planet.R = int(R)
    planet.color = color
    planet.m = float(m)
    planet.x = float(x)
    planet.y = float(y)
    planet.Vx = float(Vx)
    planet.Vy = float(Vy)


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write('{0} {1:d} {2} {3:E} {4:E} {5:E} {6:E} {7:E}\n'.format(
                obj.type.capitalize(),
                obj.R,
                obj.color,
                obj.m,
                obj.x,
                obj.y,
                obj.Vx,
                obj.Vy
            ))

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...
def write_space_object_stat_to_file(t, obj, another_obj=None, output_filename='stat.txt'):
    Vabs = math.hypot(obj.Vx, obj.Vy)
    with open(output_filename, 'a') as out_file:
        if another_obj:
            dist = math.hypot(obj.x - another_obj.x, obj.y - another_obj.y)
            out_file.write('{0},{1},{2},{3},{4}\n'.format(id(obj), obj.type, t, Vabs, dist))
        else:
            out_file.write('{0},{1},{2},{3}\n'.format(id(obj), obj.type, t, Vabs))





if __name__ == "__main__":
    print("This module is not for direct call!")
