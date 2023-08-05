import copy
import time
from typing import Dict, Tuple

import requests

from mwconstants.constants.c_media import DEF_OPTION_TAGS, IMG_OPTION_ALIASES
from mwconstants.languages import get_wiki_sites


def parse_image_options(wikitext: str, lang: str = "en") -> Tuple[str, str, list]:
    """Split media file wikitext into file title, formatting options, and caption.

    A media link always begins with the title and any formatting/captions follow as parameters separated by |.
    Wikitext media can show up in three different formats, each of which is supported here:
    * Brackets: [[File:filename.ext|formatting options|caption]]
    * Template: File:filename.ext (caption/formatting are separate parameters)
    * Gallery: filename.ext|formatting options|caption

    There are a set of allowed keywords/parameters for media formatting. Each parameter in a media file is
    checked against these formatting options and if it does not match, it is assumed to be the caption.

    For more info, see: https://www.mediawiki.org/wiki/Help:Images#Syntax
    """
    title = None
    options = []
    caption = None
    if wikitext:
        # remove optional brackets and split into parameters
        wikitext_parts = wikitext.strip("[]").split("|")
        # title is the first parameter and the only required one
        title = wikitext_parts[0]
        if len(wikitext_parts) > 1:
            lang_tags = {}
            for k in DEF_OPTION_TAGS:
                lang_tags[k] = DEF_OPTION_TAGS[k] + IMG_OPTION_ALIASES.get(
                    lang, {}
                ).get(k, [])
            for o in wikitext_parts[1:]:
                o = o.strip()
                if o in lang_tags["keywords"]:
                    options.append(o)
                elif o.split("=")[0] in lang_tags["params"]:
                    options.append(o)
                else:
                    found = False
                    for t in lang_tags["startswith"]:
                        if o.startswith(t):
                            options.append(o)
                            found = True
                            break
                    if not found:
                        for t in lang_tags["endswith"]:
                            if o.endswith(t):
                                options.append(o)
                                found = True
                                break
                    if not found:
                        caption = o

    return title, caption, options


def get_wiki_valid_img_options(lang: str) -> Dict[str, list]:
    """Get official list of acceptable image formatting tags -- e.g., frameless, top, etc."""
    session = requests.Session()
    base_url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "meta": "siteinfo",
        "siprop": "magicwords",
        "format": "json",
        "formatversion": "2",
    }
    result = session.get(url=base_url, params=params).json()

    img_keywords = []
    img_param_names = []
    img_startswith = []
    img_endswith = []
    # TODO: carry magic["name"] over with the parameters and
    #  map them to a more fine-grained taxonomy than just options
    if "magicwords" in result.get("query", {}):
        for magic in result["query"]["magicwords"]:
            if magic["name"].startswith("img_"):
                if not magic["case-sensitive"]:
                    # we don't handle case insensitive so...
                    print(f"warning case-insensitive for {lang}: {magic}")
                for tag in magic["aliases"]:
                    if "=" in tag:
                        img_param_names.append(tag.split("=")[0])
                    elif tag.endswith("$1"):
                        img_startswith.append(tag[:-2])
                    elif tag.startswith("$1"):
                        img_endswith.append(tag[2:])
                    elif "$" in tag:
                        print("Didn't expect this:", tag)
                    else:
                        img_keywords.append(tag)
    return {
        "keywords": list(set(img_keywords)),
        "params": list(set(img_param_names)),
        "startswith": list(set(img_startswith)),
        "endswith": list(set(img_endswith)),
    }


def get_img_options(project: str = "wiki") -> Tuple[dict, Dict[str, dict]]:
    """
    Utility for generating language-specific lists of valid media formatting options on a Wikimedia project.

    For example, to know that [[File:image.png|thumb]] has `thumb` formatting as opposed to a caption
    that reads `thumb` we must know that `thumb` is a valid image formatting tag and appears as a
    stand-alone keyword. Any parameters that do not match a valid image formatting tag pattern are
    assumed to be the image caption.

    See: https://www.mediawiki.org/wiki/Help:Images#Syntax
    """

    wiki_languages = get_wiki_sites(project)
    print(f"{len(wiki_languages)} languages: {wiki_languages}")
    img_options = {}
    for lang in wiki_languages:
        img_options[lang] = get_wiki_valid_img_options(lang)
        time.sleep(0.25)

    # separate out english tags, which are valid for any language
    # this greatly reduces the size of the final list
    default_option_tags = copy.deepcopy(img_options["en"])

    to_remove = []
    for lang in img_options:
        for param_type in default_option_tags:
            for tag in default_option_tags[param_type]:
                img_options[lang][param_type].remove(tag)
            if not img_options[lang][param_type]:
                img_options[lang].pop(param_type)
        if not img_options[lang]:
            to_remove.append(lang)

    for lang in to_remove:
        img_options.pop(lang)

    return default_option_tags, img_options


if __name__ == "__main__":
    print(get_img_options("wiki"))  # Wikipedia image formatting options
