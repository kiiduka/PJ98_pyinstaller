#
# test_3
#

import FreeSimpleGUI as sg

# レイアウトの定義
layout = [
    [sg.Text('あなたの名前を入力してください:')],
    [sg.InputText(key='-NAME-')],  # 入力フィールド。keyで値を取得する。
    [sg.Button('送信'), sg.Button('キャンセル')]
]

# ウィンドウの作成
window = sg.Window('名前入力フォーム', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'キャンセル':
        break
    if event == '送信':
        name = values['-NAME-']  # '-NAME-'というkeyで入力された値を取得
        if name:  # 名前が入力されているか確認
            sg.popup(f'こんにちは、{name}さん！')
        else:
            sg.popup_error('名前が入力されていません。')

# ウィンドウを閉じる
window.close()
