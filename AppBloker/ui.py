import customtkinter as ctk
from tkinter import messagebox
import time
from logic import block_with_timer, block_app_with_timer

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FocusBlockerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Focus Blocker Pro")
        self.geometry("750x650")
        self.selected_time = {"h": 0, "m": 0, "s": 0}
        self.active_blocks = []

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.title_label = ctk.CTkLabel(
            self, text="Focus Blocker Pro",
            font=ctk.CTkFont(family="Segoe UI", size=32, weight="bold")
        )
        self.title_label.grid(row=0, column=0, pady=(30, 10))

        self.subtitle_label = ctk.CTkLabel(
            self, text="Stay disciplined. Stay focused.",
            text_color="#94a3b8", font=ctk.CTkFont(size=14)
        )
        self.subtitle_label.grid(row=1, column=0, pady=(0, 20))

        self.card = ctk.CTkFrame(self, fg_color="#1e293b", corner_radius=15)
        self.card.grid(row=2, column=0, padx=40, pady=10, sticky="nsew")
        self.card.grid_columnconfigure(0, weight=1)

        self.website_entry = ctk.CTkEntry(
            self.card, placeholder_text="Enter Website (e.g. youtube.com)",
            height=45, border_color="#334155"
        )
        self.website_entry.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        self.app_entry = ctk.CTkEntry(
            self.card, placeholder_text="Enter App Name (e.g. Discord)",
            height=45, border_color="#334155"
        )
        self.app_entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.time_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        self.time_frame.grid(row=2, column=0, pady=15)

        self.set_time_btn = ctk.CTkButton(
            self.time_frame, text="Set Block Duration",
            command=self.open_time_popup,
            fg_color="#334155", hover_color="#475569", height=40
        )
        self.set_time_btn.pack(side="left", padx=10)

        self.time_display = ctk.CTkLabel(
            self.time_frame, text="00h 00m 00s",
            font=ctk.CTkFont(family="Consolas", size=16)
        )
        self.time_display.pack(side="left", padx=10)

        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.grid(row=3, column=0, pady=20)

        self.block_web_btn = ctk.CTkButton(
            self.btn_frame, text="Block Website",
            command=self.block_website_ui,
            fg_color="#3b82f6", hover_color="#2563eb",
            width=160, height=45
        )
        self.block_web_btn.grid(row=0, column=0, padx=10)

        self.block_app_btn = ctk.CTkButton(
            self.btn_frame, text="Block App",
            command=self.block_app_ui,
            fg_color="#8b5cf6", hover_color="#7c3aed",
            width=160, height=45
        )
        self.block_app_btn.grid(row=0, column=1, padx=10)

        self.list_label = ctk.CTkLabel(
            self, text="Active Blocks",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.list_label.grid(row=4, column=0, pady=(20, 5), sticky="w", padx=45)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="#0f172a")
        self.scrollable_frame.grid(row=5, column=0, padx=40, pady=(0, 30), sticky="nsew")

        self.update_timers()

    def update_timers(self):
        now = time.time()
        for block in self.active_blocks[:]:
            remaining = block['end_time'] - now
            if remaining <= 0:
                block['frame'].destroy()
                self.active_blocks.remove(block)
            else:
                h = int(remaining // 3600)
                m = int((remaining % 3600) // 60)
                s = int(remaining % 60)
                block['label'].configure(text=f"{h:02d}:{m:02d}:{s:02d}")

        self.after(1000, self.update_timers)

    def open_time_popup(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Set Timer")
        popup.geometry("300x250")
        popup.attributes("-topmost", True)

        ctk.CTkLabel(popup, text="Set Duration").pack(pady=15)

        input_frame = ctk.CTkFrame(popup)
        input_frame.pack(pady=10)

        h_entry = ctk.CTkEntry(input_frame, width=50, justify="center")
        h_entry.insert(0, str(self.selected_time["h"]))
        h_entry.grid(row=0, column=0, padx=5)

        m_entry = ctk.CTkEntry(input_frame, width=50, justify="center")
        m_entry.insert(0, str(self.selected_time["m"]))
        m_entry.grid(row=0, column=1, padx=5)

        s_entry = ctk.CTkEntry(input_frame, width=50, justify="center")
        s_entry.insert(0, str(self.selected_time["s"]))
        s_entry.grid(row=0, column=2, padx=5)

        def save():
            try:
                self.selected_time["h"] = int(h_entry.get())
                self.selected_time["m"] = int(m_entry.get())
                self.selected_time["s"] = int(s_entry.get())

                self.time_display.configure(
                    text=f"{self.selected_time['h']:02d}h {self.selected_time['m']:02d}m {self.selected_time['s']:02d}s"
                )
                popup.destroy()
            except:
                messagebox.showerror("Error", "Invalid input")

        ctk.CTkButton(popup, text="Confirm", command=save).pack(pady=20)

    def add_block_to_list(self, name, duration, block_type):
        end_time = time.time() + duration

        row = ctk.CTkFrame(self.scrollable_frame)
        row.pack(fill="x", pady=5)

        timer_label = ctk.CTkLabel(row, text="--:--:--")
        timer_label.pack(side="right", padx=10)

        ctk.CTkLabel(row, text=name).pack(side="left", padx=10)

        self.active_blocks.append({
            "end_time": end_time,
            "label": timer_label,
            "frame": row
        })

    def block_website_ui(self):
        site = self.website_entry.get().strip()
        duration = (self.selected_time["h"] * 3600 +
                    self.selected_time["m"] * 60 +
                    self.selected_time["s"])

        if duration == 0:
            messagebox.showerror("Error", "Set time first")
            return

        block_with_timer(site, duration)
        self.add_block_to_list(site, duration, "web")

    def block_app_ui(self):
        app = self.app_entry.get().strip()
        duration = (self.selected_time["h"] * 3600 +
                    self.selected_time["m"] * 60 +
                    self.selected_time["s"])

        if duration == 0:
            messagebox.showerror("Error", "Set time first")
            return

        block_app_with_timer(app, duration)
        self.add_block_to_list(app, duration, "app")


if __name__ == "__main__":
    app = FocusBlockerApp()
    app.mainloop()