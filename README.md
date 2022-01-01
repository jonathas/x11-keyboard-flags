# X11 Keyboard layout indicator as country flags

## About

On [Gnome](https://www.gnome.org/), the keyboard layout is presented as the code of the language which is currently selected. In the example below, the English (US) keyboard layout is selected:

![Original keyboard layout identifier](./original.jpg "Original keyboard layout identifier")

I don't know about you, but a country flag there looks nicer to me instead of the language. After this script runs, this is what that would look like for the English (US) keyboard layout:

![Modified keyboard layout identifier](./modified.jpg "Modified keyboard layout identifier")

Ps: Other keyboard layouts/languages are also available

## Install

Download it from [AUR](https://aur.archlinux.org/) with [yay](https://github.com/Jguer/yay), for example:

```bash
yay -S x11-keyboard-flags
```

## Usage

Run it with sudo:

```bash
sudo x11-keyboard-flags
```

Then reset gnome-shell by pressing Alt+F2 and entering the "r" command

And that's it! After these steps you'll see the flags in your keyboard layout selector.

## More details

- The flags are emojis copied from [getemoji](https://getemoji.com/#flags) and [emojipedia](https://emojipedia.org/flags/)
- The script sets these emojis in the evdev.xml file from X11
- The script makes a backup of the original evdev.xml file before running, if it doesn't exist yet
