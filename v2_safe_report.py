import datetime

def generate_report(market_data, news_data):

    today = datetime.datetime.now().strftime("%Y-%m-%d")

    report = f"""
📊 金融晨报 · {today}

====================

1️⃣ 全球市场
{market_data}

--------------------

2️⃣ 美股
{news_data.get("us_stock", "数据暂缺")}

解读：科技股仍受利率影响，市场偏谨慎

--------------------

3️⃣ 美债
{news_data.get("bond", "数据暂缺")}

解读：10Y收益率变化影响风险资产定价

--------------------

4️⃣ A股
{news_data.get("a_share", "数据暂缺")}

解读：成交量决定短期趋势

--------------------

5️⃣ 港股
{news_data.get("hk", "数据暂缺")}

解读：港股受外资流动影响明显

--------------------

6️⃣ 汇率
{news_data.get("fx", "数据暂缺")}

解读：人民币波动影响跨境资金

--------------------

7️⃣ 商品
{news_data.get("commodities", "数据暂缺")}

解读：原油与黄金反映通胀与避险

--------------------

8️⃣ 加密
{news_data.get("crypto", "数据暂缺")}

解读：BTC仍跟随纳指波动

--------------------

9️⃣ 政策
{news_data.get("policy", "数据暂缺")}

--------------------

🔟 央行
{news_data.get("central_bank", "数据暂缺")}

--------------------

1️⃣1️⃣ 今日交易重点
- 关注美元指数
- 关注港股科技板块
- 关注A股成交量
"""

    return report
