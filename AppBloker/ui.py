import tkinter as tk

def run_app():
  root =tk.Tk()
  root.title("Focus Blocker")

  root.geometry("500x400")

   
  def block_website_ui():
    site =  website_entry.get()
    time_val= time_entry.get()

    if not site or not time_val.isdigit():
       print("Please enter a valid website and time.")
       return
      


    listbox.insert(tk.END,f"{site} blocked for {time_val} minutes.")  

    website_entry.delete(0, tk.END)
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

block_site_btn  = tk.Button(root , text = "Block website")
block_site_btn.grid( row= 3 ,column =0 )


block_app_btn = tk.Button(root, text="Block App")
block_app_btn.grid(row=3, column=1)

# --- Listbox ---
tk.Label(root, text="Active Blocks").grid(row=4, column=0)



listbox = tk.Listbox(root ,width =  50) 
listbox.grid(row=5, column=0, columnspan=2)

root.mainloop()