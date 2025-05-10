import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import Dzivoklis as dz
import LinkedListImplementation as ll
import mainFunctions as mf 

def start():
    win = tk.Tk()
    win.title("Dzīvokļu Meklētājs")

    da_big_list = None
    base_url = "https://www.ss.lv/lv/real-estate/flats/"

    # URL Input (Split Fixed + Editable)
    tk.Label(win, text="Region URL:").grid(row=0, column=0, sticky="w")
    url_frame = tk.Frame(win)
    url_frame.grid(row=0, column=1, columnspan=2, sticky="w")

    tk.Label(url_frame, text=base_url).pack(side=tk.LEFT)
    txt_district = tk.Entry(url_frame, width=40)
    txt_district.insert(0, "riga/purvciems/")
    txt_district.pack(side=tk.LEFT)

    tk.Label(win, text="How many pages:").grid(row=1, column=0, sticky="w")
    txt_pages = tk.Entry(win, width=10)
    txt_pages.insert(0, "3")
    txt_pages.grid(row=1, column=1, sticky="w")

    chk_var = tk.IntVar()
    chk_save = tk.Checkbutton(win, text="Save to file", variable=chk_var)
    chk_save.grid(row=2, column=1, sticky="w")

    tk.Label(win, text="Output:").grid(row=3, column=0, sticky="nw")
    txt_output = scrolledtext.ScrolledText(win, height=20, width=100)
    txt_output.grid(row=3, column=1, columnspan=2)

    tk.Label(win, text="Search method:").grid(row=4, column=0, sticky="w")
    cb_search = ttk.Combobox(win, values=["None", "findAnythingInt", "findIela", "findSerija"])
    cb_search.current(0)
    cb_search.grid(row=4, column=1, sticky="w")

    cb_cat = ttk.Combobox(win, values=["istabu_skaits", "laukums_m2", "cena_m2", "cena"])
    cb_op = ttk.Combobox(win, values=["=", "<", ">"])
    txt_search = tk.Entry(win, width=20)

    cb_cat.grid(row=5, column=1, sticky="w")
    cb_op.grid(row=5, column=1, sticky="e")
    txt_search.grid(row=6, column=1, sticky="w")

    cb_cat.grid_remove()
    cb_op.grid_remove()
    txt_search.grid_remove()

    def show_or_hide_stuff(event=None):
        what = cb_search.get()
        cb_cat.grid_remove()
        cb_op.grid_remove()
        txt_search.grid_remove()
        if what == "findAnythingInt":
            cb_cat.grid()
            cb_op.grid()
            txt_search.grid()
        elif what in ["findIela", "findSerija"]:
            txt_search.grid()

    cb_search.bind("<<ComboboxSelected>>", show_or_hide_stuff)

    def click_scrape():
        nonlocal da_big_list
        txt_output.delete("1.0", tk.END)
        da_path = txt_district.get()
        try:
            da_pages = int(txt_pages.get())
        except:
            messagebox.showerror("nope", "Pages must be a number.")
            return

        da_big_list = ll.LinkedList(None)
        da_big_list.pop()

        mf.howManyPagesToWorkWith(da_pages, base_url + da_path, da_big_list)

        if chk_var.get():
            mf.FromLinkedListOfObjectsWriteInCSVfile("output.csv", da_big_list)

        click_show_all()
        messagebox.showinfo("All done!", "Scraping complete!")

        # Enable buttons now
        btn_search.config(state=tk.NORMAL)
        btn_show.config(state=tk.NORMAL)

    def click_search():
        if not da_big_list:
            messagebox.showerror("Wait!", "Scrape something first!")
            return

        txt_output.delete("1.0", tk.END)

        def grab_printed(func):
            import io, sys
            buff = io.StringIO()
            sys.stdout = buff
            func()
            sys.stdout = sys.__stdout__
            return buff.getvalue()

        search_what = cb_search.get()
        if search_what == "findAnythingInt":
            result = grab_printed(lambda: mf.findAnythingInt(cb_cat.get(), txt_search.get(), cb_op.get(), da_big_list))
        elif search_what == "findIela":
            result = grab_printed(lambda: mf.findIela(txt_search.get(), da_big_list))
        elif search_what == "findSerija":
            result = grab_printed(lambda: mf.findSerija(txt_search.get(), da_big_list))
        else:
            result = "No search selected."

        txt_output.insert(tk.END, result)

    def click_show_all():
        if not da_big_list:
            messagebox.showerror("Nope", "Scrape first!")
            return
        txt_output.delete("1.0", tk.END)
        n = da_big_list.head
        while n:
            txt_output.insert(tk.END, ", ".join(n.value.DzivAllDataGetter()) + "\n")
            n = n.next

    def go_scrape_threaded():
        threading.Thread(target=click_scrape).start()

    # --- Buttons ---
    btn_row = tk.Frame(win)
    btn_row.grid(row=7, column=1, sticky="w", pady=10)

    tk.Button(btn_row, text="Start Scraping", command=go_scrape_threaded).pack(side=tk.LEFT, padx=5)
    btn_search = tk.Button(btn_row, text="Search", command=click_search, state=tk.DISABLED)
    btn_search.pack(side=tk.LEFT, padx=5)
    btn_show = tk.Button(btn_row, text="Show All", command=click_show_all, state=tk.DISABLED)
    btn_show.pack(side=tk.LEFT, padx=5)

    win.mainloop()

start()
