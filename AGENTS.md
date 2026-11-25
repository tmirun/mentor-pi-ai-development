# MentorPi 开发约定

mini-ai 是下指令和同步提交的入口。代码、文档、配置和依赖都在 pro-ai 的项目目录中修改；开发测试、训练和调试也在 pro-ai 上执行。

1. **进入开发目录。** 从 mini-ai 执行 `ssh pro-ai.home`，登录后执行 `cd /home/pro-ai/projects/me/mentor-pi-ai-development`。若用非交互式 SSH，每次都在远端命令开头切换到这个目录。连接失败时向用户说明，不改用 mini-ai 的副本开发。
2. **核对工作区。** 在 pro-ai 执行 `hostname`、`pwd` 和 `git status --short --branch`，核对主机、目录、分支及已有改动。先读远端仓库的 `README.md`、`AGENTS.md` 和适用的上级目录指引。
3. **在 pro-ai 验证并推送。** 完成修改和相应验证后，检查差异，只暂存本次任务的改动，提交并推送到 `origin` 的对应分支。
4. **在 mini-ai 同步。** 推送成功后，回到 mini-ai 的 `~/projects/me/mentor-pi-ai-development`。确认分支相同、拉取不会覆盖已有工作后，执行 `git pull --ff-only`。如有文件冲突或分支分叉，保留现场并告知用户。

## MentorPi 实机

MentorPi 实机通过 `ssh rcar.home` 连接，登录用户名按本机 SSH 配置设置。连接前确认当前网络能够解析 `rcar.home`。
