#
# 漢字オンオフのテスト
#

import sys
import os
import time
import pyautogui as pag  # opencv-pythonとpillowも入れる

# スクリプトの親ディレクトリを取得しパスに追加する
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# 共通モジュールをインポートする
from modules import module_1  # import modules.module_1

# 少し待つ
time.sleep(1)

# 漢字オン　日本語ＫＢ／英語ＫＢ
pag.hotkey("kanji")
# print("\b\b\b\b\b\b\b\b\b\b\b\b漢字オン　日本語／英語")
module_1.msg_show("漢字オン　日本語／英語")
time.sleep(1)

# # 漢字オン　英語ＫＢ
# pag.hotkey("alt","`")
# print("\b\b\b\b\b\b\b\b\b\b\b\b漢字オン　英語")
# time.sleep(1)

# 漢字オフ
module_1.ime_off()
# print("\b\b\b\b\b\b\b\b\b\b\b\b漢字オフ")
module_1.msg_show("漢字オフ")
time.sleep(1)

# 画像 test_1.png を探す
# image_path = r".img/test_1.png"  # OCR
# image_path = module_1.resource_path("test_1.png")  # OCR
image_path = module_1.resource_path("test_1.png")  # Nuitka 対応
detect, x, y = module_1.image_wait(image_path)
pag.click(x + 0, y + 0, button="left")
time.sleep(0.5)

# 画像 test_2.png を探す
# image_path = r".img/test_2.png"  # pdf_txt_writer
# image_path = module_1.resource_path("test_2.png")  # pdf_txt_writer
image_path = module_1.resource_path("test_2.png")  # Nuitka 対応
detect, x, y = module_1.image_wait(image_path)
pag.click(x + 0, y + 0, button="left")
time.sleep(0.5)

#  画像 test_3.png を探す
# image_path = r".img/test_3.png"  # gr121
# image_path = module_1.resource_path("test_3.png")  # gr121
image_path = module_1.resource_path("test_3.png")  # Nuitka 対応
detect, x, y = module_1.image_wait(image_path)
pag.click(x + 0, y + 0, button="left")
time.sleep(0.5)
