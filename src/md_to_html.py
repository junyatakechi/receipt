import markdown
import sys
from pathlib import Path

def convert_markdown_to_html(markdown_content: str, output_file=None) -> str:
    """
    Markdownコンテンツを受け取り、HTMLに変換します
    
    Parameters:
        markdown_content (str): 変換するMarkdownテキスト
        output_file (str, optional): 出力するHTMLファイルのパス。指定しない場合は結果を返します。
    
    Returns:
        str: HTMLコンテンツ（output_fileが指定されていない場合）
    """
    # Markdownを拡張機能付きでHTMLに変換
    html = markdown.markdown(
        markdown_content,
        extensions=['extra', 'nl2br', 'sane_lists']
    )
    
    # HTMLの完全な構造を作成
    full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>料理ブログ</title>
    <style>
        body {{
            font-family: 'Hiragino Sans', 'Hiragino Kaku Gothic ProN', Meiryo, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1 {{
            color: #e67e22;
            border-bottom: 2px solid #e67e22;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #e67e22;
            margin-top: 30px;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin: 20px 0;
        }}
        ol, ul {{
            padding-left: 25px;
        }}
        li {{
            margin-bottom: 10px;
        }}
        strong {{
            color: #d35400;
        }}
    </style>
</head>
<body>
    {html}
</body>
</html>
    """
    
    # ファイルに出力するか、文字列として返すか
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        return f"HTMLファイルが正常に作成されました: {output_file}"
    else:
        return full_html

def main():
    """
    コマンドラインから実行する場合のメイン関数
    使用例: python md_to_html.py input.md output.html
    """
    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) >= 3 else input_file.replace('.md', '.html')
        
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                md_content = f.read()
            
            result = convert_markdown_to_html(md_content, output_file)
            print(result)
        except Exception as e:
            print(f"エラーが発生しました: {e}")
    else:
        print("引数が足りません。")

if __name__ == "__main__":
    main()