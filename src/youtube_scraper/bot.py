from pycobweb.bot import Bot

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://www.youtube.com/",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}


class YoutubeScraper(Bot):
    def __init__(bot, *args, **kwargs):
        bot.name = "youtube_scraper"
        args = args
        kwargs = kwargs

    def entry_point(bot):
        urls = [
            "https://www.youtube.com/watch?v=WWWDskI46Js",
            "https://www.youtube.com/watch?v=5WfTEZJnv_8",
            "https://www.youtube.com/watch?v=JqcncLPi9zw",
            "https://www.youtube.com/watch?v=AF_f8kl8lJQ",
            "https://www.youtube.com/watch?v=2EVFYstVuVk",
            "https://www.youtube.com/watch?v=x55lAlFtXmw",
            "https://www.youtube.com/watch?v=YIIFp8wDdeM",
            "https://www.youtube.com/watch?v=-IJuKT1mHO8",
            "https://www.youtube.com/watch?v=jQeh4BJxfMg",
            "https://www.youtube.com/watch?v=nW948Va-l10",
        ]
        for url in urls:
            bot.send(
                {
                    "url": url,
                    # "no_cache": True,
                    "callback": bot.scrape_details,
                }
            )
