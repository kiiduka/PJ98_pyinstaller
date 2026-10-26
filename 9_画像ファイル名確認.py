# 
# 画像ファイル名　確認
# 

import os
import re

# このスクリプトと同じフォルダにあるファイルを対象にする
current_dir = os.path.dirname(os.path.abspath(__file__))

# 調べるファイルを指定する
# file_path = os.path.join(current_dir, '3_ファイル加工.py')
file_path = os.path.join(current_dir, '3_登録_２作業.py')

# ファイル存在チェック
if not os.path.exists(file_path):
    print("ファイルが見つかりません。パスを確認してください。")
    exit()

# .png ファイル名を格納するセット
png_files = set()

# ファイルを読み込んで .png を抽出
with open(file_path, 'r', encoding='utf-8-sig') as f:
    content = f.read()
    # ダブルクォートかシングルクォートに囲まれた .png を探す
    matches = re.findall(r'"([^"]+\.png)"|\'([^\']+\.png)\'', content)
    for match in matches:
        png_files.add(match[0] or match[1])

# 結果をソートして表示
print("\n.pngファイル名一覧（ソート済み）:")
for name in sorted(png_files):
    print(name)
