from json import dumps
from json import loads
from pathlib import Path

from .types import YASpeller


def sort_config() -> bool:
    affected = False
    json_file = Path(".yaspeller.json")
    if not json_file.exists():
        return False
    content = json_file.read_text()
    config: YASpeller = loads(content)
    if "dictionary" not in config:
        return False
    sorted_dictionary = sorted(set(config["dictionary"]))
    if config["dictionary"] != sorted_dictionary:
        config["dictionary"] = sorted_dictionary
        new_content = dumps(config, indent=2, sort_keys=True, ensure_ascii=False)
        json_file.write_text(new_content + "\n")
        affected = True
    return affected


def sort_files(files: list[Path]) -> bool:
    affected = False
    for json_file in files:
        affected |= sort_file(json_file)
    return affected


def sort_file(json_file: Path) -> bool:
    affected = False
    content = json_file.read_text()
    dictionary: list[str] = loads(content)
    sorted_dictionary = sorted(set(dictionary))
    if dictionary != sorted_dictionary:
        new_content = dumps(
            sorted_dictionary, indent=2, sort_keys=True, ensure_ascii=False
        )
        json_file.write_text(new_content + "\n")
        affected = True
    return affected
