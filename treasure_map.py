line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?\ne.g. A1, B3, C2\n")
if ((len(position)!=2) or not(position[0] in {'A','B','C'}) or not(position[1] in {'1','2','3'})):
    print("Enter valid input like A1, B3, C2\nNOTE: Size of map is 3*3 (A1-C3)\n")
    exit()
pos1 = position[0].upper()
index2 = int(position[1])-1
char_to_num = {"A": 0, "B": 1, "C": 2}
index1 = char_to_num[pos1]
treasure_map = map
treasure_map[index2][index1]= 'X' 
print(f"{line1}\n{line2}\n{line3}")