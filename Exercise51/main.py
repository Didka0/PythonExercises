import math

def is_square(user_i_figures):
    if user_i_figures == "square":
        length = int(input("What's the length of one side of your square? "))
        face_area = length * length
        face_area = round(face_area,3)
        print(face_area)

def is_rectangle(user_i_figures):
    if user_i_figures == "rectangle":
        length = int(input("What's the length of the one side of your rectangle? "))
        width = int(input("What's the width of the one side of your rectangle? "))
        face_area = length * width
        face_area = round(face_area,3)
        print(face_area)

def is_circle(user_i_figures):
    if user_i_figures == "circle":
        radius = int(input("What's the radius of your circle? "))
        face_area = math.pi * radius * radius 
        face_area = round(face_area,3)
        print(face_area)

def is_triangle(user_i_figures):
    if user_i_figures == "triangle":
        side = int(input("What's the side of your triangle? "))
        height = int(input("What's the height of your triangle? "))
        face_area = (side * height) / 2
        face_area = round(face_area,3)
        print(face_area)

def main():
    print("You can choose between square, rectangle, circle or triangle")
    user_i_figures = input("What'a your figure? ").lower()
    if user_i_figures != "sqare" and user_i_figures != "rectangle" and user_i_figures != "circle" and user_i_figures != "triangle":
        print("Invalid input")

    is_square(user_i_figures)
    is_rectangle(user_i_figures)
    is_circle(user_i_figures)
    is_triangle(user_i_figures)

main()