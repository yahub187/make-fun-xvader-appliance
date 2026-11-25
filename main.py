import os

ENTRY_TEXT = "Spin cycle aborted. The load is unbalanced, like the person who put a single shoe in with six towels."
ENTRY_FILENAME = "entry.txt"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
