#
# test_4
#

import FreeSimpleGUI as sg

# レイアウトの定義
layout = [
    [sg.Text('好きなフルーツを選んでください:')],
    [sg.Checkbox('りんご', default=True, key='-APPLE-')],
    [sg.Checkbox('バナナ', key='-BANANA-')],
    [sg.Checkbox('オレンジ', key='-ORANGE-')],
    [sg.Text('好きな飲み物を選んでください (いずれか一つ):')],
    [sg.Radio('コーヒー', "RADIO1", default=True, key='-COFFEE-')], # 同じグループ名("RADIO1")を指定
    [sg.Radio('紅茶', "RADIO1", key='-TEA-')],
    [sg.Radio('ジュース', "RADIO1", key='-JUICE-')],
    [sg.Button('選択を確定'), sg.Button('リセット')]
]

# ウィンドウの作成
window = sg.Window('選択肢のサンプル', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '選択を確定':
        selected_fruits = []
        if values['-APPLE-']:
            selected_fruits.append('りんご')
        if values['-BANANA-']:
            selected_fruits.append('バナナ')
        if values['-ORANGE-']:
            selected_fruits.append('オレンジ')

        selected_drink = ''
        if values['-COFFEE-']:
            selected_drink = 'コーヒー'
        elif values['-TEA-']:
            selected_drink = '紅茶'
        elif values['-JUICE-']:
            selected_drink = 'ジュース'

        msg = f"選択されたフルーツ: {', '.join(selected_fruits) if selected_fruits else 'なし'}\n"
        msg += f"選択された飲み物: {selected_drink if selected_drink else 'なし'}"
        sg.popup('あなたの選択', msg)

    if event == 'リセット':
        # 各要素の値を初期状態に戻す
        window['-APPLE-'].update(False)
        window['-BANANA-'].update(False)
        window['-ORANGE-'].update(False)
        window['-COFFEE-'].update(False) # ラジオボタンは一つしかTrueにならないので、どれか一つをFalseにすれば良い
        window['-TEA-'].update(False)
        window['-JUICE-'].update(False)
        window['-COFFEE-'].update(True) # デフォルト値をTrueに戻す
        sg.popup('リセットしました。')

# ウィンドウを閉じる
window.close()