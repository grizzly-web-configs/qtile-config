from libqtile.command import lazy

from keys import keys
from libqtile.config import Group, EzKey

groupConfig = [
    dict(
        key='j',
        icon='',
        name='default1',
    ),
    dict(
        key='k',
        icon='',
        name='default2',
    ),
    dict(
        key='l',
        icon='',
        name='default3',
    ),

    dict(
        key='u',
        icon='',
        name='dispo',
    ),
    dict(
        key='i',
        icon='',
        name='organize',
    ),
    dict(
        key='o',
        icon='',
        name='hack',
    ),

    dict(
        key='m',
        icon='',
        name='private',
    ),
    dict(
        key='<comma>',
        icon='',
        name='windows',
    ),
    dict(
        key='<period>',
        icon='',
        name='chat',
    ),
]
groups = []
for conf in groupConfig:
    group = Group(name=conf['name'], label=conf['icon'])
    groups.append(group)
    keys.extend([
        # mod1 + letter of group = switch to group
        EzKey("M-" + conf['key'], lazy.group[group.name].toscreen(),
              desc="Switch to group {}".format(group.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        EzKey("M-S-" + conf['key'], lazy.window.togroup(group.name),
              desc="Switch to & move focused window to group {}".format(group.name)),
    ])