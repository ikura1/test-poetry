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

### 既存プロジェクトの開始

たぶん?
'poetry init'

### 別環境での構築

'poetry install'

## ライブラリの変更

### ライブラリのインストール

'poetry add requests'
'poetry add --dev --allow-prereleases black'
