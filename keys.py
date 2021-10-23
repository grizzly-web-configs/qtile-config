import os

from libqtile.command import lazy
from libqtile.config import EzKey, EzClick, EzDrag, KeyChord
from libqtile.utils import guess_terminal

mod = "mod4"
home = os.path.expanduser('~')
terminal = guess_terminal()

modifier_keys = {
    'M': 'mod4',
    'A': 'mod1',
    'S': 'shift',
    'C': 'control',
}

keys = [
    # Switch between windows
    EzKey("M-<Left>", lazy.layout.previous(), desc="Move focus to left"),
    EzKey("M-<Right>", lazy.layout.next(), desc="Move focus to right"),
    EzKey("M-<Down>", lazy.layout.previous(), desc="Move focus down"),
    EzKey("M-<Up>", lazy.layout.next(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    EzKey(
        "M-S-<Left>",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    EzKey(
        "M-S-<Right>",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
    ),
    EzKey(
        "M-S-<Down>",
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),
    EzKey(
        "M-S-<Up>",
        lazy.layout.shuffle_up(),
        desc="Move window up"
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    EzKey(
        "M-<space>",
        lazy.layout.toggle_split(),
        desc="Move window focus to other window"
    ),
    EzKey(
        "M-S-<Return>",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"
    ),


    EzKey(
        "M-<Return>",
        lazy.spawn(terminal),
        desc="Launch terminal"
    ),

    # Toggle between different layouts as defined below
    EzKey(
        "M-w",
        lazy.window.kill(),
        desc="Kill focused window"
    ),

    #
    # Qtile specific
    #
    EzKey("M-C-r", lazy.restart(), desc="Restart Qtile"),
    EzKey("M-C-q", lazy.shutdown(), desc="Shutdown Qtile"),

    #
    # Change the volume if your keyboard has special volume keys.
    #
    EzKey(
        "<XF86AudioRaiseVolume>",
        lazy.spawn("amixer -c 0 -q set Master 2dB+")
    ),
    EzKey(
        "<XF86AudioLowerVolume>",
        lazy.spawn("amixer -c 0 -q set Master 2dB-")
    ),
    EzKey(
        "<XF86AudioMute>",
        lazy.spawn("amixer -c 0 -q set Master toggle")
    ),

    #
    # run rofi
    #
    EzKey(
        "M-d",
        lazy.spawn("sh " + home + "/.config/rofi/run/drun.sh"),
        desc="run rofi"
    ),
    EzKey(
        "M-<Tab>",
        lazy.spawn("sh " + home + "/.config/rofi/run/windows.sh"),
        desc="run rofi"
    ),

    #
    # Screenshots
    #
    EzKey(
        "M-s",
        lazy.spawn("flameshot gui"),
        desc="run flameshot"
    ),
    EzKey(
        "M-s",
        lazy.spawn("flameshot gui --delay 2000"),
        desc="run flameshot"
    ),

    #
    # Resize Window
    #
    KeyChord([mod], "r", [
        EzKey("<Left>", lazy.layout.grow_left()),
        EzKey("<Right>", lazy.layout.grow_right()),
        EzKey("<Up>", lazy.layout.grow_up()),
        EzKey("<Down>", lazy.layout.grow_down()),
        EzKey("n", lazy.layout.normalize()),
        EzKey("f", lazy.layout.maximize())],
        mode="Windows"
    ),
]

# Drag floating layouts.
mouse = [
    EzDrag(
        "M-<Button1>",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    EzDrag(
        "M-<Button3>",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    EzClick(
        "M-<Button2>",
        lazy.window.bring_to_front()
    )
]
