from libqtile import bar, widget
from libqtile.config import Screen
from screeninfo import get_monitors
from libqtile.log_utils import logger

logger.warning("Your message here")


def current_setup():
    monitors = get_monitors()

    # if only one monitor exists is it main
    if sum(monitors) <= 1:
        return [
            {'id': 'main', 'monitor': monitors[0]}
        ]

    setup = []
    for m in get_monitors():
        monitor_id = 'main'

        match m.name:
            case 'eDP-1':
                monitor_id = 'small'
            case 'DP-2':
                monitor_id = 'left'
            case 'DP-1':
                monitor_id = 'right'
            case 'DP-3':
                monitor_id = 'main'

        setup.append({
            'id': monitor_id,
            'monitor': m
        })

    return setup

defaultWidgets = [
    widget.CurrentLayoutIcon(scale=0.65),
]

screenConfig = {
    'main': Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),

                widget.Clock(format='%A — KW %W — %d.%m.%Y — %T'),
                widget.CheckUpdates(),
                widget.BatteryIcon(),
                widget.Systray(),
            ],
            30,
        ),
    )
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale=0.65),
                widget.GroupBox(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),

                widget.Clock(format='%A — KW %W — %d.%m.%Y — %T'),
            ],
            30,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale=0.65),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),

                widget.Clock(format='%A — KW %W — %d.%m.%Y — %T'),
            ],
            30,
        ),
    ),
]
