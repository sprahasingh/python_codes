import math
def paint_calc(height,width,cover):
  num = math.ceil((height*width)/cover)
  print(f"You'll need {num} cans of paint.")
test_h = int(input("Enter height of wall\n"))
test_w = int(input("Enter width of wall\n"))
coverage = 5
paint_calc(test_h, test_w, coverage)
