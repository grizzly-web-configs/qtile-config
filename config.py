import os
import subprocess

from typing import List

from libqtile import layout, hook
from libqtile.config import Match

from keys import keys, mouse
from groups import groups
from screens import screens, layouts

home = os.path.expanduser('~')

keys = keys
mouse = mouse
groups = groups
screens = screens
layouts = layouts

##
#
#  Main Config
#  https://docs.qtile.org/en/latest/manual/config/index.html#configuration-variables
##

# if window wants fullscreen its get fullscreen
auto_fullscreen = True

# steam games want to auto-minimize themselves when losing focus, should we respect this or not?
auto_minimize = True

# focus is where my mouse is
follow_mouse_focus = True

# automatically focus if the window is in the current group
focus_on_window_activation = "smart"

# focus floating windows on click only,
# otherwise its possible that floating windows will be sent to back and you don't get it back
bring_front_click = "floating_only"

# moves cursor to often, every new window also tabs in chrome...
cursor_warp = False

shell = True

dgroups_key_binder = None
dgroups_app_rules = []  # type: List

reconfigure_screens = True



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

@hook.subscribe.startup
def dbus_register():
    id = os.environ.get('DESKTOP_AUTOSTART_ID')
    if not id:
        return
    subprocess.Popen(['dbus-send',
                      '--session',
                      '--print-reply',
                      '--dest=org.gnome.SessionManager',
                      '/org/gnome/SessionManager',
                      'org.gnome.SessionManager.RegisterClient',
                      'string:qtile',
                      'string:' + id])

@hook.subscribe.screen_change
def restart_on_randr(qtile, ev):
    qtile.cmd_restart()


@hook.subscribe.startup_once
def autostart():
    start = os.path.expanduser(home + '/.autostart/qtile.sh')
    subprocess.call([start])


# nobody really uses or cares about this string besides java UI toolkits
# LG3D to maximize irony: it is a 3D non-reparenting WM written in java that happens to be on java’s whitelist
wmname = "LG3D"
