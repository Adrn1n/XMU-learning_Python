"""
写一个程序输出操作系统的名称、平台和版本号
"""

import platform

print("OS:", platform.system())
print("Platform:", platform.platform())
print("Version:", platform.version())
