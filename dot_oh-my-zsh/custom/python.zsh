# pyenv
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# pyfmt
alias pyfmt='docker run --rm -v $(pwd):/code gcr.io/main-pj-al/pyfmt:latest'
