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
            "https://www.youtube.com/watch?v=cQcfA_I5jA8",
            "https://www.youtube.com/watch?v=oN3tz-UetKw",
            "https://www.youtube.com/watch?v=95ADPYoSRPc",
            "https://www.youtube.com/watch?v=YS1w0lkyqe0",
            "https://www.youtube.com/watch?v=x4TpzSinWqg",
            "https://www.youtube.com/watch?v=PKbL-427wms",
            "https://www.youtube.com/watch?v=Lq2lTdB1dn8",
            "https://www.youtube.com/watch?v=Neo6E4sbZvQ",
            "https://www.youtube.com/watch?v=_iVx4aJEKKA",
            "https://www.youtube.com/watch?v=h1ehTAaK0os",
        ]
        # bot.limit_url("2/30s", "https://www.youtube.com/watch?v=")
        for url in urls:
            # bot.limit_url("1/6s","https://www.youtube.com")
            bot.send(
                {
                    "url": url,
                    # "no_cache": True,
                    "callback": bot.scrape_details,
                }
            )
            # bot.send(
            #     {
            #         "url": "https://httpbin.org/ip",
            #         "no_cache": True,
            #         # "callback": bot.scrape_details,
            #     }
            # )
