# GitHub 上传指南

## 快速上传步骤

### 方法 1: 使用 GitHub CLI (推荐)

```bash
# 1. 安装 gh (如果还没安装)
sudo apt install gh  # Ubuntu/Debian
brew install gh      # macOS

# 2. 登录 GitHub
gh auth login

# 3. 创建新仓库
cd /tmp/world-news-skill
gh repo create world-news-aggregator-skill --public --source=. --push

# 完成！访问 https://github.com/BODYsuperman/world-news-aggregator-skill
```

### 方法 2: 使用 Git 命令

```bash
# 1. 初始化 Git
cd /tmp/world-news-skill
git init

# 2. 添加所有文件
git add .

# 3. 首次提交
git commit -m "Initial commit: World News Aggregator Skill"

# 4. 在 GitHub 创建空仓库
# 访问 https://github.com/new
# 仓库名：world-news-aggregator-skill
# 可见性：Public
# 不要勾选"Add README"

# 5. 关联远程仓库并推送
git remote add origin https://github.com/BODYsuperman/world-news-aggregator-skill.git
git branch -M main
git push -u origin main
```

### 方法 3: GitHub Desktop (图形界面)

1. 下载并安装 [GitHub Desktop](https://desktop.github.com/)
2. 打开 GitHub Desktop
3. File → Add Local Repository → 选择 `/tmp/world-news-skill`
4. File → Publish Repository
5. 设置仓库名：`world-news-aggregator-skill`
6. 点击 Publish Repository

---

## 仓库信息

- **仓库名**: `world-news-aggregator-skill`
- **描述**: 全球信息参考 - 多元聚合全球科技、股市、AI 论文、军事技术、政策情报
- **可见性**: Public
- **License**: MIT

---

## 上传后要做的事

### 1. 添加仓库主题 (Topics)
在仓库页面添加以下 topics:
- `openclaw`
- `skill`
- `news-aggregator`
- `ai`
- `global-news`
- `intelligence`

### 2. 添加 GitHub Actions Badge (可选)
在 README.md 顶部添加:
```markdown
[![Stars](https://img.shields.io/github/stars/BODYsuperman/world-news-aggregator-skill?style=social)](https://github.com/BODYsuperman/world-news-aggregator-skill)
```

### 3. 分享你的 Skill
- 在 OpenClaw 社区分享
- 提交到 ClawHub (https://clawhub.com)
- 在社交媒体分享

---

## 常见问题

### Q: 提示 "remote: Repository not found"
A: 确保你已经在 GitHub 创建了空仓库，并且 URL 正确。

### Q: 提示 "Permission denied"
A: 检查你的 GitHub 登录状态：
```bash
gh auth status
```

### Q: 想修改 README 怎么办？
A: 直接在 GitHub 网页上编辑，或者本地修改后推送：
```bash
git add README.md
git commit -m "Update README"
git push
```

---

*祝你上传顺利！* 🚀
