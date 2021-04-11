import tkinter as tk
from graph import WeightedGraph
from functools import partial 

root = tk.Tk()
root.title("A* Visualization")

width = 0
_width = tk.StringVar()
height = 0
_height = tk.StringVar()

def baka(grid: WeightedGraph, width: int, height: int) -> None:
    grid.draw_the_line(grid.start_location(), grid.end_location())
    for i in range(0, width):
        for j in range(0, height):
            temp = tk.StringVar()
            temp.set(str(grid.grid[i][j]))
            entry = tk.Label(root, textvariable = temp, width = "2", height = "1")
            entry.grid(padx = 10, pady = 10, row = i, column = j)    

def onii_chan() -> None:
    width = int(_width.get())
    height = int(_height.get())
    grid = WeightedGraph(width, height, True)
    instruction.destroy()
    width_insert.destroy()
    height_insert.destroy()
    create_grid.destroy()
    x.destroy()
    grid.show_grid()
    for i in range(0, width):
        for j in range(0, height):
            temp = tk.StringVar()
            temp.set(str(grid.grid[i][j]))
            entry = tk.Label(root, textvariable = temp, width = "2", height = "1")
            entry.grid(padx = 10, pady = 10, row = i, column = j)
    
    temporary_cmd = partial(baka, grid, width, height)
    draw_the_line_btn = tk.Button(root, text = "DO!!", command = temporary_cmd)
    draw_the_line_btn.grid(row = i + 1, column = 1)

instruction = tk.Label(root, text = "Insert matrix width and height: ")
instruction.grid(padx = 10, pady = 1, sticky = "")

width_insert = tk.Entry(root, textvariable = _width, width = "10")
width_insert.grid(row = 0, column = 5, padx = 10, pady = 10, sticky = "")

x = tk.Label(root, text = " x ")
x.grid(row = 0, column = 14)

height_insert = tk.Entry(root, textvariable = _height, width = "10")
height_insert.grid(row = 0, column = 18, padx = 10, pady = 10)

create_grid = tk.Button(root, text = "Create Matrix", width = "15")
create_grid.grid(row = 0, column = 28, padx = 5, pady = 10)
create_grid["command"] = onii_chan

root.geometry("600x600")
root.minsize(600, 600)
root.mainloop()