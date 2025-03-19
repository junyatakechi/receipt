import os
import argparse
import json
from openai import OpenAI

def generate_blog_from_ingredients(ingredients_list, api_key=None):
    """
    食材のリストからOpenAI APIを使用してブログ記事を生成する関数
    
    Args:
        ingredients_list (list): 食材名のリスト
        api_key (str, optional): OpenAI APIキー
    
    Returns:
        str: 生成されたブログ記事
    """
    # APIキーの設定
    if api_key is None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("OpenAI APIキーが必要です。環境変数または引数で指定してください。")
    
    # OpenAIクライアントの初期化
    client = OpenAI(api_key=api_key)
    
    # 食材をカンマ区切りのテキストに変換
    ingredients_text = ", ".join(ingredients_list)
    
    # プロンプトの作成
    prompt = f"""
    以下の食材を使用した料理のブログ記事をマークダウン形式で書いてください:
    {ingredients_text}
    
    以下の構造に従って記事を作成してください:
    
    ```
    # [魅力的なタイトル]
    
    こんにちは、食いしん坊ブロガーのゆきです！今日は[料理の簡単な紹介]をご紹介します。
    
    ## 材料（2人分）
    - [食材1]
    - [食材2]
    - [以下続く]
    
    ## 作り方
    
    1. **[ステップ1のタイトル]**  
       [ステップ1の詳細説明]
    
    2. **[ステップ2のタイトル]**  
       [ステップ2の詳細説明]
    
    [以下、手順が続く]
    
    ## 食べ方のアレンジ
    
    [アレンジ方法の説明]
    
    ## 失敗しないコツ
    
    [コツやヒントの説明]
    
    [個人的なエピソードや体験談]
    
    [健康効果についての簡単な説明]
    
    [次回の予告など締めの一文]
    ```
    
    記事は親しみやすく温かみのある文体で、マークダウン形式を使って構造化してください。特に料理手順は箇条書きで詳しく説明し、個人的なエピソードも交えてください。
    """
    
    # OpenAI APIを呼び出して記事を生成
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # 最も安価なモデルを使用
        messages=[
            {"role": "system", "content": "あなたは料理と健康に詳しいプロのブロガーです。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1200
    )
    
    # 生成された記事を返す
    return response.choices[0].message.content

def save_blog_to_file(blog_content, output_file="blog_output.txt"):
    """
    生成されたブログ記事をファイルに保存する関数
    
    Args:
        blog_content (str): ブログ記事の内容
        output_file (str): 出力ファイル名
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(blog_content)
    print(f"ブログ記事が {output_file} に保存されました。")

def main():
    parser = argparse.ArgumentParser(description="食材リストからブログ記事を生成するツール")
    parser.add_argument("--ingredients", nargs="+", help="食材名のリスト", required=True)
    parser.add_argument("--api-key", help="OpenAI APIキー (設定されていない場合は環境変数から読み込みます)")
    parser.add_argument("--output", default="blog_output.txt", help="出力ファイル名")
    
    args = parser.parse_args()
    
    try:
        # ブログ記事の生成
        blog_content = generate_blog_from_ingredients(args.ingredients, args.api_key)
        
        # 結果を表示
        print("\n===== 生成されたブログ記事 =====\n")
        print(blog_content)
        print("\n===============================\n")
        
        # ファイルに保存
        save_blog_to_file(blog_content, args.output)
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()