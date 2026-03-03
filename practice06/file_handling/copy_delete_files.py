from pathlib import Path
import shutil

def safe_delete(pathh: Path) -> bool:
    """Delete a file safely: only if it exists and is a file."""
    if pathh.exists() and pathh.is_file():
        pathh.unlink()
        return True
    return False

def main():
    base = Path(__file__).resolve().parent
    data_dir = base / "data"
    data_dir.mkdir(exist_ok=True)

    src = data_dir / "sample.txt"
    if not src.exists():
        print("Source file missing. Run write_files.py first.")
        return

    backup_dir = data_dir / "backup"
    backup_dir.mkdir(exist_ok=True)

    # 4) Copy and back up files using shutil
    dst = backup_dir / "sample_backup.txt"
    shutil.copy2(src, dst)  # keeps metadata
    print(f"Copied: {src} -> {dst}")

    # 5) Delete files safely (example: delete backup)
    deleted = safe_delete(dst)
    print("Deleted backup?" , deleted)

if __name__ == "__main__":
    main()