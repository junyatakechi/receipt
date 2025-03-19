# 環境
## OpenAI
- APIキーを環境変数にセットする。
`export OPENAI_API_KEY=your-api-key-here`

## Python

- 仮想環境の有効化
`source .venv/bin/activate`

- 依存ライブラリのインストール
`pip install -r requirements.txt`

- ライブラリ依存関係の保存
`pip freeze > requirements.txt`

# サンプルコマンド

## textのHTML変換
`python src/md_to_html.py TestData/sample-blog.txt ./public/index.html`

## ブログ文章の生成
`python src/gen_blog_text.py --ingredients じゃがいも+たまねぎ+人参+豚肉`
