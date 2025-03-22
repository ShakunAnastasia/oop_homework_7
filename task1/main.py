import math


class Figure:
    def dimention(self):
        raise NotImplementedError("Метод dimention() повинен бути реалізований у підкласі")

    def perimeter(self):
        raise NotImplementedError("Метод perimeter() повинен бути реалізований у підкласі")

    def square(self):
        raise NotImplementedError("Метод square() повинен бути реалізований у підкласі")

    def squareSurface(self):
        raise NotImplementedError("Метод squareSurface() повинен бути реалізований у підкласі")

    def squareBase(self):
        raise NotImplementedError("Метод squareBase() повинен бути реалізований у підкласі")

    def height(self):
        raise NotImplementedError("Метод height() повинен бути реалізований у підкласі")

    def volume(self):
        raise NotImplementedError("Метод volume() повинен бути реалізований у підкласі")


class TwoDimensional(Figure):
    def dimention(self):
        return 2

    def squareSurface(self):
        raise ValueError("Метод squareSurface() не підтримується для двовимірних фігур")

    def squareBase(self):
        raise ValueError("Метод squareBase() не підтримується для двовимірних фігур")

    def height(self):
        raise ValueError("Метод height() не підтримується для двовимірних фігур")

    def volume(self):
        return self.square()


class ThreeDimensional(Figure):
    def dimention(self):
        return 3

    def perimeter(self):
        raise ValueError("Метод perimeter() не підтримується для тривимірних фігур")

    def square(self):
        raise ValueError("Метод square() не підтримується для тривимірних фігур")


class Triangle(TwoDimensional):
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        if not self.is_valid():
            raise ValueError(f"Задані сторони не утворюють трикутник: {a}, {b}, {c}")

    def is_valid(self):
        return (self.a > 0 and self.b > 0 and self.c > 0 and
                self.a + self.b > self.c and
                self.b + self.c > self.a and
                self.a + self.c > self.b)

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def __str__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"


class Rectangle(TwoDimensional):
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
        if not self.is_valid():
            raise ValueError(f"Прямокутник з параметрами {a}, {b} не існує")

    def is_valid(self):
        return self.a > 0 and self.b > 0

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def __str__(self):
        return f"Rectangle({self.a}, {self.b})"


class Trapeze(TwoDimensional):
    def __init__(self, base1, base2, side1, side2):
        self.base1 = float(base1)
        self.base2 = float(base2)
        self.side1 = float(side1)
        self.side2 = float(side2)
        if not self.is_valid():
            raise ValueError(f"Трапеція з параметрами {base1}, {base2}, {side1}, {side2} не існує")

    def is_valid(self):
        if self.base1 <= 0 or self.base2 <= 0 or self.side1 <= 0 or self.side2 <= 0:
            return False
        if self.base1 == self.base2:
            return self.side1 == self.side2
        diff = abs(self.base2 - self.base1) / 2
        return self.side1 ** 2 - diff ** 2 >= 0 and self.side2 ** 2 - diff ** 2 >= 0

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def square(self):
        if self.base1 == self.base2:
            return self.base1 * self.side1
        diff = abs(self.base2 - self.base1) / 2
        height = math.sqrt(self.side1 ** 2 - diff ** 2)
        return (self.base1 + self.base2) * height / 2

    def __str__(self):
        return f"Trapeze({self.base1}, {self.base2}, {self.side1}, {self.side2})"


class Parallelogram(TwoDimensional):
    def __init__(self, a, b, height):
        self.a = float(a)
        self.b = float(b)
        self.height = float(height)
        if not self.is_valid():
            raise ValueError(f"Паралелограм з параметрами {a}, {b}, {height} не існує")

    def is_valid(self):
        return self.a > 0 and self.b > 0 and self.height > 0

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.height

    def __str__(self):
        return f"Parallelogram({self.a}, {self.b}, {self.height})"


