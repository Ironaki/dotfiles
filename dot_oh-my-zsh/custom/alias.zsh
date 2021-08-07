#1. cd
alias cv="cd .."
alias drop="cd $DROPBOX/"
alias cdd="cd $DROPBOX/Programming"
alias dl="cd ~/Downloads"
alias org="cd $DROPBOX/Org"
alias guitar="cd $DROPBOX/Guitar/Guitar-Video"

#2. Builtin Tools
alias ls="exa"
alias l="exa -lF"  # F: '/' for directory
alias ll="exa -alF"
alias lll="exa -alhUumGF --git"
alias la="exa -aF"
alias lsr="exa -lFR"
alias lar="exa -aFR"
alias -g ig="--git-ignore"
alias tree="exa -T"
alias ff="open ."
alias tt="type"
alias rm="rm -i"
alias bash="bash -l"
alias -g ggg="| grep  --color=auto --exclude-dir={.bzr,CVS,.git,.hg,.svn}"
alias -g gg="| rg"
alias copy="pbcopy"
alias dus="du -sh"
alias cl="clear"

#3. installed tools alias
# TODO: Use doom
# alias x="emacs -nw"
# alias xs="emacs &"
alias v="mvim -v"
alias vs="mvim"
alias sbt="TERM=xterm-color sbt"
alias tip="cat ~/.useful_bash_commands"
alias screenfetch="screenfetch -E" # -E to ignore error
alias we="weather -u si"
alias zl="z -l"
alias stopwatch="utimer -s"
alias sw="utimer -s"
timer() {
    # play music after timer finishes
    utimer -c $1 && afplay -v 0.1 "$ASSETS/music/alarm.flac"
}


#4. proxy
# alias proxyss="export http_proxy=http://127.0.0.1:1087 https_proxy=http://127.0.0.1:1087"
# alias proxypanda="export http_proxy=http://127.0.0.1:10080 https_proxy=http://127.0.0.1:10080"
# alias unproxy="unset http_proxy https_proxy"
