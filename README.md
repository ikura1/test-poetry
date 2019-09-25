# poetry

## はじめに

pipenv と比較されることをよく見る気がする poetry を試していく。
poetry を試すだけだとライブラリのインストールする必要がないたので、最近知った RakutenRapidAPI で載っている API を試してみようと思ったけど、よくわからんかったので yesnoAPI を叩いた。

## 流れ

- インストール
- ライブラリインストール
- 別環境での環境構築

## インストール

インストール
'pip install poetry'

'pip install'で入れた poetry の場合下記のエラーが出力された。

0.11.5 から 0.12 にアップグレードできなくて、ダメになったっぽい。
[releas note](https://poetry.eustace.io/blog/poetry-0-12-0-is-out.html)

再インストールするべし
'pip3 uninstall poetry'
'pip3 install poetry'
'poetry -V'

## 設定

### completion の設定

'poetry completion bash > \$(brew --prefix)/etc/bash_completion.d/poetry.bash-completion'

### 仮想環境

設定ファイルの確認を行う。存在しない場合、作成されるため実行する。
'poetry config --list'
'settings.virtualenvs.create = true
settings.virtualenvs.in-project = false
settings.virtualenvs.path = "/Users/ikura1/Library/Caches/pypoetry/virtualenvs"
repositories = {}'
'poetry config settings.virtualenvs.in-project true'

## ライブラリのインストール・環境構築

Pipenv では独自ファイルの Pipfile を作成される形でしたが、Poetry では pyproject.toml に記載していく形で構成を記述していきます。
vscode で toml が format されない。まずプレーンテキストとして認識される。formatter を作るチャンスか?ConfigParser で読み込みと作成を行えば、おわりな気もする。

### 新規プロジェクトの開始

いい感じに下記のコマンドでテンプレートが作成される。便利
README が md ではなく、rst なのが少し不満
'poetry new new-project'

### Pipenv プロジェクトからの移行

移行ツールを作っている方がいらしたので、使わせていただきます。
[Pipenv から Poetry への引越しツールを作った](http://kk6.hateblo.jp/entry/2019/01/16/191452)
'
pip3 install poetrify
poetrify generate
'
'
Generated init command:

poetry init --dependency=bullet --dev-dependency=black
'
なるほど、Pipfile を解釈して'poetry init'コマンドを作成する形ですか。

## プロジェクトの開始

'poetry new hoge'

### 環境構築

初期設定から始める場合に使用する。
項目は一個ずつ設定していく。
'poetry init'
'
This command will guide you through creating your pyproject.toml config.

Package name [test-bullet]:
Version [0.1.0]:
Description []:
Author [Yuki Okuda <y-okuda@glad-cube.com>, n to skip]: ikura1
License []:
'

## ライブラリの変更

### ライブラリのインストール

'poetry add requests'
'poetry add --dev --allow-prereleases black'
