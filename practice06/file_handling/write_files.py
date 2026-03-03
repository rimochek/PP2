from pathlib import Path

def main():
    base = Path(__file__).resolve().parent
    data_dir = base / "data"
    data_dir.mkdir(exist_ok=True)

    filee = data_dir / "sample.txt"

    # 1) Create a text file and write sample data (mode "w")
    lines = [
        "Alice, 19\n",
        "Bob, 22\n",
        "Charlie, 18\n",
    ]
    with filee.open("w", encoding="utf-8") as f:
        f.writelines(lines)

    # 2) Append new lines (mode "a")
    with filee.open("a", encoding="utf-8") as f:
        f.write("Diana, 25\n")
        f.write("Eve, 21\n")

    print(f"Written + appended to: {filee}")

if __name__ == "__main__":
    main()