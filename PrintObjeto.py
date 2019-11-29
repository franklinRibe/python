class Point(object):
    x = 0
    y = 0  
    def print_point(self):
        print(self.x, self.y)

class Rectangle(object):
    def find_center(rect):
        p = Point()
        p.x = rect.cornerX + rect.width / 2.0
        p.y = rect.cornerY + rect.height / 2.0
        return p

def main():
    pontoA = Point()
    pontoA.x = 3
    pontoA.y = 4
    pontoA.print_point()

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.cornerX = 0.0
    box.cornerY = 0.0

    center = Rectangle.find_center(box)
    Point.print_point(center)

if __name__ == "__main__":
    main()
