# Git Repository Assistant Knowledge Base

# What is Git?

Git is a distributed version control system that helps developers track changes in source code. It allows multiple developers to work on the same project efficiently.

Main Features:
- Version control
- Branching
- Collaboration
- Fast performance
- Open source

--------------------------------------------------

# What is GitHub?

GitHub is a cloud platform used to host Git repositories. It provides collaboration tools like Pull Requests, Issues, Discussions, and GitHub Actions.

--------------------------------------------------

# Installing Git

Windows:
Download Git from:
https://git-scm.com

Verify installation:

git --version

--------------------------------------------------

# Configure Git

Set username

git config --global user.name "Your Name"

Set email

git config --global user.email "you@example.com"

Check configuration

git config --list

--------------------------------------------------

# Create a Repository

Create folder

mkdir MyProject

Go inside folder

cd MyProject

Initialize repository

git init

--------------------------------------------------

# Clone Repository

Clone an existing repository

git clone https://github.com/user/repository.git

--------------------------------------------------

# Git Status

git status

Shows:
- Modified files
- New files
- Deleted files
- Staged files

--------------------------------------------------

# Add Files

Add one file

git add file.py

Add all files

git add .

--------------------------------------------------

# Commit Changes

git commit -m "Initial commit"

A commit saves the current state of the project.

--------------------------------------------------

# View Commit History

git log

Compact view

git log --oneline

--------------------------------------------------

# Branches

Create branch

git branch feature

Switch branch

git checkout feature

Create and switch

git checkout -b feature

New method

git switch feature

--------------------------------------------------

# Merge Branch

git checkout main

git merge feature

--------------------------------------------------

# Delete Branch

git branch -d feature

--------------------------------------------------

# Remote Repository

Add remote

git remote add origin https://github.com/user/project.git

View remote

git remote -v

--------------------------------------------------

# Push Code

git push origin main

First push

git push -u origin main

--------------------------------------------------

# Pull Changes

git pull origin main

Downloads latest changes and merges them.

--------------------------------------------------

# Fetch Changes

git fetch

Downloads changes but does not merge them.

--------------------------------------------------

# Difference Between Pull and Fetch

git fetch
- Downloads changes
- Does not merge

git pull
- Downloads changes
- Automatically merges

--------------------------------------------------

# Undo Changes

Discard unstaged changes

git restore file.py

Remove staged file

git restore --staged file.py

Reset last commit

git reset HEAD~1

--------------------------------------------------

# Stash

Save work

git stash

View stashes

git stash list

Restore stash

git stash pop

--------------------------------------------------

# Tags

Create tag

git tag v1.0

Push tags

git push --tags

--------------------------------------------------

# Merge Conflict

A merge conflict occurs when two branches modify the same part of a file.

Steps:
1. Open conflicting file
2. Resolve conflict
3. Save file
4. git add .
5. git commit

--------------------------------------------------

# .gitignore

Example:

__pycache__/
*.pyc
.env
node_modules/

--------------------------------------------------

# Fork

A fork creates your own copy of another repository.

--------------------------------------------------

# Pull Request

A Pull Request is used to request merging your changes into another branch.

Typical process:
Fork → Clone → Create Branch → Commit → Push → Pull Request

--------------------------------------------------

# GitHub Workflow

1. Create repository
2. Clone repository
3. Create branch
4. Make changes
5. git add .
6. git commit
7. git push
8. Open Pull Request
9. Merge Pull Request

--------------------------------------------------

# Common Git Commands

git init
Initialize repository

git clone
Clone repository

git status
Show repository status

git add .
Stage all files

git commit -m "message"
Save changes

git push
Upload changes

git pull
Download latest changes

git fetch
Download without merging

git branch
List branches

git checkout
Switch branch

git switch
Switch branch

git merge
Merge branches

git log
View history

git diff
Show differences

git stash
Temporarily save work

git tag
Create version tags

git remote -v
View remotes

git config --list
Show Git configuration

--------------------------------------------------

# Best Practices

- Commit frequently
- Write meaningful commit messages
- Use branches for new features
- Pull before pushing
- Keep repositories organized
- Never commit API keys
- Use .gitignore
- Review code before merging

--------------------------------------------------

# Frequently Asked Questions

Q: What is Git?

Git is a distributed version control system.

Q: What is GitHub?

GitHub is a cloud platform for hosting Git repositories.

Q: Difference between Git and GitHub?

Git is software.
GitHub is an online hosting service.

Q: What does git init do?

Creates a new Git repository.

Q: What does git clone do?

Downloads a repository from GitHub.

Q: What does git pull do?

Downloads and merges changes.

Q: What does git fetch do?

Downloads changes without merging.

Q: What is a commit?

A saved snapshot of your project.

Q: What is a branch?

An independent line of development.

Q: What is a merge?

Combining two branches into one.