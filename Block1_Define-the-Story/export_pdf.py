"""Exports the three Block 1 deliverables (HTML -> PDF) with headless Chrome/Edge.
Works on macOS, Windows and Linux.

Usage:  python3 export_pdf.py      (Windows: py export_pdf.py)
"""
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FILES = [
    "FA1_Glossary/Glossary-Group1.html",
    "IA2_User-Story-Map-MVP/User-Story-Mapping-MVP_Group1.html",
    "FA3_Epics-User-Stories/Epics-UserStories_Group1.html",
]
CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def find_browser() -> str:
    for c in CANDIDATES:
        if Path(c).exists():
            return c
    for name in ("google-chrome", "chromium", "chromium-browser", "microsoft-edge"):
        if p := shutil.which(name):
            return p
    sys.exit("No Chrome/Edge found. Open the HTML files in a browser and use Print -> Save as PDF instead.")


def main() -> None:
    browser = find_browser()
    for rel in FILES:
        html = HERE / rel
        pdf = html.with_suffix(".pdf")
        subprocess.run([browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf}", html.as_uri()],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"OK  {pdf.relative_to(HERE)}")


if __name__ == "__main__":
    main()
