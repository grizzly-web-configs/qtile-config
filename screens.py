from libqtile import bar, widget, layout
from libqtile.config import Screen
from screeninfo import get_monitors
from libqtile.log_utils import logger


def current_setups():
    monitors = get_monitors()

    # if only one monitor exists is it main
    if len(monitors) <= 1:
        return [
            {'id': 'main', 'monitor': monitors[0]}
        ]

    conf = []
    for m in get_monitors():
        monitor_id = get_monitor_id_by_name(m.name)

        conf.append({
            'id': monitor_id,
            'monitor': m
        })

    return conf


def get_monitor_id_by_name(name):
    if name == 'eDP-1':
        return 'small'
    if name == 'DP-2' or name == 'DP-1-2':
        return 'left'
    if name == 'DP-1':
        return 'right'

    return 'mRain'


barSize = 30
barConf = {
    'margin': [5, 5, 0, 5],
    'opacity': 0.7
}
sepConf = {
    'linewidth': 0,
    'padding': 4,
}

defaultLeftWidgets = [
    widget.Sep(**sepConf),
    widget.WindowName(),

]
defaultRightWidgets = [
    widget.Chord(),
    widget.Clock(format='%A — KW %W — %d.%m.%Y — %T'),
    widget.Systray(),
    widget.CurrentLayoutIcon(scale=0.65),
    widget.Sep(**sepConf),
]


def get_bar_widgets(before=None, mid=None, after=None):
    if mid is None:
        mid = []
    if after is None:
        after = []
    if before is None:
        before = []

    widgets = []
    widgets.extend(before)
    widgets.extend(defaultLeftWidgets)
    widgets.extend(mid)
    widgets.extend(defaultRightWidgets)
    widgets.extend(after)
    return widgets


screenConfig = {
    'left': Screen(
        top=bar.Bar(get_bar_widgets([
        ]), barSize, **barConf),
    ),
    'right': Screen(
        top=bar.Bar(get_bar_widgets([
        ]), barSize, **barConf),
    ),
    'main': Screen(
        top=bar.Bar(get_bar_widgets([
            widget.CheckUpdates(),
            widget.Battery(
                charge_char='',
                discharge_char='',
                full_char='',
                unknown_char='',
                empty_char='',
                low_percentage='0.2',
                format='{char} {percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W',
            ),
        ]), barSize, **barConf),
    ),
}

screens = []
for setup in current_setups():
    if setup.get('id') not in screenConfig:
        continue

    screens.append(
        screenConfig.get(setup.get('id'))
    )

screens = [
    Screen(
        top=bar.Bar(get_bar_widgets([
            widget.GroupBox(fontsize=20),
        ]), barSize, **barConf),
    ),
    Screen(
        top=bar.Bar(get_bar_widgets(), barSize, **barConf),
    ),
    Screen(
        top=bar.Bar(get_bar_widgets([], [
            widget.CheckUpdates(),
            widget.Battery(
                charge_char='',
                discharge_char='',
                full_char='',
                unknown_char='',
                empty_char='',
                low_percentage='0.2',
                format='{char} {percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W',
            ),
        ]), barSize, **barConf),
    ),
]

layouts = [
    layout.Columns(margin=5, border_focus_stack=['#d75f5f', '#8f3d3d'], padding=10, border_width=4),
    layout.Max(),
    layout.TreeTab(),
]
