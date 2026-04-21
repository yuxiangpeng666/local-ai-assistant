import requests
import json
import os

AI_NAME = "小智一号"


if os.path.exists("user_profile.json"):
    with open("user_profile.json", "r", encoding="utf-8") as f:
        profile = json.load(f)
else:
    profile = {}

def save_profile():
    with open("user_profile.json", "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)

history = []

def detect_language(text):
    for ch in text:
        if '\u4e00' <= ch <= '\u9fff':
            return "中文"
    return "英文"

def update_profile(prompt):
    if "我叫" in prompt:
        profile["name"] = prompt.split("我叫")[-1].strip()
    save_profile()

def chat(prompt):

    update_profile(prompt)
    lang = detect_language(prompt)

    history.append(prompt)
    context = "\n".join(history[-6:])

    full_prompt = f"""
你是{AI_NAME}，一个自然聊天的AI助手。

对话历史：
{context}

规则：
- 使用{lang}
- 自然简洁
- 像人聊天

用户：{prompt}
AI：
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": full_prompt,
                "stream": False
            }
        )

        answer = response.json().get("response", "出错了")
        history.append(answer)

        return answer.strip()

    except Exception as e:
        return f"错误: {e}"