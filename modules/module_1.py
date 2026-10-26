#
# 共通モジュール１
#

import sys
import os
import time
import pyautogui as pag  # opencv-pythonとpillowも入れる
import ctypes  # MS-IMEの漢字オフで使う

# 画像認識精度は、１に近いほど高精度になるが、
# 高精度に設定し過ぎると、認識できなくて止まる
#  0.83 --> 0.81 --> 0.8 --> 0.82 --> 0.83
yomitori_seido = 0.83

# MS-IMEの漢字オフの設定値
VK_IME_OFF = 0x1A  # 「IMEをオフにする」という仮想キーの番号
KEYEVENTF_KEYUP = 0x0002  # 「キーを離した」という動作を表すフラグ
WM_IME_CONTROL = 0x0283  # 「IMEを制御せよ」というメッセージの種類
IMC_SETOPENSTATUS = 0x0006  # IME制御の中の「オン/オフの状態を設定する」という命令

# 使用するIMEを設定する　"google" or "ms"
IME_TYPE = "google"


# IME_TYPE = "ms"

# 画像の中心座標を返す
# 見つからない場合は、x,yをNoneで返す
def image_detect(image_path):
    try:
        location = pag.locateCenterOnScreen(image_path, confidence=yomitori_seido)
        if location is not None:
            # print("画像あり")
            x, y = location
            time.sleep(0.2)
            return True, x, y  # 画像の中心座標を返す
        else:
            # print("画像なし")
            time.sleep(0.2)
            return False, None, None  # x, yをNoneで返す
    except pag.ImageNotFoundException:
        # print("画像なし")
        time.sleep(0.2)
        return False, None, None  # x, yをNoneで返す
    except Exception as e:
        print(f"その他エラー: {e}")
        time.sleep(0.2)
        return False, None, None  # x, yをNoneで返す


# 画像が見つかるまで待つ
# 見つかったら中心座標を返す
def image_wait(image_path):
    loop_count = 1
    time_out = 1
    detect, x, y = False, None, None  # 戻り値の変数を初期化
    # Falseでループして、Trueで抜ける
    while not detect:
        detect, x, y = image_detect(image_path)
        print(f"\r実行中 {loop_count}   ", end="", flush=True)
        loop_count += 1

        if time_out == 180:
            print("\nタイムアウト終了")
            sys.exit()
        time_out += 1

        # print("")
        # print(f"image_path = {image_path}")
        # print(f"detect = {detect}")
        # print(f"x = {x}")
        # print(f"y = {y}")
        # print("")
        time.sleep(0.2)
    time.sleep(1)
    return detect, x, y  # 画像の中心座標を返す


# 画像が見つかるまで縦スクロールして待つ
# 見つかったら中心座標を返す
def image_wait_scroll(image_path):
    loop_count = 1
    time_out = 1
    detect, x, y = False, None, None  # 戻り値の変数を初期化
    # Falseでループして、Trueで抜ける
    while not detect:
        detect, x, y = image_detect(image_path)
        print(f"\r実行中 {loop_count}      ", end="", flush=True)
        loop_count += 1

        if time_out == 120:
            print("\nタイムアウト終了")
            sys.exit()
        time_out += 1

        pag.scroll(-20)  # 縦スクロール
        time.sleep(0.2)
    time.sleep(1)
    return detect, x, y  # 画像の中心座標を返す


# MS-IMEの漢字オフ
def ms_ime_off():
    # DLLを使えるように読み込む
    user32 = ctypes.windll.user32
    imm32 = ctypes.windll.imm32

    # IMEオフキーを送る
    user32.keybd_event(VK_IME_OFF, 0, 0, 0)  # IMEオフキーを押す
    user32.keybd_event(VK_IME_OFF, 0, KEYEVENTF_KEYUP, 0)  # キーを離す
    time.sleep(0.2)

    # IMEを直接オフにする（念のため）
    hwnd = user32.GetForegroundWindow()  # アクティブなウィンドウを取得
    ime_wnd = imm32.ImmGetDefaultIMEWnd(hwnd)  # そのウィンドウのIME窓口を取得
    user32.SendMessageW(ime_wnd, WM_IME_CONTROL, IMC_SETOPENSTATUS, 0)  # オフの命令を送る
    time.sleep(0.2)


# Google日本語入力の漢字オフ
# Google日本語入力に、予め Ctrl+Shift+F12 を追加設定しておく
def google_ime_off():
    pag.hotkey("ctrl", "shift", "f12")
    time.sleep(0.2)


# 漢字オフ　IME_TYPEの設定値で呼び分ける
def ime_off():
    if IME_TYPE == "google":
        google_ime_off()
    else:
        ms_ime_off()


# 作ったけど使わない
# print("\b\b\b\b\b\b\b\b\b\b\b\b") の代替
# 直前の表示が\rのとき、行頭に戻って上書き表示する
def msg_show(msg):
    print("\r" + msg + " " * 30)


# ウィンドウ操作
def window_operations(window_title):
    window = next((win for win in pag.getAllWindows() if window_title in win.title), None)
    if window:
        window.moveTo(0, 0)  # ウィンドウを画面の左上隅に移動
        time.sleep(0.5)
        window.activate()  # ウィンドウをアクティブ化
        time.sleep(0.5)
        window.maximize()  # 最大化
        time.sleep(0.5)
    else:
        print(f"\n{window_title} が見つかりません")
        time.sleep(0.5)
    return


# # pyinstaller 対応
# def resource_path(relative_path):
#     # PyInstallerでファイルを含めた場合のリソースパスを取得
#     try:
#         # PyInstallerでの一時ディレクトリパス
#         base_path = sys._MEIPASS
#     except Exception:
#         # 通常の開発環境用パス
#         base_path = os.path.abspath("../.img")
#     return os.path.join(base_path, relative_path)


# Nuitka 対応
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # Nuitka --onefile でフリーズされた場合
        # sys.executable は一時ディレクトリ内の実行ファイルへのパス
        # そのディレクトリ内にバンドルされた .img フォルダがあるはず
        base_path = os.path.dirname(sys.executable)
        # .img フォルダは実行ファイルと同じ階層に展開されると想定
        return os.path.join(base_path, ".img", relative_path)
    else:
        # 通常の開発環境の場合
        # スクリプトの親ディレクトリにある .img フォルダを参照
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".img", relative_path))
