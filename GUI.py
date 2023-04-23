import tkinter
from tkinter import *
import random

root = Tk()
root.title("Sudoku")
root.minsize(width=700, height=550)


title = Label(root, text='SUDOKU', fg="black",font="Geneva 30")
title.pack()


entry_list = [[],[],[]]
var =[]
done = False
# Define a variable to keep track of the elapsed time
elapsed_time = 0
update_id = None

#guess = str()
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


def update_time():
    global elapsed_time, done, update_id
    if not done:
        elapsed_time += 1
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        time_string = f"{minutes:02d}:{seconds:02d}"
        time_label.config(text=time_string)
        update_id = root.after(1000, update_time)

def submit():
    global done,update_id
    update_id = None
    done = True


def one_grid(row, row_index):
    global grid, entry_list
    entries = []
    
    for i in range(9):
        # create a new Entry widget for this cell in the grid
        entry = Entry(row, textvariable=var, width=2, highlightbackground="#282828", fg="#0000CE", font="Geneva 30 bold", bg="whitesmoke", justify=CENTER)
        # position the cell within the grid using its index
        entry.place(x=(i % 3) * 47 + 5, y=(i // 3) * 47 + 5)
        # bind the show_possible_numbers function to the "<Button-1>" event of the Entry widget
        entry.bind("<Button-1>", show_possible_numbers)
        # add the new Entry widget to the list of entries for this row
        entries.append(entry)
        # add the new Entry widget to the global list of entries for the whole grid
        entry_list[i // 3].append(entry)

        entry_list[i // 3][row_index * 3 + i % 3] = entry
        # set the custom attribute "position" of the Entry widget to its position in the grid
        entry.position = (row_index, i)


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
    global grid , elapsed_time, done, update_id
    elapsed_time = 0
    done = False
    if not update_id:
        update_id = root.after(1000, update_time)

    clear()
    for a in entry_list:
        for b in a:
            b.delete(first=0,last=100)
    amount = 20

    
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

def stay(num,x,y):

    for e in range(9):
        if grid[y][e] ==num:
            return False
    for e in range(9):
        if grid[e][x] ==num:
            return False

    for i in range(3):
        for e in range(3):
            if grid[((y//3)*3)+i][((x//3)*3)+e] ==num:
                return False
    return True

def pressed_solve():
    global grid,done
    done =False
    solver()
def solver():
    global grid,done,update_id
    
    
    if(done ==False):
        
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    for num in range(1,10):
                        if stay(num,x,y):
                            grid[y][x]=num
                            solver()
                            grid[y][x]=0
                    return
        done =True
        update_id = None
        for a in entry_list:
            for b in a:
                b.delete(first=0,last=100)
        display_val()
        return
    
def pressed_hint():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for num in range(1, 10):
                    if stay(num, x, y):
                        grid[y][x] = num
                        for a in entry_list:
                            for b in a:
                                b.delete(first=0,last=100)
                        display_val()
                        return
    
def show_possible_numbers(event):
    global grid
    widget = event.widget

    row, col = widget.position

     #convert widget position to girt position
    x = (row // 3) * 3 + col // 3
    y = (row % 3) * 3 + col % 3

    numbers = [i for i in range(1,10)]
    exist  = []
    for i in range(9):
        # Check row
        if grid[x][i] in numbers:
            numbers.remove(grid[x][i])
        # Check column
        if grid[i][y] in numbers:
            numbers.remove(grid[i][y])
        # Check subgrid
        subgrid_x, subgrid_y = (x // 3) * 3, (y // 3) * 3
        for j in range(3):
            for k in range(3):
                if grid[subgrid_x + j][subgrid_y + k] in numbers:
                    numbers.remove(grid[subgrid_x + j][subgrid_y + k])
    for i in range(1,10):
        if i not in numbers:
            exist.append(i)
    posnum.config(text="Exist numbers: " + " ".join(str(num) for num in exist))

def checkrow_horz(a):
    for x in a:
        if(duplicate_checker(x) == True):
            return True
        
        
def checkrow_vert(a):
    for y in range(len(a)):
        temp = []
        for x in a:
            temp.append(x[y])
        if(duplicate_checker(temp) == True):
            return True
            
def checkcol(a):
    for y in range(3):
        temp = []
        for x in range(int(len(a)/3)):
            temp.append(a[x][3*y])
            temp.append(a[x][3*y+1])
            temp.append(a[x][3*y+2])
        if(duplicate_checker(temp) == True):
           return True
        temp = []
        for x in range(3,(int(len(a)/3))*2):
            temp.append(a[x][3*y])
            temp.append(a[x][3*y+1])
            temp.append(a[x][3*y+2])
        if(duplicate_checker(temp) == True):
           return True
        temp = []
        for x in range(6,(int(len(a)/3))*3):
            temp.append(a[x][3*y])
            temp.append(a[x][3*y+1])
            temp.append(a[x][3*y+2])
        if(duplicate_checker(temp) == True):
           return True

def submit():
    global entry_list
    
    temp = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    u=0
    for a in entry_list:
        a_splited = [a[x:x+9] for x in range(0, len(a), 9)]
        for y in range(9):
            if(a_splited[0][y].get() != '' ):
                temp[u][y]= int(a_splited[0][y].get())
        u+=1
    u=3
    for a in entry_list:
        a_splited = [a[x:x+9] for x in range(0, len(a), 9)]
        for y in range(9):
            if(a_splited[1][y].get() != '' ):
                temp[u][y]= int(a_splited[1][y].get())
        u+=1
        
    u=6
    for a in entry_list:
        a_splited = [a[x:x+9] for x in range(0, len(a), 9)]
        for y in range(9):
            if(a_splited[2][y].get() != '' ):
                temp[u][y]= int(a_splited[2][y].get())
        u+=1
             
    if(checkrow_horz(temp) == True or checkrow_vert(temp) ==True or checkcol(temp) ==True):
        wrong()
    else:
        correct()

def wrong():
    title.config(fg="#990000", text="Try Again")
    rows = [canvas for canvas in box.winfo_children() if isinstance(canvas, Canvas)]
    for row in rows:
        row.config(highlightbackground="#990000")
        row.after(2100, lambda row=row: row.config(highlightbackground="white"))
    title.after(2100, lambda: title.config(fg="#382888", text="Sudoku"))


def correct():
    global done
    done = True
    highlight_color = "#288888"
    normal_color = "white"
    title.config(fg="#288888", text="Correct")
    rows = [canvas for canvas in box.winfo_children() if isinstance(canvas, Canvas)]
    for row in rows:
        row.config(highlightbackground=highlight_color)
        row.after(2100, lambda row=row: row.config(highlightbackground=normal_color))
    title.after(2100, lambda: title.config(fg="#382888", text="Sudoku"))


posnum = Label(root,text="", font="Geneva 25 bold")
posnum.pack()
#create a box (canvas) in the root master
box = Canvas(root, width = 435, height = 435,bd=6, highlightthickness=5)  
box.pack(side=LEFT)


coordinates = [(0, 0), (150, 0), (300, 0), (0, 150), (150, 150), (300, 150), (0, 300), (150, 300), (300, 300)]
#Create rows for the grid
for i in range(9):
    canvas = Canvas(box, width=120, height=120, background="#282828", bd=10, highlightthickness=10)
    one_grid(canvas,i)
    canvas.place(x=coordinates[i][0], y=coordinates[i][1])
    globals()["row" + str(i+1)] = canvas



time_label = Label(root,text="00:00", font="Geneva 30 bold")
time_label.pack(pady =20)

but = Canvas(root, width=500, height=200, bd=13, highlightthickness=0)
but.pack(padx =20)
submitbtn = Button(but, text="Submit", fg="#282828", command=submit, font="Geneva 30 bold", highlightbackground="#00ff00", justify=CENTER)
submitbtn.configure(bg='#282828', width=8)
submitbtn.pack(pady=20)

reset = Button(but, text="New Game", fg="#282828", command = scramble,font="Geneva 30 bold",highlightbackground="#00BFFF",justify=CENTER)
reset.configure(bg='#382888', width=8)
reset.pack(pady=20)

solve = Button(but, text="Solve", fg="#282828", command = pressed_solve ,font="Geneva 30 bold",highlightbackground="#FF8C00",justify=CENTER)
solve.configure(bg='#FCD4D4', width=8)
solve.pack(pady=20)

hint = Button(but, text="Help", fg="#282828", font="Geneva 30 bold", highlightbackground="#FFFF00", justify=CENTER)
hint.configure(bg='#FCD4D4', width=8)
hint.pack(pady=20)


update_time()
scramble()

root.mainloop()
