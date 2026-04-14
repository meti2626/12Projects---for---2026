import tkinter as tk
from tkinter import messagebox
from logic import block_with_timer, block_app_with_timer


def run_app():
    root = tk.Tk()
    root.title("Focus Blocker Pro")
    root.geometry("650x520")
    root.configure(bg="#121212")

    # ---------------- HELPERS ----------------

    def convert_to_seconds(h, m, s):
        return (h * 3600) + (m * 60) + s

    def get_time_values():
        try:
            h = int(hour_entry.get() or 0)
            m = int(min_entry.get() or 0)
            s = int(sec_entry.get() or 0)
            return convert_to_seconds(h, m, s), h, m, s
        except:
            messagebox.showerror("Error", "Enter valid numbers for time")
            return None, 0, 0, 0

    # ---------------- FUNCTIONS ----------------

    def block_website_ui():
        site = website_entry.get().strip()
        site = site.replace("https://", "").replace("http://", "").replace("www.", "")

        duration, h, m, s = get_time_values()
        if duration is None:
            return

        if not site:
            messagebox.showerror("Error", "Enter a website")
            return

        block_with_timer(site, duration)
        listbox.insert(tk.END, f"🌐 {site} → {h}h {m}m {s}s BLOCKED")

        website_entry.delete(0, tk.END)

    def block_app_ui():
        app = app_entry.get().strip()

        duration, h, m, s = get_time_values()
        if duration is None:
            return

        if not app:
            messagebox.showerror("Error", "Enter an application name")
            return

        block_app_with_timer(app, duration)
        listbox.insert(tk.END, f"📱 {app} → {h}h {m}m {s}s BLOCKED")

        app_entry.delete(0, tk.END)

    # ---------------- TITLE ----------------

    title = tk.Label(
        root,
        text="FOCUS BLOCKER PRO",
        font=("Segoe UI", 22, "bold"),
        fg="white",
        bg="#121212"
    )
    title.pack(pady=15)

    # ---------------- INPUT CARD ----------------

    card = tk.Frame(root, bg="#1E1E1E", padx=15, pady=15)
    card.pack(pady=10, padx=20, fill="x")

    # Website
    tk.Label(card, text="Website", fg="white", bg="#1E1E1E").grid(row=0, column=0, sticky="w")
    website_entry = tk.Entry(card, width=40)
    website_entry.grid(row=0, column=1, pady=5)

    # App
    tk.Label(card, text="Application", fg="white", bg="#1E1E1E").grid(row=1, column=0, sticky="w")
    app_entry = tk.Entry(card, width=40)
    app_entry.grid(row=1, column=1, pady=5)

    # ---------------- TIME INPUT (H:M:S) ----------------

    time_frame = tk.Frame(root, bg="#121212")
    time_frame.pack(pady=10)

    tk.Label(time_frame, text="Hours", fg="white", bg="#121212").grid(row=0, column=0)
    hour_entry = tk.Entry(time_frame, width=6)
    hour_entry.grid(row=0, column=1, padx=5)

    tk.Label(time_frame, text="Min", fg="white", bg="#121212").grid(row=0, column=2)
    min_entry = tk.Entry(time_frame, width=6)
    min_entry.grid(row=0, column=3, padx=5)

    tk.Label(time_frame, text="Sec", fg="white", bg="#121212").grid(row=0, column=4)
    sec_entry = tk.Entry(time_frame, width=6)
    sec_entry.grid(row=0, column=5, padx=5)

    # ---------------- BUTTONS ----------------

    btn_frame = tk.Frame(root, bg="#121212")
    btn_frame.pack(pady=15)

    tk.Button(
        btn_frame,
        text="Block Website",
        command=block_website_ui,
        bg="#00C896",
        fg="black",
        width=18
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        btn_frame,
        text="Block App",
        command=block_app_ui,
        bg="#FF4D4D",
        fg="black",
        width=18
    ).grid(row=0, column=1, padx=10)

    # ---------------- ACTIVE BLOCKS ----------------

    tk.Label(
        root,
        text="Active Blocks",
        font=("Segoe UI", 14, "bold"),
        fg="white",
        bg="#121212"
    ).pack(pady=5)

    listbox = tk.Listbox(root, width=65, height=10)
    listbox.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    run_app()