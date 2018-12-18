# added by Anaconda3 4.2.0 installer
export PATH="/Users/Armstrong/anaconda/envs/ipykernel_py2/bin:$PATH"
eval $(/usr/libexec/path_helper -s)
source $HOME/.bashrc
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS=notebook
export PATH="/Users/Armstrong/Spark/spark-2.3.0-bin-hadoop2.7/bin:$PATH"

# PATH for SML, Vim, Emacs
export PATH="$PATH:/usr/local/smlnj/bin"
export PATH="/Applications/MacVim.app/Contents/MacOS:$PATH"
export PATH="$PATH:/Users/Armstrong/.util_script/shell"
export PATH="$PATH:/Users/Armstrong/.util_script/python"

# Set Editor
export EDITOR="emacs"
export HISTFILESIZE=4096
export HISTSIZE=4096

# 1. alias for bash commands
# 1a. alias for cd
alias cdd="cd ~/Dropbox/Programming/"
alias ccc="cd .."
alias cv="cd .."
alias cdc="cd ~/Dropbox/Code/Self_Study_Courses"
alias dr="cd ~/Dropbox"
alias dl="cd ~/Downloads"
alias cdo="cd ~/Dropbox/Org"
alias guitar="cd ~/Dropbox/Guitar/Guitar-Video"

# 1b. alias for ls
alias lg="ls -alhF" 
alias la="ls -aG"
alias ll="ls -alhFG"

# 1c. alias for open
alias ff="open ."

# 1d. utilities to replace bash commands
alias tt="type"
alias pa="realpath"
alias copy="pbcopy"
alias gg="grep"

# 1e. confirm rm
alias rm="rm -i"

# 2 alias for applications
# 2a. alias for emacs
alias x="/Applications/Emacs.app/Contents/MacOS/Emacs -nw"
alias xs="/Applications/Emacs.app/Contents/MacOS/Emacs"
alias spacemacs="HOME=~/.spacemacs /Applications/Emacs.app/Contents/MacOS/Emacs"

# 2b. alias for vim
alias v="vim"
alias vs="vim -g"

# 2c. alias for anaconda python. Suggest use activatezwei if you want to use python 2 enviroment.
alias py="/Users/Armstrong/anaconda/bin/python"
alias py2="/Users/Armstrong/anaconda/envs/ipykernel_py2/bin/python"
alias pip2="/Users/Armstrong/anaconda/envs/ipykernel_py2/bin/pip"
alias activatezwei="source activate ipykernel_py2"
alias activatedrei="source activate base"

# 2.4 others
alias sbt="TERM=xterm-color sbt"
alias catt="highlight -O ansi --force"
alias gspdfmerge="gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite"

# Terminal Prompt setting
BOLD="\[$(tput bold)\]"
BLUE="\[$(tput setaf 4)\]"
NORMAL="\[$(tput sgr0)\]"

PS1="\n${BOLD}${BLUE}(^•ω •^)${NORMAL} \W ==> "

# For rvm
source ~/.profile

# Alias to convert a stereo recording to mono
#
# $1 - The input filename

function qtmono {
        basename=$(basename "$1")
        filename="${basename%.*}"
        extension="${basename##*.}"

        ffmpeg -i $1 -codec:v copy -af pan="mono| c0=FR" $filename-mono.$extension
}

alias tip="cat ~/.useful_bash_commands"

# Recommended way to activate conda?
. /Users/Armstrong/anaconda/etc/profile.d/conda.sh
# Deprecated ?
export PATH="/Users/Armstrong/anaconda/bin:$PATH" 

########################################DEPRECATED################################################################################

# 3a. Google Cloud Platform
# alias gcp="ssh klijia@35.196.105.176"
# alias aws="ssh -i \"/Users/Armstrong/Dropbox/Programming/Columbia_Computer_Systems/hw1-data-lab/aws-option/hw3.pem\" ubuntu@ec2-18-219-43-52.us-east-2.compute.amazonaws.com"

# 5 alias for shell utilities and commands
#alias mvtor="~/.util_script/mvtor.sh"
#alias xsbak="~/.util_script/xsbak.sh"
