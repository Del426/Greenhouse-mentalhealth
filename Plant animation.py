import tkinter as tk
from datetime import datetime, timedelta

class PlantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Plant App")

        self.plant_growth = 0
        self.tasks_completed = 0

        self.plant_image = tk.PhotoImage(file="starter.gif")  # Replace with your plant image
        self.plant_label = tk.Label(root, image=self.plant_image)
        self.plant_label.pack()

        self.info_label = tk.Label(root, text="Plant Growth: 0\nTasks Completed: 0")
        self.info_label.pack()

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.root.after(1000, self.update_growth)  # Call update_growth() every second

    def complete_task(self):
        self.tasks_completed += 1
        self.plant_growth += 10  # Adjust growth factor as needed
        self.update_info()

    def update_growth(self):
        self.plant_growth -= 1  # Plant growth decreases over time
        self.update_info()
        self.root.after(1000, self.update_growth)  # Schedule the next update

    def update_info(self):
        self.info_label.config(text=f"Plant Growth: {self.plant_growth}\nTasks Completed: {self.tasks_completed}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlantApp(root)
    root.mainloop()