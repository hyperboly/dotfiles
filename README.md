# Dotfiles

This repo includes all of the necessary dots I need.

Dependencies:
- picom
- polybar
- One of these WMs:
    - i3 (4.22+)
    - qtile
    - awesomewm
    - hyprland
- font awesome
- Ubuntu Mono
- Noto Fonts
- neovim
- zsh
- alacritty
- rofi
- playerctl

- Dependencies for hyprland on Arch (Depencies above still mostly apply)
    - grim
    - slurp
    - hyprland
    - swaylock
    - swayidle
    - swww
    - foot
    - xdg-desktop-portal-hyprland
    - pipewire
    - wireplumber
    - dunst
    - dracula-gtk-theme
    - lxappearance
    - rofi-lbonn-wayland-git
    - bibata-cursor-theme-bin
    - brightnessctl
    - pamixer
    - swappy

# Notes
- This is a bare git repo, so treat it like so
- I am currently using i3, so use qtile and awesome with care; a lot will break
- Scripts in `~/.local/bin` require their own dependencies
- There is no bar for hyprland, there are keyboard controls though

# XSS-Lock
- To temporarily activate i3lock, enter the following
    ```sh
    xset 600
    xset -dpms
    ```
- `xset 600` means show the lockscreen in 600 secs
- `xset -dpms` means don't turn off the screen
- Configure xss-lock permanently with [this](https://sleeplessbeastie.eu/2022/08/22/how-to-permanently-disable-dpms-using-xorg/)
- xss-lock doesn't work in wayland (Hyprland)
