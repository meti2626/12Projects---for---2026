import tkinter as tk
from tkinter import messagebox
from logic import block_with_timer, block_app_with_timer

# ---------------- GLOBAL TIMER ----------------
selected_time = {"h": 0, "m": 0, "s": 0}


def run_app():
    root = tk.Tk()
    root.title("Focus Blocker Pro")
    root.geometry("700x550")
    root.configure(bg="#0f172a")  # deep modern dark

    # ---------------- STYLE HELPERS ----------------

    def style_entry(e):
        e.configure(
            bg="#1e293b",
            fg="white",
            insertbackground="white",
            relief="flat",
            font=("Segoe UI", 11)
        )

    def style_button(btn, color):
        btn.configure(
            bg=color,
            fg="white",
            activebackground=color,
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            padx=10,
            pady=6
        )

    # ---------------- TIME POPUP ----------------

    def open_time_popup():
        popup = tk.Toplevel(root)
        popup.title("Set Time")
        popup.geometry("300x220")
        popup.configure(bg="#111827")
        popup.grab_set()  # modal

        tk.Label(
            popup,
            text="Set Timer",
            font=("Segoe UI", 14, "bold"),
            fg="white",
            bg="#111827"
        ).pack(pady=10)

        frame = tk.Frame(popup, bg="#111827")
        frame.pack(pady=10)

        h_var = tk.StringVar(value="0")
        m_var = tk.StringVar(value="0")
        s_var = tk.StringVar(value="0")

        def create_box(var):
            e = tk.Entry(frame, textvariable=var, width=3, justify="center")
            style_entry(e)
            return e

        h = create_box(h_var)
        h.grid(row=0, column=0, padx=5)

        tk.Label(frame, text=":", fg="white", bg="#111827").grid(row=0, column=1)

        m = create_box(m_var)
        m.grid(row=0, column=2, padx=5)

        tk.Label(frame, text=":", fg="white", bg="#111827").grid(row=0, column=3)

        s = create_box(s_var)
        s.grid(row=0, column=4, padx=5)

        def save_time():
            try:
                selected_time["h"] = int(h_var.get())
                selected_time["m"] = int(m_var.get())
                selected_time["s"] = int(s_var.get())
                popup.destroy()
            except:
                messagebox.showerror("Error", "Invalid time values")

        btn = tk.Button(popup, text="Set", command=save_time)
        style_button(btn, "#22c55e")
        btn.pack(pady=15)

    # ---------------- LOGIC ----------------

    def get_seconds():
        h = selected_time["h"]
        m = selected_time["m"]
        s = selected_time["s"]
        return (h * 3600) + (m * 60) + s, h, m, s

    def block_website_ui():
        site = website_entry.get().strip()
        site = site.replace("https://", "").replace("http://", "").replace("www.", "")

        duration, h, m, s = get_seconds()

        if duration == 0:
            messagebox.showerror("Error", "Set time first")
            return

        if not site:
            messagebox.showerror("Error", "Enter a website")
            return

        block_with_timer(site, duration)
        listbox.insert(tk.END, f"🌐 {site} → {h}h {m}m {s}s BLOCKED")
        website_entry.delete(0, tk.END)

    def block_app_ui():
        app = app_entry.get().strip()

        duration, h, m, s = get_seconds()

        if duration == 0:
            messagebox.showerror("Error", "Set time first")
            return

        if not app:
            messagebox.showerror("Error", "Enter an application name")
            return

        block_app_with_timer(app, duration)
        listbox.insert(tk.END, f"📱 {app} → {h}h {m}m {s}s BLOCKED")
        app_entry.delete(0, tk.END)

    # ---------------- TITLE ----------------

    tk.Label(
        root,
        text="Focus Blocker Pro",
        font=("Segoe UI", 24, "bold"),
        fg="white",
        bg="#0f172a"
    ).pack(pady=20)

    # ---------------- CARD ----------------

    card = tk.Frame(root, bg="#1e293b", padx=20, pady=20)
    card.pack(padx=30, pady=10, fill="x")

    # Website
    tk.Label(card, text="Website", fg="#cbd5f5", bg="#1e293b").grid(row=0, column=0, sticky="w")
    website_entry = tk.Entry(card, width=40)
    style_entry(website_entry)
    website_entry.grid(row=1, column=0, pady=5)

    tk.Button(card, text="Set Time", command=open_time_popup, width=12)
    style_button(card.grid_slaves(row=1, column=1)[0] if card.grid_slaves(row=1, column=1) else tk.Button(card), "#334155")

    set_time_btn1 = tk.Button(card, text="Set Time", command=open_time_popup)
    style_button(set_time_btn1, "#334155")
    set_time_btn1.grid(row=1, column=1, padx=10)

    # App
    tk.Label(card, text="Application", fg="#cbd5f5", bg="#1e293b").grid(row=2, column=0, sticky="w", pady=(10, 0))
    app_entry = tk.Entry(card, width=40)
    style_entry(app_entry)
    app_entry.grid(row=3, column=0, pady=5)

    set_time_btn2 = tk.Button(card, text="Set Time", command=open_time_popup)
    style_button(set_time_btn2, "#334155")
    set_time_btn2.grid(row=3, column=1, padx=10)

    # ---------------- ACTION BUTTONS ----------------

    btn_frame = tk.Frame(root, bg="#0f172a")
    btn_frame.pack(pady=20)

    btn1 = tk.Button(btn_frame, text="Block Website", command=block_website_ui, width=18)
    style_button(btn1, "#22c55e")
    btn1.grid(row=0, column=0, padx=10)

    btn2 = tk.Button(btn_frame, text="Block App", command=block_app_ui, width=18)
    style_button(btn2, "#ef4444")
    btn2.grid(row=0, column=1, padx=10)

    # ---------------- LIST ----------------

    tk.Label(
        root,
        text="Active Blocks",
        font=("Segoe UI", 14, "bold"),
        fg="white",
        bg="#0f172a"
    ).pack(pady=10)

    listbox = tk.Listbox(
        root,
        width=70,
        height=10,
        bg="#1e293b",
        fg="white",
        relief="flat",
        highlightthickness=0
    )
    listbox.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    run_app()