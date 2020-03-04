import subprocess
import os
import shutil

# Destination is current dir
DEST_DIRECTORY = '.'

# Check for UPX
if os.path.isdir("upx"):
    upx_string = "--upx-dir=upx"
else:
    upx_string = ""

# Nuke Build dir
if os.path.isdir("build"):
    shutil.rmtree("build")

# Run pyinstaller for Gui
subprocess.run(" ".join(["pyinstaller Gui.spec ",
                                      upx_string,
                                      "-y ",
                                      "--onefile ",
                                      f"--distpath {DEST_DIRECTORY} ",
                                      ]),
                shell=True)
