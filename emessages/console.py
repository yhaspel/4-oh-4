import io

import wikipedia
import re

from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

from . import models
from PIL import Image
import requests


# wikipedia.set_lang("he")


def text_end(line):
    if line == "":
        return True
    else:
        return False


def get_wiki_http_errors():
    w = wikipedia.page("List_of_HTTP_status_code")

    tip_title = re.compile("^==(.+)==$")
    error_title = re.compile("^(\d+)(.+)$")
    error_codes = {}
    tips = []
    lines = w.content.split("\n")
    index, length = 0, len(lines)
    while index < length:
        line = lines[index]
        if tip_title.match(line):
            tip = {}
            tip["tip_title"] = tip_title.match(line).groups()[0]
            tip["tip_text"] = ""
            tip["tip_author"] = "wiki"
            tip["tip_category"] = "info"
            while not error_title.match(line) and not index >= length - 1:
                index += 1
                line = lines[index]
                tip["tip_text"] += line
            tips.append(tip)
            # if index >= length - 1:
            #     break
        if error_title.match(line):
            em = {}
            em["error_code"] = error_title.match(line).groups()[0]
            print("loading {}".format(em["error_code"]))
            em["title"] = error_title.match(line).groups()[1]
            em["description"] = ""
            try:
                em["photo"] = Image.open(
                    io.BytesIO(requests.get("https://http.cat/{}.png".format(em["error_code"])).content))
            except OSError:
                pass
            while not text_end(line):
                index += 1
                line = lines[index]
                em["description"] += line
                if error_title.match(line):
                    index -= 1
                    break
                    # because we just found it maybe.. and we need the upper loop to check it

            error_codes[em["error_code"]] = em
        index += 1
    return error_codes.values()


def save_emessages(dict_emessages):
    for em in dict_emessages:
        photo = em.get("photo", False)
        if photo:
            del em["photo"]
        item = models.EMessage(**em)
        if photo:
            item.photo.save(name="{}.{}".format(em["error_code"], 'png'), content=File(photo.fp))
        item.save()
    print("Done")



