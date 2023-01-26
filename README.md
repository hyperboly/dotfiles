# Dotfiles

This repo includes all of the necessary dots I need.

Dependencies:
- picom
- polybar
- One of these WMs:
    - i3 (4.22+)
    - qtile
    - awesomewm
- font awesome
- Ubuntu Mono
- Noto Fonts
- neovim
- zsh
- alacritty
- rofi
- playerctl

# Notes
- This is a bare git repo, so treat it like so
- I am currently using i3, so use qtile and awesome with care; a lot will break
- To activate i3lock, enter the following
    ```sh
    xset 600
    xset -dpms
    ```
- `xset 600` means show the lockscreen in 600 secs
- `xset -dpms` means don't turn off the screen
- Configure xss-lock permanently with [this](https://sleeplessbeastie.eu/2022/08/22/how-to-permanently-disable-dpms-using-xorg/)
