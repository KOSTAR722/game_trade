import tkinter as tk
from tkinter import filedialog
import read_sheet
import script
import time
from datetime import datetime
import threading
# ループを管理するフラグ
running = False

# 特定の関数
def task():
    try:
            
        print(f"実行中: {datetime.now().strftime('%H:%M:%S')}")
        script.main(chrome_path_entry.get(),mode,read_sheet.main(sheet_url))
    except Exception as e:
        print(e)
        #if e==


def start_loop():
    global running
    global data
    if running:
        print("既に動作中です")
        return  # すでに実行中なら何もしない

    try:
        start_time = datetime.strptime(runtime_start_entry.get(), "%Y.%m.%d.%H:%M")
        end_time = datetime.strptime(runtime_end_entry.get(), "%Y.%m.%d.%H:%M")
        print("開始時刻:", start_time)
        print("終了時刻:", end_time)
    except ValueError:
        tk.messagebox.showerror("エラー", "時間は YYYY.mm.dd.HH:MM 形式で入力してください")
        return
    
    try:
        data=read_sheet.main(sheet_url)
    except Exception as e:
        print(e)
        tk.messagebox.showerror("エラー","URLを確認してください")
        return 

    running = True
    threading.Thread(target=loop_task, args=(start_time, end_time), daemon=True).start()

def loop_task(start_time, end_time):
    global running
    while running:
        now = datetime.now()
        if start_time <= now <= end_time:
            task()  # 特定の関数を実行
        time.sleep(1)  # 1秒ごとにチェック
        if now > end_time:  # 終了時間を過ぎたら停止
            running = False

def stop_loop():
    global running
    running = False

def browse_chrome_path():
    foldername = filedialog.askdirectory()
    chrome_path_entry.delete(0, tk.END)
    chrome_path_entry.insert(0, foldername)

def start_process():
    global chrome_path
    global sheet_url
    global mode
    chrome_path = chrome_path_entry.get()
    sheet_url = sheet_url_entry.get()
    interval_start = interval_start_entry.get()
    interval_end = interval_end_entry.get()
    mode = mode_var.get()

    start_loop()

# def execute_main(interval_start,interval_end,mode):

def complete_process():
    print("Process Completed")

root = tk.Tk()
root.title("出品フォーム")
root.geometry("300x400")

# Chromeのパス
chrome_path_label = tk.Label(root, text="Chromeのパス:")
chrome_path_label.grid(row=0, column=0, padx=2, pady=2, sticky='e')
chrome_path_frame = tk.Frame(root)
chrome_path_frame.grid(row=0, column=1, padx=2, pady=2, sticky='w')
chrome_path_entry = tk.Entry(chrome_path_frame, width=25)
chrome_path_entry.pack(side=tk.LEFT)
browse_button = tk.Button(chrome_path_frame, text="参照", command=browse_chrome_path)
browse_button.pack(side=tk.LEFT)

# シートURL
sheet_url_label = tk.Label(root, text="シートURL:")
sheet_url_label.grid(row=1, column=0, padx=2, pady=2, sticky='e')
sheet_url_entry = tk.Entry(root, width=30)
sheet_url_entry.grid(row=1, column=1, columnspan=2, padx=2, pady=2, sticky='w')

# モード選択（ラジオボタン）
mode_var = tk.StringVar(value="自動")
mode_label = tk.Label(root, text="モード:")
mode_label.grid(row=2, column=0, padx=2, pady=2, sticky='e')
mode_frame = tk.Frame(root)
mode_frame.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky='w')
auto_radio = tk.Radiobutton(mode_frame, text="自動", variable=mode_var, value="自動")
auto_radio.pack(side=tk.LEFT)
manual_radio = tk.Radiobutton(mode_frame, text="手動", variable=mode_var, value="手動")
manual_radio.pack(side=tk.LEFT)

# 出品時間の間隔（左寄せ）
interval_label = tk.Label(root, text="出品間隔:")
interval_label.grid(row=3, column=0, padx=2, pady=2, sticky='e')
interval_frame = tk.Frame(root)
interval_frame.grid(row=3, column=1, columnspan=4, padx=2, pady=2, sticky='w')
interval_start_entry = tk.Entry(interval_frame, width=5)
interval_start_entry.insert(0, "10")
interval_start_entry.pack(side=tk.LEFT)
interval_start_label = tk.Label(interval_frame, text="分から")
interval_start_label.pack(side=tk.LEFT)
interval_end_entry = tk.Entry(interval_frame, width=5)
interval_end_entry.insert(0, "10")
interval_end_entry.pack(side=tk.LEFT)
interval_end_label = tk.Label(interval_frame, text="分まで")
interval_end_label.pack(side=tk.LEFT)

# ツール稼働時間
runtime_label = tk.Label(root, text="ツール稼働時間:")
runtime_label.grid(row=4, column=0, padx=2, pady=2, sticky='e')
runtime_start_label = tk.Label(root, text="開始時間:")
runtime_start_label.grid(row=5, column=0,padx=2, pady=2, sticky='e')
runtime_start_entry = tk.Entry(root, width=20)
runtime_start_entry.insert(0, "10")
runtime_start_entry.grid(row=5, column=1,padx=2, columnspan=3,pady=2, sticky='w')
runtime_end_label = tk.Label(root, text="停止時間:")
runtime_end_label.grid(row=6, column=0,padx=2, pady=2, sticky='e')
runtime_end_entry = tk.Entry(root, width=20)
runtime_end_entry.insert(0, "10")
runtime_end_entry.grid(row=6, column=1,padx=2, columnspan=3,pady=2, sticky='w')


# 開始ボタン
start_button = tk.Button(root, text="開始", command=start_process)
start_button.grid(row=7, column=0,pady=2,columnspan=2)

# 完了ボタン
complete_button = tk.Button(root, text="完了", command=complete_process)
complete_button.grid(row=7, column=1,pady=2)



root.mainloop()
