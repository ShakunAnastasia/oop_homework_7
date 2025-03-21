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
        self.a = a
        self.b = b
        self.c = c
        if not self.is_valid():
            raise ValueError("Задані сторони не утворюють трикутник")
    def is_valid(self):
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)
    def perimeter(self):
        return self.a + self.b + self.c
    def square(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Rectangle(TwoDimensional):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def perimeter(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.b

class Trapeze(TwoDimensional):
    def __init__(self, base1, base2, side1, side2):
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2
    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2
    def square(self):
        height = math.sqrt(self.side1**2 - ((self.base2 - self.base1) / 2)**2)
        return (self.base1 + self.base2) * height / 2

class Parallelogram(TwoDimensional):
    def __init__(self, a, b, height):
        self.a = a
        self.b = b
        self.height = height
    def perimeter(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.height

class Circle(TwoDimensional):
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return 2 * math.pi * self.radius
    def square(self):
        return math.pi * self.radius**2

class Ball(ThreeDimensional):
    def __init__(self, radius):
        self.radius = radius
    def squareSurface(self):
        return 4 * math.pi * self.radius**2
    def volume(self):
        return (4 / 3) * math.pi * self.radius**3

class TriangularPyramid(ThreeDimensional):
    def __init__(self, base_side, height):
        self.base_side = base_side
        self.height = height
    def squareBase(self):
        return (math.sqrt(3) / 4) * self.base_side**2
    def squareSurface(self):
        base_area = self.squareBase()
        lateral_area = (3 / 2) * self.base_side * math.sqrt((self.base_side**2) / 4 + self.height**2)
        return base_area + lateral_area
    def volume(self):
        return (1 / 3) * self.squareBase() * self.height

class QuadrangularPyramid(ThreeDimensional):
    def __init__(self, base_a, base_b, height):
        self.base_a = base_a
        self.base_b = base_b
        self.height = height
    def squareBase(self):
        return self.base_a * self.base_b
    def squareSurface(self):
        base_area = self.squareBase()
        lateral_area = self.base_a * math.sqrt((self.base_b / 2)**2 + self.height**2) + \
                       self.base_b * math.sqrt((self.base_a / 2)**2 + self.height**2)
        return base_area + lateral_area
    def volume(self):
        return (1 / 3) * self.squareBase() * self.height

class RectangularParallelepiped(ThreeDimensional):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def squareSurface(self):
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)
    def volume(self):
        return self.a * self.b * self.c

class Cone(ThreeDimensional):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def squareSurface(self):
        slant_height = math.sqrt(self.radius**2 + self.height**2)
        return math.pi * self.radius * slant_height + math.pi * self.radius**2
    def volume(self):
        return (1 / 3) * math.pi * self.radius**2 * self.height

class TriangularPrism(ThreeDimensional):
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height
    def squareBase(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def squareSurface(self):
        base_area = self.squareBase()
        lateral_area = (self.a + self.b + self.c) * self.height
        return 2 * base_area + lateral_area
    def volume(self):
        return self.squareBase() * self.height

def read_shapes_from_file(filename):
    shapes = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            shape_type = parts[0]
            params = list(map(float, parts[1:]))
            try:
                if shape_type == "Triangle":
                    shapes.append(Triangle(*params))
                elif shape_type == "Rectangle":
                    shapes.append(Rectangle(*params))
                elif shape_type == "Trapeze":
                    shapes.append(Trapeze(*params))
                elif shape_type == "Parallelogram":
                    shapes.append(Parallelogram(*params))
                elif shape_type == "Circle":
                    shapes.append(Circle(*params))
                elif shape_type == "Ball":
                    shapes.append(Ball(*params))
                elif shape_type == "TriangularPyramid":
                    shapes.append(TriangularPyramid(*params))
                elif shape_type == "QuadrangularPyramid":
                    shapes.append(QuadrangularPyramid(*params))
                elif shape_type == "RectangularParallelepiped":
                    shapes.append(RectangularParallelepiped(*params))
                elif shape_type == "Cone":
                    shapes.append(Cone(*params))
                elif shape_type == "TriangularPrism":
                    shapes.append(TriangularPrism(*params))
                else:
                    print(f"Невідомий тип фігури: {shape_type}")
            except ValueError as ve:
                print(f"Помилка у файлі {filename}: {ve}")
    return shapes

def find_max_measure(shapes):
    if not shapes:
        return None
    return max(shapes, key=lambda shape: shape.volume())

def main():
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    for file in input_files:
        print(f"Обробка файлу: {file}")
        shapes = read_shapes_from_file(file)
        max_shape = find_max_measure(shapes)
        if max_shape:
            print(f"Фігура з найбільшою мірою: {type(max_shape).__name__}, Міра: {max_shape.volume()}")
        else:
            print("Фігури не знайдено або дані невірні.")
        print()

if __name__ == "__main__":
    main()
