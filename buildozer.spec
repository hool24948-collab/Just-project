[app]

# (str) Title of your application
title = Pixel Art Editor

# (str) Package name
package.name = pixelarteditor

# (str) Package domain (needed for android packaging)
package.domain = org.pixelart

# (str) Version of your application
version = 0.1

# (list) Source files to include (let it include all python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
