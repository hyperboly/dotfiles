# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import psutil 
import subprocess

from libqtile import bar, layout, widget, extension, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()
home = '/home/john/'

colors = []
cache= home + '.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "j", lazy.layout.next(), desc="Move window focus to other window"),
    #Key([mod], "k", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "Tab", lazy.screen.toggle_group()),
    #floating/full
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    #quick launch
    Key([mod, "shift"], "s",
        lazy.spawn("flameshot gui"),
        ),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("sh " + home + ".local/bin/dunst/volume.sh up"),
        ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("sh " + home + ".local/bin/dunst/volume.sh down"),
        ),
    Key([], "XF86AudioMute",
        lazy.spawn("sh " + home + ".local/bin/dunst/volume.sh mute"),
        ),
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("sh " + home + ".local/bin/dunst/brightnessControls.sh up"),
        ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("sh " + home + ".local/bin/dunst/brightnessControls.sh down"),
        ),
    Key([mod], "b",
        lazy.spawn("chromium --force-dark-mode --enable-features=WebUIDarkMode"),
        ),
    Key([mod, "shift"], "d",
        lazy.spawn("discord"),
        ),
    Key([mod], "o",
        lazy.spawn("obsidian"),
        ),
    Key([mod], "Return",
        lazy.spawn("rofi -show drun"),
        ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.run_extension(extension.DmenuRun(
        background = colors[3],
        foreground = colors[8],
        dmenu_prompt = ">",
        dmenu_font = "JetBrains Mono-23",
	    selected_background = colors[2],
    	selected_foreground = [8],
    	#dmenu_lines = 5,
        dmenu_bottom = True
        )
    )
),
]

#groups = [Group(i) for i in "123456789"]

groups = [
    Group('1', label=''),
    Group('2', label='', matches=[Match(wm_class='chromium')]),
    Group('3', label='', matches=[Match(wm_class='chromium')]),
    Group('4', label='', matches=[Match(wm_class='discord')], layout='max'),
    Group('5', label=''),
    Group('6', label='', matches=[Match(wm_class='dolphin')]),
    Group('7', label=''),
    Group('8', label=''),
    Group('9', label='')
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


layouts = [
    layout.Columns(
        border_focus_stack=colors[8],
        border_focus=colors[5],
        border_normal=colors[2],
        insert_position = 1,
        border_width=3,
        margin=15
        ),
    layout.Max(),
    # layout.Monadtall(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=25,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.TextBox(
                    background = colors[0],
                    fmt = "",
                    padding = 12,
                    fontsize = 33,
                    mouse_callbacks = {'Button1':
                        lazy.spawn("rofi -show drun -font 'Noto Sans Mono 16'")}
                ),
                widget.GroupBox(
                    foreground = colors[8],
                    background = colors[0],
                	highlight_color = colors[5],
                    block_highlight_text_color = colors[8],
                    this_current_screen_border = colors[4],
                    this_screen_border = colors[5],
                    highlight_method='block',
                	hide_unused = True,
                    spacing = 5,
                    padding = 5,
                    fontsize = 30
                ),
                #widget.Prompt(
                #    foreground = colors[1],
                #    background = colors[8]
                #),
                #widget.WindowName(
                #    foreground = colors[8],
                #    background = colors[2],
                #    padding = 5
                #),
                widget.Spacer(
                    background = colors[0]
                ),
                #widget.Sep(
				#	foreground = colors[8],
				#	background = colors[1],
				#	linewidth = 3,
				#	padding = 5
                #),
                #widget.CPU(
				#	foreground = colors[8],
				#	background = colors[1],
				#	padding = 5
                #),
                #widget.Sep(
				#	foreground = colors[8],
				#	background = colors[0],
				#	linewidth = 2,
				#	padding = 5
                #),
                #widget.Memory(
                #    foreground = colors[8],
                #    background = colors[1],
	            #    format = "Mem: {MemUsed:.0f}",
                #    measure_mem = 'G',
                #    padding = 5
                #),
                #widget.Sep(
				#	foreground = colors[8],
				#	background = colors[1],
				#	linewidth = 3,
				#	padding = 5
                #),
                widget.Net(
                    foreground = colors[8],
                    background = colors[0],
                    interface = "wlo1",
                    padding = 10,
                #   format = "Net: {down} ↓↑ {up}"
                    format = " {down}",
                    fontsize = 15,
                    max_chars = 8,
                    mouse_callbacks = {'Button1': lazy.spawn("alacritty -e nmtui")},
                ),
                #widget.Sep(
				#	foreground = colors[8],
				#	background = colors[0],
				#	linewidth = 2,
				#	padding = 5
                #),
                widget.Battery(
                    battery = 0,
                    foreground = colors[8],
                    background = colors[0],
                    charge_char = '',
                    discharge_char = '',
                    #hide_threshold = 0.99,
                    format = " {char}{percent:2.0%}",
                    low_percentage = 0.2,
                    fontsize = 15,
                    padding = 10,
                ),
                #widget.Sep(
				#	foreground = colors[8],
				#	background = colors[0],
				#	linewidth = 2,
				#	padding = 5
                #),
                widget.Volume(
					foreground = colors[8],
					background = colors[0],
					padding = 10,
					fmt = " {}",
                    mouse_callbacks = {'Button1': lazy.spawn('pavucontrol')},
                    fontsize = 15
                ),
                #widget.Sep(
				#	foreground = colors[8],
				#	background = colors[0],
				#	linewidth = 2,
				#	padding = 5
                #),
                widget.Clock(
					foreground = colors[8],
					background = colors[0],
					format="%a %I:%M%p\n%Y/%m/%d",
					padding = 10,
                    mouse_callbacks = {'Button1': lazy.spawn("alacritty -e calcurse")},
                    fontsize = 15
                ),
                ],
            50,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/startup.sh')
    subprocess.Popen([home])

@hook.subscribe.startup_complete
def autostart():
    startScript = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([startScript])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
