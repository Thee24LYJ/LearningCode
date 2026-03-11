alias l='ls -aClFh'
alias v='vim'
alias cl='clear'
alias s='source'
alias ..='cd ..'
alias ...='cd ../..'
alias cb='cd -'
alias va='vim ~/.bash_aliases'
alias vc='vim ~/.bashrc'
alias sa='source ~/.bash_aliases'
alias sc='source ~/.bashrc'

# git config
alias gi='git init'
alias gs='git status'
alias gl='git log --graph'
alias ga='git add'
alias ga.='git add .'
alias gc='git commit'
alias gr='git remote'
alias gb='git branch'
alias gck='git checkout'
alias gcl='git clone'
alias gpl='git pull'
alias gph='git push'
alias gm='git merge --no-ff'

# env config
# 定制命令提示符
# csh
#set green="%\033[1;32m%}"
#set end="%\033[0m%}"
#set prompt="\n""${green}[${USER}"@"${HOST} -> %Y-%W-%D %T] %//\n${end}>"

# bash
BOLD_GREEN='\[\033[1;32m\]'
BLUE='\[\033[0;34m\]'
PURPLE='\[\033[0;35m\]'
RESET='\[\033[0m\]'
# 解析git分支(如果存在)
parse_git_branch() {
    git branch 2>/dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
PS1="${BOLD_GREEN}[${USER}@${HOSTNAME} -> \D{%Y-%W-%d %T}] \w${BLUE}\$(parse_git_branch)${RESET}\n> "
