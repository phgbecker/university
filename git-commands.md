### daily git commands

 - git help command
 - git clone {url}
 - git status
 - git status -s
 - git pull
 - git commit -m " "
 - git log
 - git log --oneline
 - git diff
 - git diff {file}
 - git branch
 - git branch {name}
 - git checkout {name}
 - git checkout -b {new branch name}
 - git commit --amend

## Undoing commits and changes to git:
 https://www.atlassian.com/git/tutorials/undoing-changes

```
 - Go to old revision, makes a new branch, then commits 
   git checkout {commit revision SHA-1 ID}
   git branch -b undoing-changes-from-last-commit-revision
   git commit -m ""
 
 - Makes new commit undoing the last commit
   git revert HEAD
 
 - Undo last commit but keep files:
   git reset HEAD~1
   git reset --soft HEAD~1
 ```
