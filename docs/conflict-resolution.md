# Merge Conflict Playbook

1. Run `git status` to see the conflicted files.
2. Open the files and inspect the conflict markers.
3. Keep the final content you want and delete the markers.
4. Run `git add` on each resolved file.
5. Finish with `git commit` or `git rebase --continue`.

If the merge or rebase becomes too messy, abort it and start again with `git merge --abort` or `git rebase --abort`.