class Circle(TwoDimensional):
    def __init__(self, radius):
        self.radius = float(radius)
        if not self.is_valid():
            raise ValueError(f"Коло з радіусом {radius} не існує")

    def is_valid(self):
        return self.radius > 0

    def perimeter(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle({self.radius})"


class Ball(ThreeDimensional):
    def __init__(self, radius):
        self.radius = float(radius)
        if not self.is_valid():
            raise ValueError(f"Куля з радіусом {radius} не існує")

    def is_valid(self):
        return self.radius > 0

    def squareSurface(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    def __str__(self):
        return f"Ball({self.radius})"


class TriangularPyramid(ThreeDimensional):
    def __init__(self, base_side, height):
        self.base_side = float(base_side)
        self.height = float(height)
        if not self.is_valid():
            raise ValueError(f"Трикутна піраміда з параметрами {base_side}, {height} не існує")

    def is_valid(self):
        return self.base_side > 0 and self.height > 0

    def squareBase(self):
        return (math.sqrt(3) / 4) * self.base_side ** 2

    def squareSurface(self):
        base_area = self.squareBase()
        lateral_area = (3 / 2) * self.base_side * math.sqrt((self.base_side ** 2) / 4 + self.height ** 2)
        return base_area + lateral_area

    def volume(self):
        return (1 / 3) * self.squareBase() * self.height

    def __str__(self):
        return f"TriangularPyramid({self.base_side}, {self.height})"


class QuadrangularPyramid(ThreeDimensional):
    def __init__(self, base_a, base_b, height):
        self.base_a = float(base_a)
        self.base_b = float(base_b)
        self.height = float(height)
        if not self.is_valid():
            raise ValueError(f"Чотирикутна піраміда з параметрами {base_a}, {base_b}, {height} не існує")

    def is_valid(self):
        return self.base_a > 0 and self.base_b > 0 and self.height > 0

    def squareBase(self):
        return self.base_a * self.base_b

    def squareSurface(self):
        base_area = self.squareBase()
        lateral_area = (self.base_a * math.sqrt((self.base_b / 2) ** 2 + self.height ** 2) +
                        self.base_b * math.sqrt((self.base_a / 2) ** 2 + self.height ** 2))
        return base_area + lateral_area

    def volume(self):
        return (1 / 3) * self.squareBase() * self.height

    def __str__(self):
        return f"QuadrangularPyramid({self.base_a}, {self.base_b}, {self.height})"


class RectangularParallelepiped(ThreeDimensional):
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        if not self.is_valid():
            raise ValueError(f"Прямокутний паралелепіпед з параметрами {a}, {b}, {c} не існує")

    def is_valid(self):
        return self.a > 0 and self.b > 0 and self.c > 0

    def squareSurface(self):
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)

    def volume(self):
        return self.a * self.b * self.c

    def __str__(self):
        return f"RectangularParallelepiped({self.a}, {self.b}, {self.c})"


class Cone(ThreeDimensional):
    def __init__(self, radius, height):
        self.radius = float(radius)
        self.height = float(height)
        if not self.is_valid():
            raise ValueError(f"Конус з параметрами {radius}, {height} не існує")

    def is_valid(self):
        return self.radius > 0 and self.height > 0

    def squareSurface(self):
        slant_height = math.sqrt(self.radius ** 2 + self.height ** 2)
        return math.pi * self.radius * slant_height + math.pi * self.radius ** 2

    def volume(self):
        return (1 / 3) * math.pi * self.radius ** 2 * self.height

    def __str__(self):
        return f"Cone({self.radius}, {self.height})"


class TriangularPrism(ThreeDimensional):
    def __init__(self, a, b, c, height):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.height = float(height)
        if not self.is_valid():
            raise ValueError(f"Трикутна призма з параметрами {a}, {b}, {c}, {height} не існує")

    def is_valid(self):
        return (self.a > 0 and self.b > 0 and self.c > 0 and self.height > 0 and
                self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b)

    def squareBase(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def squareSurface(self):
        base_area = self.squareBase()
        lateral_area = (self.a + self.b + self.c) * self.height
        return 2 * base_area + lateral_area

    def volume(self):
        return self.squareBase() * self.height

    def __str__(self):
        return f"TriangularPrism({self.a}, {self.b}, {self.c}, {self.height})"


def read_shapes_from_file(filename):
    shapes = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split()
                if not parts:
                    continue
                shape_type = parts[0]
                try:
                    params = list(map(float, parts[1:]))
                    if shape_type == "Triangle" and len(params) == 3:
                        shapes.append(Triangle(*params))
                    elif shape_type == "Rectangle" and len(params) == 2:
                        shapes.append(Rectangle(*params))
                    elif shape_type == "Trapeze" and len(params) == 4:
                        shapes.append(Trapeze(*params))
                    elif shape_type == "Parallelogram" and len(params) == 3:
                        shapes.append(Parallelogram(*params))
                    elif shape_type == "Circle" and len(params) == 1:
                        shapes.append(Circle(*params))
                    elif shape_type == "Ball" and len(params) == 1:
                        shapes.append(Ball(*params))
                    elif shape_type == "TriangularPyramid" and len(params) == 2:
                        shapes.append(TriangularPyramid(*params))
                    elif shape_type == "QuadrangularPyramid" and len(params) == 3:
                        shapes.append(QuadrangularPyramid(*params))
                    elif shape_type == "RectangularParallelepiped" and len(params) == 3:
                        shapes.append(RectangularParallelepiped(*params))
                    elif shape_type == "Cone" and len(params) == 2:
                        shapes.append(Cone(*params))
                    elif shape_type == "TriangularPrism" and len(params) == 4:
                        shapes.append(TriangularPrism(*params))
                    else:
                        print(f"Невірна кількість параметрів або невідомий тип: {line.strip()}")
                except ValueError as ve:
                    print(f"Помилка у файлі {filename}: {ve}")
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено")
    return shapes


def find_max_measure(shapes):
    valid_shapes = [shape for shape in shapes if shape is not None]
    if not valid_shapes:
        return None
    return max(valid_shapes, key=lambda shape: shape.square() if shape.dimention() == 2 else shape.volume())


def main():
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    output_file = "output.txt"

    with open(output_file, 'w', encoding='utf-8'):
        pass

    for file in input_files:
        print(f"Обробка файлу: {file}")
        shapes = read_shapes_from_file(file)
        max_shape = find_max_measure(shapes)
        with open(output_file, 'a', encoding='utf-8') as output:
            output.write(f"Файл {file}:\n")
            if max_shape:
                measure_name = "Площа" if max_shape.dimention() == 2 else "Об'єм"
                measure_value = max_shape.square() if max_shape.dimention() == 2 else max_shape.volume()
                output.write(f"  Фігура з найбільшою мірою: {max_shape}, {measure_name}: {measure_value:.2f}\n")
            else:
                output.write("  Фігури не знайдено або дані невірні\n")
            output.write("\n")
        print(f"Результати записано в {output_file}")


if __name__ == "__main__":
    main()
