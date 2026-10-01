# Git & VS Code – Learning Notes and Quick Reference

This document summarizes the Git, GitHub, VS Code, and terminal concepts I learned during my RPA Architect learning journey.

The goal is not to memorize every Git command, but to understand **what each command does, when to use it, and how Git works as a system.**

---

# 1. Git Fundamentals

Git is a distributed version control system used to track changes in files and source code.

The basic workflow is:

```text
Working Directory
       ↓
    git add
       ↓
Staging Area
       ↓
   git commit
       ↓
Local Repository
       ↓
    git push
       ↓
Remote Repository (GitHub)
```

## Working Directory

The Working Directory contains the files I am currently working on.

When I modify a file such as `README.md`, the change first exists in my Working Directory.

## Staging Area

The Staging Area determines which changes will be included in the next commit.

To stage a specific file:

```bash
git add README.md
```

To stage all changes:

```bash
git add .
```

## Local Repository

When I create a commit, the staged changes are stored in my local Git history.

```bash
git commit -m "Update README"
```

Creating a commit does **not** automatically send it to GitHub.

## Remote Repository

A remote repository is a copy of the repository stored on another system, such as GitHub.

To send my local commits to the remote repository:

```bash
git push
```

---

# 2. Checking Repository Status

One of the most important Git commands is:

```bash
git status
```

It shows the current state of the repository.

It can tell me whether files are:

- modified
- untracked
- staged
- committed
- ahead of the remote branch
- behind the remote branch

I should use `git status` frequently while working.

---

# 3. Viewing Changes with git diff

To see changes that I have made but have not staged yet:

```bash
git diff
```

For example:

```diff
+ New line
```

means that a line was added.

After running `git add`, the normal `git diff` may show nothing because the change has moved to the Staging Area.

To inspect staged changes:

```bash
git diff --staged
```

---

# 4. Staging Changes with git add

To stage one file:

```bash
git add README.md
```

To stage all current changes:

```bash
git add .
```

A good workflow is:

```bash
git add .
git status
git commit -m "..."
```

I should check `git status` after staging files so that I do not accidentally commit files that should not be included.

---

# 5. Creating Commits

To save staged changes in Git history:

```bash
git commit -m "Update README"
```

A commit can be thought of as a checkpoint in the project's history.

Good commit messages describe the actual change:

```text
Add API integration
Fix invoice validation
Update SQL exercises
Add Git ignore rules
```

Avoid meaningless commit messages such as:

```text
update
test
stuff
asd
```

---

# 6. Viewing Commit History

To view a compact commit history:

```bash
git log --oneline
```

Example:

```text
058c5ae Add remote practice section
ed47146 Merge branch 'feature/conflict-practice'
26031dc Complete Git workflow on main
```

To see branches and merges visually:

```bash
git log --oneline --graph --decorate --all
```

This is especially useful when working with multiple branches.

---

# 7. Understanding HEAD

`HEAD` represents my current position in the Git history.

For example:

```text
HEAD -> main
```

means that I am currently working on the `main` branch.

---

# 8. Understanding origin/main

`origin/main` is a **remote-tracking branch**.

It represents my local Git repository's latest known state of the remote `main` branch.

Important:

`origin/main` is not a live connection to GitHub.

To update my knowledge of the remote repository, I can run:

```bash
git fetch
```

---

# 9. Pushing Changes

To send local commits to GitHub:

```bash
git push
```

Before push:

```text
LOCAL

A → B → C
        ↑
       main


REMOTE

A → B
    ↑
origin/main
```

After push:

```text
A → B → C
        ↑
   main / origin/main
```

---

# 10. Fetching Remote Changes

To check for new commits and branch information from the remote repository:

```bash
git fetch
```

Fetch:

- downloads information about remote changes
- updates remote-tracking branches such as `origin/main`
- does not automatically modify my current working files
- does not automatically move my local `main` branch

We tested this by making a change directly on GitHub.

Before fetching, local Git still believed:

```text
main → ed47146
origin/main → ed47146
```

After:

```bash
git fetch
```

Git discovered the new remote commit:

```text
main → ed47146
             \
              058c5ae ← origin/main
```

---

# 11. Inspecting Remote Changes

To see commits that exist on `origin/main` but not on my local `main`:

```bash
git log main..origin/main --oneline
```

To inspect the file changes:

```bash
git diff main..origin/main
```

A useful workflow is:

```text
git fetch
    ↓
git log main..origin/main --oneline
    ↓
git diff main..origin/main
    ↓
git pull
```

This allows me to inspect incoming changes before applying them.

---

# 12. Pulling Remote Changes

To bring remote changes into my local branch:

```bash
git pull
```

A simplified mental model is:

```text
git pull
≈
git fetch
+
integrate remote changes into the current local branch
```

We used `git pull` to retrieve the `Add remote practice section` commit that was created directly on GitHub.

---

# 13. Cloning a Repository

When a repository already exists remotely and I want to download it for the first time:

```bash
git clone <repository-url>
```

During our practice, we used:

```bash
git clone https://github.com/ozaysevinc/rpa-architect-learning.git rpa-architect-learning-clone
```

Clone automatically:

```text
downloads the project files
+
downloads Git history
+
creates the .git directory
+
configures the origin remote
+
checks out the default branch
```

Therefore, after cloning an existing repository, I normally do not need to run `git init` or manually configure `origin`.

---

# 14. Checking Remote Configuration

To see configured remote repositories:

```bash
git remote -v
```

This displays the remote addresses used for fetch and push operations.

---

# 15. Discarding an Unstaged Change

If I modify a file but have not staged it yet and want to discard the change:

```bash
git restore README.md
```

This restores