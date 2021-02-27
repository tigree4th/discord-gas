# discord-gas

discord-gas は開発中のリポジトリです。
最終的に、Discord の投稿を読み取り、GAS を通してスプレッドシートに出力することを目的としています。

<br/>

## デモ

デモはまだありません。

<br/>

## 機能

### 最終目標

1. discord.py を使用し、DiscordBOT から自動的にメッセージを吸い上げる
2. 特定語句を判定し、条件に一致した場合に処理を行う
3. データベースやスプレッドシートへの書き出しを行う

<br/>

## 動作条件

- Python 3.7 以上の環境
- [discord.py](https://github.com/Rapptz/discord.py)

### discord.py のインストールについて

#### Windows 以外の環境

```shell
$ python3 -m pip install -U "discord.py[voice]"
```

#### Windows 環境

```shell
$ py -3 -m pip install -U discord.py[voice]
```

<br/>

## 関連公式ドキュメント

- [discord.py](https://discordpy.readthedocs.io/ja/latest/index.html)

<br/>

## 参考文献

- [Python で実用 Discord Bot(discordpy 解説)](https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f)
- [discord.py 入門](https://qiita.com/sizumita/items/9d44ae7d1ce007391699)
- [python3 の venv でプロジェクト毎にライブラリを管理する](https://akogare-se.hatenablog.com/entry/2019/01/02/220330)

<br/>

## 使い方

`discord-test.py`と同じ階層に下記のような環境変数設定用ファイル`.env`を作ってください。`DISCORD_ACCESS_TOKEN=`の後に DiscordAPP 用のアクセストークン、`DISCORD_CHANNEL_ID=`の後にターゲットとなるチャンネル ID を入力してください。

```env
DISCORD_ACCESS_TOKEN=
DISCORD_CHANNEL_ID=
```

<br/>

## 備考

Windows 環境および Linux 環境でテスト済みです。
このリポジトリは、まだ開発段階のリポジトリです。
