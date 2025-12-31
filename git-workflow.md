# Summary for making a new branch

1. `git checkout main && git pull origin main` (update everything)
2. `git checkout -b <branch>` (create a new branch)
3. *write code, do work*
4. `git add .` (add changes)
5. `git commit -m "type(scope): imperative description"` (commit, see below for format)
6. `git checkout main` (switch to main branch)
7. `git pull origin main` (just to make sure we have the latest)
8. `git merge <branch>` (merge new feature)
9. `git push origin main` (publish to remote)
10. `git branch -d <branch>` (cleanup now that branch isn't needed)

# Summary checklist for adding something to a different branch (example is main)

1. `git add . && git commit -m` "chore(wip)" (Save current work)
2. `git switch main` (switch to the new branch)
3. *Create and save files*
4. `git add <file>` (add file to the commit)
5. `git commit -m "type(scope): imperative description"` (follow conventional commit)
6. `git push origin main` (upload)
7. `git switch <previous_branch>` (return to work)
8. `git merge main` (pull updates into this branch)

# Summary of conventional commit strategy

## Standard types

| Tag | Purpose |
| :--- | :--- |
| **`feat`** | A new feature for the user (e.g., `feat(host): add laser toggle`). |
| **`fix`** | A bug fix. |
| **`docs`** | Documentation only changes (e.g., adding your Style Guide). |
| **`style`** | Formatting, missing semi-colons; no code logic changes. |
| **`refactor`** | A code change that neither fixes a bug nor adds a feature. |
| **`perf`** | A code change that improves performance. |
| **`test`** | Adding missing tests or correcting existing tests. |
| **`chore`** | Maintenance tasks (updating dependencies, build scripts, etc.). |

## My addition and usage

* **`qol` (Quality of Life)** is not part of the strict "Conventional Commits" standard, but it is a very common community extension. Use for little tweaks that make my life easier but don't add a big feature.
* **Scope** identifies the subsystem that is being worked on in this commit
* Remember to use the imperative in the description


