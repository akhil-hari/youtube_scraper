from pycobweb.bot import callback
from ..utils.clean import *
from ..schemas.video import video
from datetime import datetime


@callback
def scrape_details(bot, response):
    # print("call", datetime.now())
    parser = response.html_parser
    response_text = parse_unicode(response.text_data)
    if parser is None:
        return bot.error(response, "Invalid Response")
    url = response.url
    view_count_regex = r'"viewCount":"(.+?)"'
    likes_regex = (
        r'"defaultText":{"accessibility":{"accessibilityData":{"label":"(.+?) likes"}}'
    )
    keywords_regex = r'"keywords":\[(.+?)\]'
    title_regex = r'"title":"(.+?)"'
    video_length_sec_regex = r'"lengthSeconds":"(\d+?)"'
    description_regex = r'"description":{"simpleText":"(.+?)"'
    comments_count_regex = r'"commentCount":{"simpleText":"(.+?)"}'
    video_id_xpath = r"//meta[@itemprop='videoId']/@content"
    channel_id_xpath = r"//meta[@itemprop='channelId']/@content"

    raw_view_count = re.search(view_count_regex, response_text)
    raw_likes_count = re.search(likes_regex, response_text)
    raw_comments_count = re.search(comments_count_regex, response_text)
    raw_keywords = re.search(keywords_regex, response_text)
    raw_title = re.search(title_regex, response_text, re.DOTALL)
    raw_video_length_sec = re.search(video_length_sec_regex, response_text)
    raw_description = re.search(description_regex, response_text, re.DOTALL)
    raw_video_id = parser.xpath(video_id_xpath)
    raw_channel_id = parser.xpath(channel_id_xpath)

    time = (datetime.now().astimezone()).isoformat()
    view_count = clean_int(raw_view_count.group(1)) if raw_view_count else None
    likes_count = clean_int(raw_likes_count.group(1)) if raw_likes_count else None
    comments_count = (
        clean_int(raw_comments_count.group(1), strict=False)
        if raw_comments_count
        else None
    )
    keywords = clean_list(raw_keywords.group(1)) if raw_keywords else None
    title = raw_title.group(1) if raw_title else None
    video_length_sec = (
        clean_int(raw_video_length_sec.group(1)) if raw_video_length_sec else None
    )
    description = (
        raw_description.group(1).encode("unicode_escape").decode("utf-8")
        if raw_description
        else None
    )
    hashtags = parse_hashtags(raw_description.group(1)) if raw_description else None
    video_id = raw_video_id[0].strip() if raw_video_id else None
    channel_id = raw_channel_id[0].strip() if raw_channel_id else None
    script = parser.xpath("//script[contains(text(),'ytcfg.set')]")
    # print(len(script))
    # count = 0
    # for el in script:
    #     open(f".data/script[{count}].js","w").write(el.xpath("./text()")[0])
    #     count += 1

    data_dict = {
        "video_id": video_id,
        "channel_id": channel_id,
        "title": title,
        "description": description,
        "url": url,
        "view_count": view_count,
        "likes_count": likes_count,
        "comments_count": comments_count,
        "video_length_seconds": video_length_sec,
        "keywords": keywords,
        "hashtags": hashtags,
        "collected_time": time,
    }
    bot.store(video(data_dict))
