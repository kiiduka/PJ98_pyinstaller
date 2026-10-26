
pyinstaller で実行ファイルを作るときの変更箇所

１．モジュールのインポート行を変更する。

  # # スクリプトの親ディレクトリを取得しパスに追加する
　# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
　# # 共通モジュールをインポートする
　# from modules import module_1  # import modules.module_1

　# pyinstaller
　import module_1

２．イメージパスを変更する。

　# image_path = r".img/smash_hoshu_1.png"  # 納入物件受注残リスト
　image_path = module_1.resource_path("smash_hoshu_1.png")  # pyinstaller

３．実行方法

　1 ターミナルを開く。

　2 仮想環境 .venv に切り替える。
　   .venv\Scripts\activate

　3 初回は、pyinstaller test_2.py --onefile --icon=ico/test.icoを実行する。
    --onefile は、すべての依存ファイルを一つの実行ファイルにまとめる
    --icon は、アイコンファイルのパス

　4 specファイルが作成される。

　5 specファイルに、実行ファイルに入れる画像ファイルを記述する。
　
　6 以降は、pyinstaller test_2.spec を実行する。
