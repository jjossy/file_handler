from pathlib import Path

def build_symlink(source, target):
    parent_dir = Path(__file__).parent.parent.absolute()
    print("{}/{}".format(parent_dir, target))
    print("{}/{}".format(parent_dir, source))
    p = Path("{}/{}".format(parent_dir, target))
    p.symlink_to("{}/{}".format(parent_dir, source))
