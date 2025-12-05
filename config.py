import os
from pathlib import Path


if os.name == "nt":
    ROOT_DIRS = [r"C:\Users\marit\Documents\streamlit"]
else:
    ROOT_DIRS = []
    for user_path in Path("/home").iterdir():
        if any(s in str(user_path) for s in ["admin", "sysmgr"]):
            continue
        ROOT_DIRS.append(str(user_path / "streamlit"))
