import argparse
import re
import sys
from pathlib import Path
from typing import Any, List


def _try_int(s: Any) -> Any:
    """Try to convert to int."""
    try:
        return int(s)
    except Exception:
        return s


def _alphanum_key(s: str) -> int:
    """Turn a string into a list of string and number chunks.
    
    E.g:
    "z23a" -> ["z", 23, "a"]
    """
    strings_and_ints = [_try_int(string) for string in re.split('([0-9]+)', s)]
    min_value = sys.maxsize
    for i in strings_and_ints:
        if isinstance(i, int):
            min_value = min(i, min_value)
    if min_value == sys.maxsize:
        raise ValueError("No valid number in filename.")
    return min_value


def _load_file(path: Path) -> List[str]:
    """Read file from the path."""
    with open(path, "r") as reader:
        return reader.readlines()

def _write_file(path: Path, lines: List[str]):
    """Write file at the path."""
    string = "".join(lines)
    with open(path, "w") as writer:
        writer.write(string)


def main():
    """"""
    if sys.version_info[0] < 3:
        raise ValueError("Python 3 or a more recent version is required.")
    parser = argparse.ArgumentParser(
        description='Markdown concatentation tool'
    )
    parser.add_argument(
        '--markdown_dir', 
        action="store", 
        dest="markdown_dir"
    )
    results = parser.parse_args()
    if results.markdown_dir is None:
        raise ValueError(
            "--markdown_dir must be supplied to the script."
        )
    markdown_dir = Path(results.markdown_dir).absolute()
    markdown_names = [path.name for path in markdown_dir.glob("*.md")]
    book_name = markdown_dir.name
    # Lines from all the files.
    lines = []
    for file_name in sorted(markdown_names, key=_alphanum_key):
        path = markdown_dir / file_name
        lines += _load_file(path)
        lines += ["\n\n"]
    bib_file_defined = len(list(markdown_dir.glob("*.bib")))
    if bib_file_defined:
        lines += ["# Bibliography"]
    # Write lines to file.
    save_dir = Path(".") / "build"
    save_dir.mkdir(parents=True, exist_ok=True)
    save_path = save_dir / f"{book_name}.md"
    _write_file(save_path, lines)


if __name__ == "__main__":
    main()