import customtkinter as ctk


class TodoApp:
    def __init__(self, root, manager, db):
        self.root = root
        self.db = db
        self.manager = manager
        self.root.title("Habit Tracker")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # scroolling between the tasks
        self.scroll_frame = ctk.CTkScrollableFrame(self.root)
        self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.refresh_list()

    def refresh_list(self):
        for items in self.manager.tasks_list:

            # create a frame for every tasks.
            card = ctk.CTkFrame(
                self.scroll_frame,
                corner_radius=10,
                fg_color="#2b2b2b",
                border_width=1,
                border_color="white",
            )
            card.pack(fill="x", padx=20, pady=8)

            label_name = ctk.CTkLabel(
                card, text=items["task"], font=("Segoe UI", 17), anchor="w"
            )
            label_name.pack(side="left", padx=20, pady=15)

            streak_label = ctk.CTkLabel(
                card, text=f"streak: {items['streak']}", font=("Segoe UI", 14)
            )
            streak_label.pack(side="right", padx=10)
