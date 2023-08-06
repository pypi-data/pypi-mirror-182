from json import dumps
from json import loads
from pathlib import Path

from .types import YASpeller


def sort_words() -> bool:
    affected = False
    json_file = Path(".yaspeller.json")
    content = json_file.read_text()
    config: YASpeller = loads(content)
    sorted_dictionary = sorted(set(config["dictionary"]))
    if config["dictionary"] != sorted_dictionary:
        config["dictionary"] = sorted_dictionary
        new_content = dumps(config, indent=2, sort_keys=True, ensure_ascii=False)
        json_file.write_text(new_content + "\n")
        affected = True
    return affected
