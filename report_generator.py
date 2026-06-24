from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_report(market, news):

    prompt = f"""
你是一名香港金融分析师，生成金融晨报：

市场数据：
{market}

新闻：
{news}

要求：
- 中文
- 结构化
- 11段
- 包含美股/港股/A股影响
"""

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return res.choices[0].message.content
