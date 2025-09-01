# darknet_crawler.py

# Sample darknet post data - extendable list of dicts with optional metadata
darknet_posts = [
    {"text": "Selling high quality coke and MDMA in bulk.", "source": "DarknetMarket1"},
    {"text": "Get ganja delivered safely, cheap prices!", "source": "TelegramGroupA"},
    {"text": "New batch of white powder available.", "source": "ForumX"},
    {"text": "Legal products only.", "source": "MarketZ"}
]

# Suspicious keywords list
suspicious_keywords = ["coke", "ganja", "MDMA", "white powder", "pills", "cocaine", "heroin", "marijuana", "cannabis", "ecstasy"]

def crawl_darknet(posts, keywords):
    flagged = []
    for post in posts:
        for keyword in keywords:
            if keyword.lower() in post["text"].lower():
                flagged.append({"post": post, "keyword": keyword})
                break
    return flagged

if __name__ == "__main__":
    flagged_posts = crawl_darknet(darknet_posts, suspicious_keywords)
    for item in flagged_posts:
        print(f'Flagged Post: "{item["post"]["text"]}" Keyword: {item["keyword"]}')
