to2.pw
====

最短2文字(ドメインを除く)の短縮URLを作成できるウェブアプリです([to2.pw](https://to2.pw) / [ee.sb](https://ee.sb)にて利用できます)

## 説明
有効時間により発行される短縮URLの長さが変わります, 有効期限を3時間に設定するとドメイン + 2文字の短縮URLを発行することができます.

## 利用技術
* Django
* Nuxt


## 起動方法

docker-composeを使用しています

### 開発環境
`docker-compose up -f docker-compose.dev.yml up`


### 本番環境
`docker-compose up -f docker-compose.deploy.yml up`

## ライセンス

AGPL
