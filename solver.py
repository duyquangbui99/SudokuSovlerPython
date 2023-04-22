import tkinter
from tkinter import *
import random



entry_list = [[],[],[]]
var =[]
done = False
# Define a variable to keep track of the elapsed time
elapsed_time = 0
update_id = None

guess = str()
grid = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]
]



def one_grid(row):
    global grid, entry_list
    entries = []
    for i in range(9):
        # create a new Entry widget for this cell in the grid
        entry = Entry(row, textvariable=var, width=2, highlightbackground="#282828", fg="#0000CE", font="Geneva 30 bold", bg="whitesmoke", justify=CENTER)
        # position the cell within the grid using its index
        entry.place(x=(i % 3) * 47 + 5, y=(i // 3) * 47 + 5)
         # add the new Entry widget to the list of entries for this row
        entries.append(entry)
        # add the new Entry widget to the global list of entries for the whole grid
        entry_list[i // 3].append(entry)
    return entries

def display_val():
    global entry_list

    # Display values in the first three rows
    u=0
    for a in entry_list:
        a_splited = [a[x:x+9] for x in range(0, len(a), 9)]
        for y in range(9):
            if(grid[u][y] != 0):
                a_splited[0][y].insert(0,grid[u][y]) 
        u+=1
    # Display values in the second three rows
    u=3
    for a in entry_list:
        a_splited = [a[x:x+9] for x in range(0, len(a), 9)]
        for y in range(9):
            if(grid[u][y] != 0):
                a_splited[1][y].insert(0,grid[u][y]) 
        u+=1
    # Display values in the last three rows   
    u=6
    for a in entry_list:
        a_splited = [a[x:x+9] for x in range(0, len(a), 9)]
        for y in range(9):
            if(grid[u][y] != 0):
                a_splited[2][y].insert(0,grid[u][y]) 
        u+=1

def clear():
    global grid
    grid = [[0] * 9 for _ in range(9)]

def scramble():
    global grid

    clear()
    for a in entry_list:
        for b in a:
            b.delete(first=0,last=100)
    amount = 100

    
    for i in range(amount):
        y = random.randint(0,len(grid)-1)
        x = random.randint(0,len(grid)-1)
        num = random.randint(1,len(grid))
        allow = 0
        for e in range(len(grid)):
            if num not in grid[x] and num != grid[e][y]:
                allow +=1
        grid[x][y] = num
        tempo = grid     
        tempo = rearrange(tempo)
        
        for e in range(len(grid)):
            if(duplicate_checker(tempo[e])):
                allow = 0
        if allow !=len(grid):
            grid[x][y] = 0
               
    display_val()
    

def rearrange(a):
    # Create a new 2D list to store the rearranged values
    temp = [[], [], [], [], [], [], [], [], []]
    # Keep track of the number of elements processed and the current subgrid
    count = 0
    ch = 0
    
    # Loop through each row in the input grid
    for e in range(len(a)):
        # Loop through the first 3 elements in the row
        for x in range(3):
            # If the element is not 0, add it to the current subgrid
            if a[e][x] != 0:
                temp[ch].append(a[e][x])
        # Increment the count and check if a subgrid is complete
        count += 1
        if count == 3:
            ch += 1
            count = 0

    # Repeat the above process for the next 3 columns and the last 3 columns
    for e in range(len(a)):
        for x in range(3, 6):
            if a[e][x] != 0:
                temp[ch].append(a[e][x])
        count += 1
        if count == 3:
            ch += 1
            count = 0
            
    for e in range(len(a)):
        for x in range(6, 9):
            if a[e][x] != 0:
                temp[ch].append(a[e][x])
        count += 1
        if count == 3:
            ch += 1
            count = 0
            
    # Return the rearranged 2D list
    return temp

def duplicate_checker(a):
    unique_set = set(a)
    is_duplicate = len(a) != len(unique_set)
    # print(is_duplicate)
    if is_duplicate:
        return True
    






