from pathlib import Path

def main():
    base = Path(__file__).resolve().parent
    filee = base / "data" / "sample.txt"

    if not filee.exists():
        print("File not found. Run write_files.py first.")
        return

    print("=== read() ===")
    with filee.open("r", encoding="utf-8") as f:
        textt = f.read()
    print(textt)

    print("=== readline() ===")
    with filee.open("r", encoding="utf-8") as f:
        first_line = f.readline()
    print(first_line.rstrip("\n"))

    print("=== readlines() ===")
    with filee.open("r", encoding="utf-8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        print(i, "->", line.rstrip("\n"))

if __name__ == "__main__":
    main()