import time 

import pygetwindow as gw


distraction_keyword = ["YouTube", "Instagram", "TikTok", "Facebook"]


def is_distraction(app_name):
    for keyword in distraction_keyword:
        if keyword.lower() in app_name.lower():
            return True
    return False

def get_active_window():
    try:
       window = gw.getActiveWindow()  
       if window:
            return window.title
       return "No active window"
    except:
       return "Error getting window"   

app_time = {}

last_window = ""

while True:
    active_window = get_active_window()

    if active_window not in app_time:
        app_time[active_window] = 0

    app_time[active_window] += 1


    if active_window != last_window:
       print("\n--- App Usage ---")
       for app, seconds in app_time.items():
         if is_distraction(app):
             print(f"{app}: {seconds} seconds (Distraction)")
         else:         
            
             print(f"{app}: {seconds} seconds  -- not distraction")




         last_window = active_window
    time.sleep(1)     