import re

def parse_unicode(text):
    text = text.encode()
    return text.decode("unicode_escape")

def parse_hashtags(text):
    hashtag_regex = r"(#\w+)"
    raw_hashtags =  re.findall(hashtag_regex, text)
    hashtags = clean_list(raw_hashtags)
    return hashtags if hashtags else []


def clean_int(num_string, convert_to="int", strict=True):
    if isinstance(num_string, str):
        num_string = num_string.strip('"\' \n\t')
        num_string = num_string.replace(",","")
        num_string = num_string.replace(" ","")
        num_string = num_string.strip()
        try:
            num_value = int(num_string) if convert_to == "int" else float(num_string)
            return num_value
        except ValueError:
            return None if strict else num_string
    elif isinstance(num_string, (int, float)):
        return num_string

def clean_list(list_string):
    if isinstance(list_string, str):
        list_string = list_string.strip("'\"")
        output_list = list(map(lambda x: x.strip().strip('"'), list_string.split(",")))
        return output_list
    elif isinstance(list_string, (list, tuple)):
        output_list = list(map(lambda x: x.strip().strip('"'), list_string))
        return output_list
