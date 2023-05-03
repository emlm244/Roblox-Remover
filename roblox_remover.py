import os
import shutil
import platform

def remove_roblox_windows():
    os.system("taskkill /f /im RobloxPlayer.exe")
    os.system("taskkill /f /im RobloxStudio.exe")

    os.system("start /wait msiexec /x {CDEE33D0-3F0F-44D2-9A1A-3A8C63B6CBB6} /qn")
    os.system("start /wait msiexec /x {CDEE33D0-3F0F-44D2-9A1A-3A8C63B6CBB6} /qn")

    shutil.rmtree(os.path.expanduser("~\\AppData\\Roaming\\Roblox"), ignore_errors=True)
    shutil.rmtree(os.path.expanduser("~\\AppData\\Local\\Roblox"), ignore_errors=True)

def remove_roblox_mac():
    os.system("killall Roblox")
    os.system("killall RobloxStudio")

    shutil.rmtree("/Applications/Roblox.app", ignore_errors=True)
    shutil.rmtree("/Applications/RobloxStudio.app", ignore_errors=True)

    shutil.rmtree(os.path.expanduser("~/Library/Caches/com.roblox.*"), ignore_errors=True)
    shutil.rmtree(os.path.expanduser("~/Library/Application Support/Roblox"), ignore_errors=True)

def main():
    current_os = platform.system()
    if current_os == "Windows":
        remove_roblox_windows()
    elif current_os == "Darwin":
        remove_roblox_mac()
    else:
        print("This script is not supported on your operating system.")

if __name__ == "__main__":
    main()
