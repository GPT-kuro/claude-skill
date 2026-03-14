# AI News Pipelin

## 目的
# AI News Pipeline

## 目的
AIニュース記事を整理し、要約とSNS投稿コンテンツを生成する。

## 入力
- ニュースURL
- 記事本文

## 出力
- ニュース要約
- 重要ポイント
- X投稿案

## ワークフロー

### Step1 ニュース取得
ニュースURLまたは記事本文を入力

### Step2 要約生成
skills/ai-news-summary.md を使用

出力
- 3行要約
- 重要ポイント
- トレンド性

### Step3 投稿生成
skills/x-post-generator.md を使用

出力
- X投稿案
