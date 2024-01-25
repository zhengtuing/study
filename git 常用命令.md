Git 常用命令

### 基础命令

- `git init`：在当前目录中初始化一个新的Git仓库。
- `git clone [url]`：克隆一个远程仓库到本地。
- `git add [file]`：将文件添加到暂存区。
- `git commit -m "[commit message]"`：将暂存区的更改提交到仓库。
- `git status`：查看仓库当前的状态。
- `git log`：查看提交历史。

### 分支与合并

- `git branch`：列出、创建或删除分支。
- `git checkout [branch-name]`：切换到指定分支。
- `git merge [branch]`：将指定分支合并到当前分支。
- `git branch -d [branch-name]`：删除一个分支。

### 远程仓库操作

- `git remote add [remote-name] [url]`：添加一个新的远程仓库。
- `git fetch [remote-name]`：从远程仓库下载新分支与数据。
- `git pull [remote-name] [branch-name]`：从远程仓库获取并合并指定分支。
- `git push [remote-name] [branch-name]`：将本地分支的更新推送到远程仓库。

### 撤销更改

- `git checkout -- [file]`：撤销对文件的修改。
- `git reset [file]`：从暂存区撤销对文件的修改。
- `git reset --hard [commit]`：撤销所有更改，回到指定提交。
- `git revert [commit]`：撤销指定提交的更改，并创建一个新的提交。

### 高级命令

- `git rebase [branch]`：变基操作，用于重写提交历史。
- `git stash`：暂时保存未提交的更改。
- `git stash pop`：应用之前暂存的更改。




要查看远程仓库的分支，可以使用下面的Git命令：

1. **查看远程分支列表**：
   - 使用 `git branch -r`：这个命令会列出所有远程跟踪的分支。
   - 或者使用 `git branch -a`：这个命令不仅会显示本地分支，还会显示远程分支。
2. **获取最新的远程分支信息**：
   - 在查看远程分支之前，你可能需要先通过 `git fetch [remote-name]` 来获取最新的远程仓库数据。这个命令会下载远程仓库的最新信息，但不会自动合并或修改你当前的工作。
3. **查看远程仓库详细信息**：
   - 使用 `git remote show [remote-name]`：这个命令会显示更详细的信息，包括每个分支的跟踪情况和是否需要合并。