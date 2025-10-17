import os
import webbrowser
import shutil

def get_chrome_path():
    """Automatically detect Chrome path across systems."""
    paths = [
        "C:/Program Files/Google/Chrome/Application/chrome.exe",
        "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
        os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
    ]
    for path in paths:
        if os.path.exists(path):
            return path

    chrome_in_path = shutil.which("chrome") or shutil.which("google-chrome")
    if chrome_in_path:
        return chrome_in_path

    try:
        import winreg
        reg_path = r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\chrome.exe"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
            return winreg.QueryValue(key, None)
    except Exception:
        pass

    return None


def open_in_chrome(url):
    """Open a URL in Chrome (auto-detect) or default browser."""
    chrome_path = get_chrome_path()
    if chrome_path:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open(url)
    else:
        webbrowser.open_new_tab(url)
        print("Chrome not found — opened in default browser.")
