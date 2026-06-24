from market_data import fetch_market_data
from news_scraper import fetch_news
from report_generator import generate_report
from sender_email import send_email
from datetime import datetime

def main():
    market = fetch_market_data()
    news = fetch_news()

    report = generate_report(market, news)

    today = datetime.now().strftime("%Y-%m-%d")

    send_email(
        subject=f"金融晨报 · {today}",
        body=report,
        to_email="你的QQ邮箱@qq.com"
    )

if __name__ == "__main__":
    main()
