##Rudy Garcia

import math
from array import *
import time as time

MENU = "\t\t---MENU---\t\t\n 1: change matrix one\n 2: change matrix 2\n 3:use answer matrix as new matrix\n 4: reset both matrixes\n 5: do the darn multiplication!"
options = range(1,6)
global matrix__1
matrix__1 = []
global matrix__2
matrix__2 = []
global matrix__3
matrix__3 = []
global past_1
global past_2
global past_3


def correct_inputs(number = "", num_type = ""):
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
          if number > 0:
            play = True
          else:
            raise ValueError
        except ValueError:
          number = input("I need an positive integer: ")
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

def matrix_displayer(height, length, matrix_num = 3):
  formatted = " "
  edge = "┏"
  edge_char =  "━━━"
  space_length = maxi(matrix_num)
  while len(edge_char) < space_length:
    edge_char += "━" 
  for x in range(0,length):
    edge += edge_char
  edge += "┓\n"
  formatted += edge
  count = 0
  print(f"formatting matrix {matrix_num}... ")
  time.sleep(0.5)
  try:
    for r in range(0,height):
      line = " ┃"
      for c in range(0, length):
        value = 0
        spaces = ""
        if matrix_num == 1:
          value = matrix__1[r][c]
        elif matrix_num == 2:
          value = matrix__2[r][c]
        elif matrix_num == 3 :
          value = matrix__3[r][c]
        diff = space_length - len(str(value))
        string = f" {value}{spaces}"
        while len(string) < space_length:
          string += " "
        line = line + string
        count += 1
      formatted += f"{line}┃\n"
  except IndexError:
    print(f"Something still wrong for {r} and {c}")
    pass
  edge_2 = " ┗"
  for x in range(0,length):
    edge_2 += edge_char 
  edge_2 += "┛\n"
  formatted += edge_2
  print(formatted)
## to be completed

def solver(height_1, length_2):
  for y in range(0,height_1):
    temp_row = []
    for i in range(0, length_2):
      place_value = 0
      for x in range(0,len(matrix__1[0])):
        place_value += matrix__1[y][x] * matrix__2[x][i]
      temp_row.append(place_value)
    matrix__3.append(temp_row)

def maxi(matrix_num):
  maxes = []
  if matrix_num == 1:
    for x in range(0,len(matrix__1)):
      relative_max = max(matrix__1[x])
      maxes.append(relative_max)
  if matrix_num == 2:
    for x in range(0,len(matrix__2)):
      relative_max = max(matrix__2[x])
      maxes.append(relative_max)
  if matrix_num == 3:
    for x in range(0,len(matrix__3)):
      relative_max = max(matrix__3[x])
      maxes.append(relative_max)
  absolute_max = max(maxes)
  length = len(str(absolute_max)) + 3
  return length

def main():
  print("Hello, I do matrices multiplication!")
  quit = "g"
  main_count = 0
  while quit != "q":
    play = False
    matrix__1 = []
    matrix__2 = []
    matrix__3 = []
    if main_count > 0:
      print(MENU)
      option = input("Your choice: ")
      try:
        option = int(option)
      except TypeError:
        print("It needs to be a number at least!")
      while option not in options:
        option = input("I need a correct choice: ")
        try:
          option = int(option)
        except TypeError:
          print("It needs to be a number at least!")
      if option == 1:
        length_1 = input("matrix 1 row length: ")
        length_1 = correct_inputs(length_1)
        height_1 = input("matrix 1 coloumn heigth: ")
        height_1 = correct_inputs(height_1)
        matrix_1(length_1, height_1)
        matrix_displayer(height_1, length_1, 1)
      elif option == 2:
        length_2 = input("matrix 2 row length: ")
        length_2 = correct_inputs(length_2)
        height_2 = input("matrix 2 coloumn heigth: ")
        height_2 = correct_inputs(height_2)
        matrix_2(length_2, height_2)
        matrix_displayer(height_2, length_2, 2)
      elif option == 3:
        which = input("Which one? (1 or 2)")
        try:
          which = int(which)
          if which == 1:
            matrix__1 == past_1
          elif which == 2:
            matrix__2 = past_2
          else:
            print("No replacement done")
        except ValueError:
          print("No replacement done")
      elif option == 4:
        length_1 = input("matrix 1 row length: ")
        length_1 = correct_inputs(length_1)
        height_1 = input("matrix 1 coloumn heigth: ")
        height_1 = correct_inputs(height_1)
        length_2 = input("matrix 2 row length: ")
        length_2 = correct_inputs(length_2)
        height_2 = input("matrix 2 coloumn heigth: ")
        height_2 = correct_inputs(height_2)
        matrix_1(length_1, height_1)
        matrix_displayer(height_1, length_1, 1)
        matrix_2(length_2, height_2)
        matrix_displayer(height_2, length_2, 2)
      elif options == 5:
         solver(height_1, length_2)
      print("Your resulting matrix:")
      matrix_displayer(height_1, length_2)
    else:
      while play != True:
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
          play = True
      matrix_1(length_1, height_1)
      matrix_displayer(height_1, length_1, 1)
      matrix_2(length_2, height_2)
      matrix_displayer(height_2, length_2, 2)
      solver(height_1, length_2)
      print("Your resulting matrix:")
      matrix_displayer(height_1, length_2)
    past_1 = matrix__1
    past_2 = matrix__2
    past_3 = matrix__3
    main_count += 1
    quit = input("Enter \"q\" to quit, hit enter to continue")
  print("Thank you for using me! Have a good rest of your day! ✌")
  time.sleep(5)
main()