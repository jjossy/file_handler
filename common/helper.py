from pathlib import Path

def build_symlink(source, target):
    p = Path(target)
    parent_dir = Path(__file__).parent.parent.absolute()
    p.symlink_to("{}/{}".format(parent_dir, source))

