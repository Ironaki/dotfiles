export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

eval "$(pyenv init -)"

alias pyfmt='docker run --rm -v $(pwd):/code ironaki/pyfmt:latest'
