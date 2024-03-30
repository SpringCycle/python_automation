from pathlib import Path
import zipfile

root_dir = Path('.')

change_path = Path('test')

for path in root_dir.glob("*.zip"):                  #glob checks all folders and rglob checks the sub folders
    with zipfile.ZipFile(path,'r') as zf:
        final_path = change_path / Path(path.stem)
        print(final_path)
        # zf.extractall(path= change_path)
