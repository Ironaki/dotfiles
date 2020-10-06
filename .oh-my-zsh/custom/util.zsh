# qtmono
# ffmpeg => For files with only one audio track, copy one audio track to another one
qtmono() {
        basename=$(basename "$1")
        filename="${basename%.*}"
        extension="${basename##*.}"

        ffmpeg -i $1 -codec:v copy -af pan="mono| c0=FR" $filename-mono.$extension
}

# wee
# get weather information
# all the code here is just for fixing color problems in a light theme
wee() {
    curl -s "wttr.in/$1?m$2" \
        | sed -e 's:021m:017m:g' \
              -e 's:027m:017m:g' \
              -e 's:033m:021m:g' \
              -e 's:039m:021m:g' \
              -e 's:045m:033m:g' \
              -e 's:051m:033m:g' \
              -e 's:050m:031m:g' \
              -e 's:049m:031m:g' \
              -e 's:048m:034m:g' \
              -e 's:047m:034m:g' \
              -e 's:046m:142m:g' \
              -e 's:082m:142m:g' \
              -e 's:208m:196m:g' \
              -e 's:118m:178m:g' \
              -e 's:154m:178m:g' \
              -e 's:190m:214m:g' \
              -e 's:226m:214m:g' \
              -e 's:220m:208m:g' \
              -e 's:214m:208m:g' \
              -e 's:202m:196m:g' \
        | sed '$d'
}

# cattJupyter
# nbconvert, highlight => Instead of cat out plain json (.ipynb), convert the file to highlighted python
cattJupyter() {
    jupyter nbconvert --to python --stdout $1 | bat
}

# gdiff
# colordiff => git diff style output
gdiff() {
    colordiff -u $@ | less -R
}

# rvm
# source ~/.profile

################################################################################
#                                      z                                       #
################################################################################
. /usr/local/etc/profile.d/z.sh

################################################################################
#                            kill all finder window                            #
################################################################################
alias kf="osascript -e 'tell application \"Finder\" to close every window'"

################################################################################
#                                     fzf                                      #
################################################################################
# use fd as default search engine
export FZF_DEFAULT_COMMAND="fd -HI --type f"
# export FZF_DEFAULT_COMMAND="find * -type f"

# integration with z
# https://github.com/junegunn/fzf/wiki/Examples#z
j() {
    [ $# -gt 0 ] && _z "$*" && return
    cd "$(_z -l 2>&1 | fzf --height 40% --nth 2.. --reverse --inline-info +s --tac --query "${*##-* }" | sed 's/^[0-9,.]* *//')"
}

# color schema / default opts
# https://github.com/junegunn/fzf/wiki/Color-schemes
_gen_fzf_default_opts() {
    local base03="234"
    local base02="235"
    local base01="240"
    local base00="241"
    local base0="244"
    local base1="245"
    local base2="254"
    local base3="230"
    local yellow="136"
    local orange="166"
    local red="160"
    local magenta="125"
    local violet="61"
    local blue="33"
    local cyan="37"
    local green="64"

    ## Solarized Light color scheme for fzf
    export FZF_DEFAULT_OPTS="
     --height 40%
     --layout=reverse
     --color fg:-1,bg:-1,hl:$blue,fg+:$base02,bg+:$base2,hl+:$blue
     --color info:$yellow,prompt:$yellow,pointer:$base03,marker:$base03,spinner:$yellow
    "
}
_gen_fzf_default_opts

################################################################################
#                                    ledger                                    #
################################################################################

csv2ledger() {
    icsv2ledger -a $1  --incremental --confirm-dupes --ledger-file $3 $2 $3
}

export BAT_THEME="Solarized (light)"
export MANPAGER="sh -c 'col -bx | bat -l man -p'"
