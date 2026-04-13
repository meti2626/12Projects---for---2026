import tkinter as tk

from tkinter import messagebox
from logic import block_with_timer 
from logic import block_app_with_timer

def run_app():
  root =tk.Tk()
  root.title("Focus Blocker")

  root.geometry("500x400")

   
  def block_website_ui():
    site =  website_entry.get()

    site = site.replace("https://", "").replace("http://", "").replace("www.", "")

    time_val= time_entry.get()

    if not site or not time_val.isdigit():
       print("Please enter a valid website and time.")
       return
      


    block_with_timer(site, int(time_val) * 60)
    listbox.insert(tk.END, f"{site} - {time_val} min (BLOCKED)") 

## see what we used it for

    website_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)



  def block_app_ui():
      app = APP_entry.get()
      time_val = time_entry.get()

      if not app or not time_val.isdigit():
          messagebox.showerror("Error", "Enter valid app and time")
          return

      block_app_with_timer(app, int(time_val) * 60)

      listbox.insert(tk.END , f"{app} blocked for {time_val} minutes.")

      APP_entry.delete(0, tk.END)
      time_entry.delete(0, tk.END)


# -- Inputs --

  tk.Label(root, text = "Website").grid(row=0, column=0 )
  website_entry = tk.Entry(root)

  website_entry.grid(row=0, column=1)


  tk.Label(root ,text= "Application" ) .grid(row= 1,column =0)
  APP_entry = tk.Entry(root)
  APP_entry.grid(row=1, column=1)


  tk.Label(root , text =" Time (minutes) :").grid(row =2 ,column =0)
  time_entry = tk.Entry(root)
  time_entry.grid(row=2, column=1)

  # --- Buttons ---

  tk.Button(root , text = "Block website" , command =block_website_ui).grid(row=3, column=0)
  
  tk.Button(root , text = "Block Application" , command = block_app_ui).grid(row=3, column=1)



  # --- Listbox ---
  tk.Label(root, text="Active Blocks").grid(row=4, column=0)



  listbox = tk.Listbox(root ,width =  50) 
  listbox.grid(row=5, column=0, columnspan=2)

  root.mainloop()