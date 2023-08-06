from json import dumps
from json import loads
from pathlib import Path
from string import punctuation

from .types import YASpeller


punctuation = punctuation + "“”’…"


def find_unused_words() -> bool:
    affected = False
    words_cloud = get_words_cloud()
    dictionary = get_dictionary()
    unused = dictionary - words_cloud
    if unused:
        write_dictionary(sorted(dictionary - unused))
        affected = True
    return affected


def get_words_cloud() -> set[str]:
    words_cloud = set()
    docs = Path("docs")
    for md_file in docs.glob("**/*.md"):
        content = md_file.read_text()
        words_cloud |= {
            word.strip(punctuation)
            for token in content.split()
            for word in token.split("-")
        }
    return words_cloud


def get_dictionary() -> set[str]:
    json_file = Path(".yaspeller.json")
    content = json_file.read_text()
    config: YASpeller = loads(content)
    return set(config["dictionary"])


def write_dictionary(new_dictionary: list[str]) -> None:
    json_file = Path(".yaspeller.json")
    content = json_file.read_text()
    config: YASpeller = loads(content)
    config["dictionary"] = new_dictionary
    new_content = dumps(config, indent=2, sort_keys=True, ensure_ascii=False)
    json_file.write_text(new_content + "\n")
