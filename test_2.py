#
# test_2
#

import FreeSimpleGUI as sg

# レイアウトの定義
layout = [
    [sg.Text('Hello, World! Welcome to FreeSimpleGUI.')],
    [sg.Button('OK'), sg.Button('終了')]
]

# ウィンドウの作成
window = sg.Window('My First FreeSimpleGUI Window', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '終了':  # ウィンドウが閉じられたか「終了」ボタンが押されたら
        break
    if event == 'OK':
        sg.popup('OKボタンが押されました！')  # ポップアップを表示

# ウィンドウを閉じる
window.close()
