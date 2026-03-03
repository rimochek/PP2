from pathlib import Path
import shutil

def main():
    base = Path(__file__).resolve().parent
    root = base / "workspace"
    src_dir = root
    dst_dir = root / "moved_here"

    dst_dir.mkdir(parents=True, exist_ok=True)

    filee = src_dir / "note.txt"
    if not filee.exists():
        print("note.txt not found. Run create_list_dirs.py first.")
        return

    # 4) Move/copy files between directories
    moved_to = dst_dir / filee.name
    shutil.move(str(filee), str(moved_to))
    print(f"Moved: {filee} -> {moved_to}")

    # Copy back as demonstration
    copied_to = src_dir / "note_copied_back.txt"
    shutil.copy2(moved_to, copied_to)
    print(f"Copied: {moved_to} -> {copied_to}")

if __name__ == "__main__":
    main()