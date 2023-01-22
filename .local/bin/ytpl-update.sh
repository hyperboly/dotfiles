#!/bin/bash

# Check if yt-dlp is installed and updated
pkgCheck () {
    if which yt-dlp > /dev/null ; then
        echo "yt-dlp is installed"
        yt-dlp -U
    else
        echo "yt-dlp is not installed"
        yesNo "Would you like to install yt-dlp [y/n]? " && sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
        sudo chmod a+rx /usr/local/bin/yt-dlp
    fi
}

function yesNo {
    while true; do
        read -p "$* [y/n]: " yn
        case $yn in
            [Yy]*) return 0  ;;  
            [Nn]*) echo "Aborted" ; exit ;;
        esac
    done
}

playlistDownload () {
    printf "\033c"
    echo "Downloading music from remote, please make sure $musDir is the correct directory"
    yesNo "Continue? " && yt-dlp  -x --audio-format opus --add-metadata --metadata-from-title "%(title)s" -q -o "$musDir/%(title)s.%(ext)s" --download-archive $musDir/downloaded.txt $URL
}

pkgCheck

echo "Which directory would you like to download to (Ex. ~/Music/example)?"
read musDir

echo "Insert playlist URL you would like to download/update"
read URL

playlistDownload
