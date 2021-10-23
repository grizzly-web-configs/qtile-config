
import os
import subprocess

from typing import List

from libqtile import layout, hook
from libqtile.config import Match

from keys import keys, mouse
from groups import groups
from screens import screens

keys = keys
mouse = mouse
groups = groups
screens = screens

shell = True
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = True

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

layouts = [
    layout.Columns(margin=10, border_focus_stack=['#d75f5f', '#8f3d3d'], padding=10, border_width=4),
    layout.TreeTab(),
]

widget_defaults = dict(
    font='JetBrainsMono Nerd Font Mono',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])


@hook.subscribe.startup_once
def autostart():
    start = os.path.expanduser('sh ~/.config/.autostart/qtile.sh')
    subprocess.call([start])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
