function qtmono {
        basename=$(basename "$1")
        filename="${basename%.*}"
        extension="${basename##*.}"

        ffmpeg -i $1 -codec:v copy -af pan="mono| c0=FR" $filename-mono.$extension
}

_weatherr() {
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
alias wee='_weatherr'


# For rvm
source ~/.profile

. /usr/local/etc/profile.d/z.sh

