export PATH="$PATH:/usr/local/smlnj/bin"
export PATH="$PATH:/Users/Armstrong/.util_script/shell"
export PATH="$PATH:/Users/Armstrong/.util_script/python"
export PATH="/usr/local/opt/imagemagick@6/bin:$PATH"

export EDITOR="emacs"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/Armstrong/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/Armstrong/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/Armstrong/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/Armstrong/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
