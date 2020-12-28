if hash pyenv &> /dev/null; then
  alias brew='PATH="${PATH//$(pyenv root)\/shims:/}" brew'
fi
