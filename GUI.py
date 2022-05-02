import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.title("Lorenzo Del Forno Dynamic Stock Trading Simulator")

mainFrame = tk.Frame(master= window, width=1360, height=750, bg="white")
mainFrame.pack(fill="both")

leftSide = tk.Frame(master= mainFrame, width=260, height=750, bg="blue")
leftSide.pack(fill="y", side="left")

controlPanel = tk.Frame(master= leftSide, width=260, height=100, bg="white")
controlPanel.pack(fill="y", side="top")

stockGeneral = tk.Frame(master= mainFrame, width=700, bg="yellow")
stockGeneral.pack(fill="y", side="left")

stockAdvanced = tk.Frame(master= mainFrame, width=300, bg="red")
stockAdvanced.pack(fill="y", side="left")


window.mainloop()
