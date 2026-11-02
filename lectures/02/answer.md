# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）：
- 自分で学習を実行したか（`executed_training_myself`）：はい / いいえ（実行できた範囲：　）
- 学習前：`format_rate` =　 / `content_rate` =　
- 学習後：`format_rate` =　 / `content_rate` =　
- 退行した質問：
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：
- 学習で変わったこと・変わらなかったこと：

## 宿題

- 取り組んだレベル：基礎
- 変えた設定やデータ：num_train_epochs
- 結果（比較表や数字）：
値変更前のresulut.json
{
  "config": {
    "base_model": "Qwen/Qwen3.5-0.8B",
    "revision": "2fc06364715b967f1860aea9cf38778875588b17",
    "seed": 42,
    "num_train_epochs": 20,
    "warmup_steps": 6,
    "lr": 0.0002,
    "lora_r": 16,
    "lora_alpha": 32,
    "max_seq_len": 512,
    "max_new_tokens": 96,
    "gen": {
      "do_sample": false
    }
  },
  "versions": {
    "transformers": "5.18.0",
    "peft": "0.21.1",
    "trl": "1.14.2",
    "torch": "2.11.0+cu130"
  },
  "method": "LoRA（量子化なし）",
  "before": {
    "label": "before",
    "n": 21,
    "format_rate": 0.09523809523809523,
    "content_rate": 0.0,
    "both_rate": 0.0,
    "seconds": 21.1
  },
  "after": {
    "label": "after",
    "n": 21,
    "format_rate": 1.0,
    "content_rate": 0.9047619047619048,
    "both_rate": 0.9047619047619048,
    "seconds": 48.4
  },
  "regressed": [],
  "executed_training_myself": true
}
値変更後のresulut.json

{
  "config": {
    "base_model": "Qwen/Qwen3.5-0.8B",
    "revision": "2fc06364715b967f1860aea9cf38778875588b17",
    "seed": 42,
    "num_train_epochs": 1,
    "warmup_steps": 6,
    "lr": 0.0002,
    "lora_r": 16,
    "lora_alpha": 32,
    "max_seq_len": 512,
    "max_new_tokens": 96,
    "gen": {
      "do_sample": false
    }
  },
  "versions": {
    "transformers": "5.18.0",
    "peft": "0.21.1",
    "trl": "1.14.2",
    "torch": "2.11.0+cu130"
  },
  "method": "LoRA（量子化なし）",
  "before": {
    "label": "before",
    "n": 21,
    "format_rate": 0.9047619047619048,
    "content_rate": 0.6666666666666666,
    "both_rate": 0.6666666666666666,
    "seconds": 34.4
  },
  "after": {
    "label": "after",
    "n": 21,
    "format_rate": 0.9047619047619048,
    "content_rate": 0.6666666666666666,
    "both_rate": 0.6666666666666666,
    "seconds": 29.2
  },
  "regressed": [],
  "executed_training_myself": true
}
- 気づき
　当然かもしれないが学習のループの回数を減らすことによって
　format_rateとcontent_rateがともに若干低下する。
　適度が学習ループの数を定義することが大事なんだと思った。

- ファインチューニングが向く場面・向かない場面についての考察：
　ファインチューニングはやはりデータが少ない場面では向かないことがわかった。
　かつファインチューニングをしたからといって日付など変動する値に対する対応は苦手で
　あくまでもある一定のテンプレート化される行為に対してファインチューニングをしていくことで一定の効果がみれらることが分かった。



- 
以下の部分で何をどう学習されているのかがわからなかった。（コードベースでどこから学習データを取得し、どうデータが学習しているのかがわからなかったの意味。今後学習する。）
4. LoRA 学習（T4 で 4〜5 分）
