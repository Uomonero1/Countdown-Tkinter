from datetime import date
import tkinter as tk

today = date.today()
window = tk.Tk()
window.title("Countdown")
window.resizable(width=False, height=False)

def countdown():
    day = int(entry_day.get())
    month = int(entry_month.get())
    year = int(entry_year.get())
    desired_date = date(year, month, day)
    time_delta = abs(desired_date - today)
    label_result["text"] = f"{time_delta} until {desired_date}"
    print(time_delta)

# DAY
window.columnconfigure(0, weight=1, minsize=100)
window.rowconfigure(0, weight=1, minsize=100)
frame = tk.Frame(master=window)
frame.grid(row=0, column=0, padx=10)
label_day = tk.Label(master=frame, text="Enter a day")
label_day.pack()
entry_day = tk.Entry(master=frame)
entry_day.pack()


# MONTH
window.columnconfigure(0, weight=1, minsize=100)
window.rowconfigure(1, weight=1, minsize=100)
frame_month = tk.Frame(master=window)
frame_month.grid(row=1, column=0, padx=10)
label_month = tk.Label(master=frame_month, text="Enter a month")
label_month.pack()
entry_month = tk.Entry(master=frame_month)
entry_month.pack()


# YEAR
window.columnconfigure(0, weight=1, minsize=100)
window.rowconfigure(2, weight=1, minsize=100)
frame_year = tk.Frame(master=window)
frame_year.grid(row=2, column=0, padx=10)
label_year = tk.Label(master=frame_year, text="Enter a year")
label_year.pack()
entry_year = tk.Entry(master=frame_year)
entry_year.pack()

# RESULT
window.columnconfigure(0, weight=1, minsize=100)
window.rowconfigure(3, weight=1, minsize=100)
frame_result = tk.Frame(master=window)
frame_result.grid(row=3, column=0, padx=10)
label_result = tk.Label(master=frame_result, text="Result")
label_result.pack()

# ENTER BUTTON
frame_btn = tk.Frame(master=window)
frame_btn.grid(row=1, column=2, padx=10)
enter_btn = tk.Button(master=frame_btn, text="Enter", width=5, height=2, fg="Navy", command=countdown)
enter_btn.pack()



window.mainloop()