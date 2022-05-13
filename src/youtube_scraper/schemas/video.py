from pycobweb.schema import NormalSchema

key_list = [
    "video_id",
    "channel_id",
    "title",
    "description",
    "url",
    "view_count",
    "likes_count",
    "comments_count",
    "video_length_seconds",
    "keywords",
    "hashtags",
    "collected_time"
    ]

video = NormalSchema(key_list, "video_data")