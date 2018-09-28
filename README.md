# keynote_snap
snap keynote windows to required size for macOSX

## requirements
- python rumps

``` pip install rumps ```

## how to

- run

``` python keynote_snap.py ```

Snap button located on status bar `[Keynote_Snap]`

- to change size

Rewrite the numbers below in {}

``` osascript -e 'tell application "Keynote"' -e 'set bounds of front window to {500, 450, 1180+500, 600+450}' -e 'end tell' ```

