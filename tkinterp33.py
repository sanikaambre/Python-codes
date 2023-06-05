import tkinter as tk
parent=tk.Tk()
mytext=tk.Text(parent)
mytext.insert('1.0',"-Python excercises,solution-")
mytext.insert('1.19','Practice')
mytext.delete('1.0')
mytext.delete('end - 2 chars')
mytext.pack()
parent.mainloop()

            
