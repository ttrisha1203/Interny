import tkinter as tk
from time import strftime


# Create a function to update the time
def update_time():
    current_time = strftime('%H:%M:%S %p')  # Format time as HH:MM:SS AM/PM
    label.config(text=current_time)  # Update label text
    label.after(1000, update_time)  # Call update_time every 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("250x100")

# Create a label to display the time
label = tk.Label(root, font=('calibri', 35, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Call the update_time function to start updating the time
update_time()

# Run the Tkinter event loop
root.mainloop()
