from pathlib import Path
import zipfile

root_dir = Path('/Users/vandana/Documents/test')
archive_path = root_dir / Path('compress.zip')    #compress.zip is the filename for archieving the files


with zipfile.ZipFile(archive_path,'w') as zf:
    for files in root_dir.glob("*.txt"):
        zf.write(files)
        files.rmdir()         #deletes the file after archieving 
