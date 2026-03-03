from pathlib import Path
import os

def main():
    base = Path(__file__).resolve().parent
    root = base / "workspace"

    # 1) Create nested directories
    nested = root / "a" / "b" / "c"
    nested.mkdir(parents=True, exist_ok=True)

    # Create a couple of files for listing demo
    (root / "note.txt").write_text("hello\n", encoding="utf-8")
    (root / "data.csv").write_text("x,y\n1,2\n", encoding="utf-8")
    (root / "readme.md").write_text("# demo\n", encoding="utf-8")

    # 2) List files and folders
    print("=== listdir() ===")
    print(os.listdir(root))

    print("=== Path.iterdir() ===")
    for p in root.iterdir():
        print("DIR " if p.is_dir() else "FILE", "-", p.name)

    # 3) Find files by extension
    print("=== find .txt files ===")
    for p in root.rglob("*.txt"):
        print(p)

    # show cwd (getcwd) and chdir example
    print("Current working dir:", os.getcwd())
    os.chdir(root)
    print("Changed working dir:", os.getcwd())

if __name__ == "__main__":
    main()