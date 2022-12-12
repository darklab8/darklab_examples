https://stackoverflow.com/questions/7295511/how-to-add-a-file-to-the-first-commit-on-a-git-repo

In case anyone needs to do this in the future, here's an easier solution. I recently had to modify an early commit because of a problematic typo in the commit message. This works for changing anything about a previous commit. I modified Charles Bailey's answer here.

# Go back to the commit you want to change (detach HEAD)
git checkout <sha1_for_commit_to_change>

# Make any changes now (add your new file) then add them to the index
git add <new_files>

# amend the current commit
git commit --amend

# temporarily tag this new commit
# (or you could remember the new commit sha1 manually)
git tag tmp

# go back to the original branch (assume master for this example)
git checkout master

# Replay all the commits after the change onto the new initial commit
git rebase --preserve-merges --onto tmp <sha1_for_commit_to_change>

# remove the temporary tag
git tag -d tmp
Note that this will change all of your commit IDs following the amended commit, so it's not recommended on a public repository. Also, you'll have to recreate all of your tags