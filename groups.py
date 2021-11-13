from libqtile.command import lazy

from keys import keys
from libqtile.config import Group, EzKey

groupConfig = [
    dict(
        key='1',
        params={
            'label': '1',
            'name': 'default1',
        },
    ),
    dict(
        key='2',
        params={
            'label': '2',
            'name': 'default2',
        },
    ),
    dict(
        key='3',
        params={
            'label': '3',
            'name': 'default3',
        },
    ),

    dict(
        key='j',
        params={
            'label': '',
            'name': 'code1',
        },
    ),
    dict(
        key='k',
        params={
            'label': '',
            'name': 'code2',
        },
    ),
    dict(
        key='l',
        params={
            'label': '',
            'name': 'code3',
        },
    ),

    dict(
        key='u',
        params={
            'label': '',
            'name': 'dispo',
        },
    ),
    dict(
        key='i',
        params={
            'label': '',
            'name': 'organize',
        },
    ),
    dict(
        key='o',
        params={
            'label': '',
            'name': 'hack',
        },
    ),

    dict(
        key='m',
        params={
            'label': '',
            'name': 'private',
        },
    ),
    dict(
        key='<comma>',
        params={
            'label': '',
            'name': 'windows',
            'layout': 'max',
            'exclusive': True
        },
    ),
    dict(
        key='<period>',
        params={
            'label': '',
            'name': 'chat',
        },
    ),
]
groups = []
for conf in groupConfig:
    group = Group(**conf['params'])
    groups.append(group)
    keys.extend([
        # mod1 + letter of group = switch to group
        EzKey("M-" + conf['key'], lazy.group[group.name].toscreen(),
              desc="Switch to group {}".format(group.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        EzKey("M-S-" + conf['key'], lazy.window.togroup(group.name),
              desc="Switch to & move focused window to group {}".format(group.name)),
    ])