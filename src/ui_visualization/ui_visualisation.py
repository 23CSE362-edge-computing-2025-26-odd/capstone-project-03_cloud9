import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Map Visualization")
root.geometry("600x600")   

# Example gateways and items
gateways = [(2, 3), (6, 8), (9, 5)]
items = {"M001": (3, 4), "M002": (7, 5), "M003": (4, 8)}

# Create matplotlib figure
fig, ax = plt.subplots(figsize=(5, 5))  # bigger figure

# Plot gateways
for gx, gy in gateways:
    ax.plot(gx, gy, 'rs', markersize=10, label="Gateway")

# Plot items
for item, (x, y) in items.items():
    ax.plot(x, y, 'bo', markersize=8)
    ax.text(x + 0.3, y, item, fontsize=12)

ax.set_title("Factory Layout", fontsize=14)
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)

# Embed matplotlib figure into Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop()


