# 「sensortray」はCPU温度&#40;sensors&#41;を通知タスクトレイ&#40;Notify&#41;表示のPythonによる実装です。

## セットアップ方法

sensors&#40;lm&#95;sensors&#41;コマンドを使えるようにしておくこと。  
ほとんどのLinuxで公式パッケージから追加インストールできるはず。  
「lm&#95;sensors」の設定しなくても多分「sensors」コマンドでCPU温度「Core 0」は最初から取得できるはず。  

[lm sensors](https://wiki.archlinuxjp.org/index.php/Lm_sensors)  
>lm&#95;sensors (Linux monitoring sensors) は  
>温度、電圧、ファンを監視するフリーでオープンソースなツールとドライバです。  

[ハードウェアから温度情報などを取得する](http://gihyo.jp/admin/serial/01/ubuntu-recipe/0183)  
>Ubuntuに導入するには，UbuntuソフトウェアセンターやSynapticパッケージマネジャーで  
>パッケージ「lm-sensors」をインストールしてください。  

環境毎に表示テキストの空白数や摂氏温度記号の文字コードが違うなどの誤差があります。  

    Core0 Temp:   +65.0°C
    Core 0:         +35.0°C
    Core 0:      +47.0℃

「[sensortray.tsv](sensortray.tsv)」の「tempO」「tempC」項目の検索文字列を書き換えて誤差を吸収してください。  


## 操作方法。

通知タスクトレイ&#40;Notify&#41;左クリック→アイコン点滅条件の数値設定ウィンドウ表示。  
通知タスクトレイ&#40;Notify&#41;右クリック→数値設定初期化。  


## アイコン「sensorC.icl」関連&#40;Windows&#41;。

付録の「celdivsave.py」は「sensorC.png」を分割して「sensorC.icl」を作る過程で作ったツールです。  
「sensorC&#91;&#63;&#63;&#93;.png」をアイコンDLL「sensorC.icl」に変換するには別途Windows系のソフトが必要です。  
[複数のアイコンを簡単にICL/DLLファイルへまとめられる「アイコンパッキング」](http://www.forest.impress.co.jp/docs/review/20130822_612100.html)
>「アイコンパッキング」は、複数のICO形式のアイコンファイルを簡単に  
>1つのICL/DLLファイルへまとめられるソフト。  


## 動作環境。

Python 2.7.6&#40;Tahrpup6.0.5&#41;で動作を確認しています。  
「[LTsv/](LTsv/ "LTsv/"」フォルダ内のモジュールの詳細は「[LTsv10kanedit(tsvtool10)](https://github.com/ooblog/LTsv10kanedit "「LTsv10kanedit(tsvtool10)」は「L:Tsv」の読み書きを中心としたモジュール群と漢字エディタ「kanedit」のPythonによる実装の予定です。")」を参考。  

Windowsでは以下２点の理由で起動はすれど動作しません。  
1.Tkinterで通知タスクトレイ&#40;Notify&#41;クリックからのポップアップメニュー出現方法が不明。  
2.そもそもWindowsでCPU温度を所得する方法が不明。  


## ライセンス・著作権など。

Copyright (c) 2016 ooblog  
License: MIT  
[https://github.com/ooblog/sensortray/blob/master/LICENSE](https://github.com/ooblog/sensortray/blob/master/LICENSE "https://github.com/ooblog/sensortray/blob/master/LICENSE")  
