import os
import argparse
from gen_blog_text import generate_blog_from_ingredients
from md_to_html import convert_markdown_to_html

def create_blog_html_usecase():
    parser = argparse.ArgumentParser(description="食材リストからブログ記事を生成し、HTMLに変換するツール")
    parser.add_argument("--ingredients", nargs="+", help="食材名のリスト", required=True)
    parser.add_argument("--api-key", help="OpenAI APIキー (設定されていない場合は環境変数から読み込みます)")
    
    args = parser.parse_args()

    blog_content: str = generate_blog_from_ingredients(args.ingredients, args.api_key)
    full_html: str = convert_markdown_to_html(blog_content)
    
    
    output_file = "./public/index.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
        
    print("Done")
    

if __name__ == "__main__":
    create_blog_html_usecase()