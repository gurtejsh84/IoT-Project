import turtle



def draw_window():
    window_coordinates = [220, 140, 420, 140, 420, 340, 220, 340, 220, 140]
    turtle.color("red")
    turtle.penup()
    turtle.goto(window_coordinates[0], window_coordinates[1])
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.goto(window_coordinates[i * 2], window_coordinates[i * 2 + 1])
    turtle.end_fill()

def draw_polygon(vertices):
    turtle.color("white")
    turtle.penup()
    turtle.goto(vertices[0], vertices[1])
    turtle.pendown()
    turtle.begin_fill()
    for i in range(0, len(vertices), 2):
        turtle.goto(vertices[i], vertices[i + 1])
    turtle.end_fill()

def main():
    turtle.speed(1)
    turtle.hideturtle()

    draw_window()

    num_vertices = int(input("Enter the number of vertices of the polygon: "))
    polygon_vertices = []
    for i in range(num_vertices):
        x = int(input(f"Enter x{i + 1}: "))
        y = int(input(f"Enter y{i + 1}: "))
        polygon_vertices.extend([x, y])

    polygon_vertices.extend([polygon_vertices[0], polygon_vertices[1]])  # Closing the polygon

    draw_polygon(polygon_vertices)

    input("\nPress Enter to clip the polygon...")

    draw_window()

    turtle.done()

main()