# slack reposter

## 概要
仕様変更により2022年から過去の90日以上古い投稿が見えなくなった
自動的に再投稿することで,上記制限を回避することが目的。

## 詳細
現状特定のWSの自己紹介用のチャンネルを利用し、以下の作業を
定期的(90日以内で不定期)に実行している

- 自己紹介チャンネル->過去自己紹介チャンネル
- 過去自己紹介チャンネル->過去自己紹介チャンネル


## 自動テスト
現状なしだが作成中

## デプロイ
特になし

## TODO
* clientはWebClientですべて統一したい
  * WebhookClientで取得した投稿をWebClientで書き込みしているため