from pathlib import Path
import sys

errors = []
warnings = []

target_dirs = ["skills", "prompts", "project"]

required_sections_by_type = {
    "PROJECT_INSTRUCTIONS.md": ["## 目的", "## トーン・文体", "## 出力ルール", "## 禁止事項"],
}

common_required_words = {
    "prompts": ["## 目的", "## 出力条件"],
}

replace_suggestions = {
    "Git hub": "GitHub",
    "Claude code": "Claude Code",
    "chatgpt": "ChatGPT",
    "x投稿": "X投稿",
}

forbidden_words = [
    "神すぎる",
    "やばい",
]

def check_file(file_path: Path):
    text = file_path.read_text(encoding="utf-8")

    if file_path.name in required_sections_by_type:
        for section in required_sections_by_type[file_path.name]:
            if section not in text:
                errors.append(f"{file_path}: 必須セクション不足 → {section}")

    if "prompts" in file_path.parts:
        for word in common_required_words["prompts"]:
            if word not in text:
                warnings.append(f"{file_path}: 推奨セクション不足 → {word}")

    if file_path.suffix == ".md" and not text.strip().startswith("# "):
        warnings.append(f"{file_path}: 先頭にH1見出し（# タイトル）がありません")

    if len(text) > 6000:
        warnings.append(f"{file_path}: 文章量が多すぎる可能性があります（6000文字超）")

    if "URL" not in text and "出典" not in text and "参照" not in text:
        warnings.append(f"{file_path}: 出典・参照情報の記載が見当たりません")

    for wrong, correct in replace_suggestions.items():
        if wrong in text:
            warnings.append(f"{file_path}: 表記ゆれ候補『{wrong}』→『{correct}』")

    for word in forbidden_words:
        if word in text:
            warnings.append(f"{file_path}: 禁止候補表現『{word}』が含まれています")

def main():
    found = False

    for dir_name in target_dirs:
        path = Path(dir_name)
        if path.exists():
            for file_path in path.glob("**/*.md"):
                found = True
                check_file(file_path)

    if not found:
        warnings.append("チェック対象のMarkdownファイルがありません")

    if warnings:
        print("=== WARNING ===")
        for w in warnings:
            print(w)

    if errors:
        print("=== ERROR ===")
        for e in errors:
            print(e)
        sys.exit(1)

    print("チェックOK")

if __name__ == "__main__":
    main()
