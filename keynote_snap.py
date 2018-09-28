#!/Users/sassan/.pyenv/shims/python
import rumps
import os

scpt = '''
osascript -e 'tell application "Keynote"' -e 'set bounds of front window to {500, 450, 1180+500, 600+450}' -e 'end tell'
'''

@rumps.clicked("Toggle screen fix")
def toggle(sender):
    os.system(scpt)

if __name__ == "__main__":
    app = rumps.App("Rumps Test", title="[KeynoteSnap]")
    app.run()


