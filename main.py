##rudy garcia

import math

matrix__1 = []
matrix__2 = []

def correct_inputs(number = "", num_type = ""):
  if number == "" and num_type == "":
    print("Not the right use m8")
  else:
    play = False
    while play != True: 
      if num_type == "f":
        try:
          number = float(number)
          play = True
        except ValueError:
          number = input("I need a number: ")
      else:
        try:
          number = int(number)
          play = True
        except ValueError:
          number = input("I need an integer: ")
  return number

def matrix_1(length_1, height_1):
  print("\tMATRIX 1:")
  for x in range(0, height_1):
    temp_row = []
    for i in range(0, length_1):
      number = input(f"row {x+1} coloumn {i+1}: ")
      number = correct_inputs(number, "f")
      temp_row.append(number)
    matrix__1.append(temp_row)

def matrix_2(length_2, height_2):
  print("\tMATRIX 2:")
  for x in range(0, height_2):
    temp_row = []
    for i in range(0, length_2):
      number = input(f"row {x+1} coloumn {i+1}: ")
      number = correct_inputs(number, "f")
      temp_row.append(number)
    matrix__2.append(temp_row)

def space_insert(number):
  emptiness = ""
  for x in range(0, number):
    emptiness += ""
  return emptiness

def matrix_displayer(height, length):
  formatted_1 = " "
  
  for x in range(0,length_1):
    formatted_1 += "___"
  space_length = length_1/2 + 1
  star_place = math.floor(height_1/2) 
  formatted_1 += space_insert(space_length)
  for x in range(0,length_2):
    formatted_1 += "___"
  for y in range(0, height_1)

  print(formatted_1)
## to be completed

def solver(length_1):
  matrix_3 = []
  for y in range(0,matrix_1.length())
    for i in range(0, length_2):
      place_value = 0
      fin_row = []
      for x in range(0,matrix_1[0].length()):
        place_value += matrix_1[y][x] * matrix_2[x][y]
      fin_row.append(place_value)
    mtrix_3.append(fin_row)
print("Hello, I do matrices multiplication!")
length_1 = input("matrix 1 row length: ")
length_1 = correct_inputs(length_1)
height_1 = input("matrix 1 coloumn heigth: ")
height_1 = correct_inputs(height_1)
length_2 = input("matrix 2 row length: ")
length_2 = correct_inputs(length_2)
height_2 = input("matrix 2 coloumn heigth: ")
height_2 = correct_inputs(height_2)
if length_1 != height_2:
  print("These matrices are imcompatible for multiplication")
else:
  print("All right, let's fill those matrixes out! (by rows)")
matrix_1(length_1, height_1)
matrix_2(length_2, height_2)
