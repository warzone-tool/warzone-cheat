import tkinter as tk

class FakeTrainerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Elusion Trainer - Trial Version")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Company Name
        self.company_label = tk.Label(root, text="Elusion", font=("Arial", 20, "bold"), fg="blue")
        self.company_label.pack(pady=10)

        # Trial Version Note
        self.trial_label = tk.Label(root, text="Trial Version - 7 Days Left", font=("Arial", 10), fg="gray")
        self.trial_label.pack()

        # Status Label
        self.status_label = tk.Label(root, text="Status: Not Running", font=("Arial", 12), fg="red")
        self.status_label.pack(pady=10)

        # Feature Buttons
        self.aimbot_var = tk.BooleanVar()
        self.aimbot_button = tk.Checkbutton(root, text="Aimbot", variable=self.aimbot_var, command=self.update_status)
        self.aimbot_button.pack(pady=5, anchor='w')

        self.esp_var = tk.BooleanVar()
        self.esp_button = tk.Checkbutton(root, text="ESP (Enemy Outline)", variable=self.esp_var, command=self.update_status)
        self.esp_button.pack(pady=5, anchor='w')

        self.norecoil_var = tk.BooleanVar()
        self.norecoil_button = tk.Checkbutton(root, text="NoRecoil", variable=self.norecoil_var, command=self.update_status)
        self.norecoil_button.pack(pady=5, anchor='w')

        self.radar_var = tk.BooleanVar()
        self.radar_button = tk.Checkbutton(root, text="Radar", variable=self.radar_var, command=self.update_status)
        self.radar_button.pack(pady=5, anchor='w')

        # Start Button
        self.start_button = tk.Button(root, text="Start Trainer", command=self.start_trainer)
        self.start_button.pack(pady=10, fill='x')

    def update_status(self):
        features = []
        if self.aimbot_var.get():
            features.append("Aimbot")
        if self.esp_var.get():
            features.append("ESP")
        if self.norecoil_var.get():
            features.append("NoRecoil")
        if self.radar_var.get():
            features.append("Radar")

        if features:
            self.status_label.config(text=f"Status: Running - {', '.join(features)}", fg="green")
        else:
            self.status_label.config(text="Status: Not Running", fg="red")

    def start_trainer(self):
        if self.aimbot_var.get() or self.esp_var.get() or self.norecoil_var.get() or self.radar_var.get():
            self.status_label.config(text="Status: Trainer Started (Fake!)", fg="green")
        else:
            self.status_label.config(text="Status: Please enable at least one feature", fg="orange")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FakeTrainerGUI(root)
    root.mainloop()