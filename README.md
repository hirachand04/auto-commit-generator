# 🤖 Auto Commit Generator - Step by Step Guide

A Python script that automatically generates backdated Git commits to fill your GitHub contribution graph.  This guide will walk you through everything from scratch! 

## ⚠️ Important Disclaimer

**This project is strictly for educational purposes only.**

- ✅ Use to learn Git internals and automation
- ✅ Test in your own repositories (public or private)
- ❌ Do NOT use to misrepresent your actual work
- ⚠️ Authentic contributions are always more valuable than automated ones

---

## 📋 What You'll Need

Before starting, make sure you have:

- [ ] A computer (Windows, Mac, or Linux)
- [ ] Internet connection
- [ ] GitHub account (free)
- [ ] 15 minutes of your time

That's it! We'll install everything else together.

---

## 🚀 Complete Setup Guide

### Step 1: Install Python

**Check if Python is already installed:**

```bash
python --version
```

**If not installed:**

- **Windows**: Download from https://python.org/downloads (check "Add Python to PATH")
- **Mac**: `brew install python3` or download from python.org
- **Linux**: `sudo apt install python3` (Ubuntu/Debian) or `sudo yum install python3` (CentOS/Fedora)

**Verify installation:**

```bash
python --version
# Should show: Python 3.x.x
```

---

### Step 2: Install Git

**Check if Git is already installed:**

```bash
git --version
```

**If not installed:**

- **Windows**: Download from https://git-scm.com/download/win
- **Mac**: `brew install git` or download from git-scm.com
- **Linux**: `sudo apt install git` (Ubuntu/Debian) or `sudo yum install git` (CentOS/Fedora)

**Verify installation:**

```bash
git --version
# Should show: git version 2.x.x
```

---

### Step 3: Configure Git (First Time Only)

Set your name and email (this will appear in commits):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Verify configuration:**

```bash
git config --global user.name
git config --global user.email
```

---

### Step 4: Create a GitHub Repository

You can use this script with **any repository** (new or existing, public or private). 

#### Option A: Create a New Repository

1. Go to https://github.com/new
2. Repository name: `auto-commit-generator` (or any name you like)
3. Description: "Automated commit generator for learning Git"
4. Choose **Public** or **Private** (your choice!)
5. ✅ Check "Add a README file"
6. Click **"Create repository"**

#### Option B: Use an Existing Repository

You can use any repository you already own. Just make sure:
- You have write access
- You're okay with adding automated commits
- Consider using a dedicated/test repository

---

### Step 5: Set Up Authentication

GitHub needs to verify it's you pushing commits. Choose **one** method:

#### 🔑 Method A: SSH Keys (Recommended - One-time setup)

**Generate SSH key:**

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

Press Enter 3 times (accept defaults, no passphrase needed for simplicity).

**Start SSH agent:**

```bash
# Mac/Linux:
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Windows (Git Bash):
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519
```

**Copy your public key:**

```bash
# Mac/Linux:
cat ~/.ssh/id_ed25519.pub

# Windows (Git Bash):
cat ~/.ssh/id_ed25519.pub

# Windows (PowerShell):
type $env:USERPROFILE\.ssh\id_ed25519.pub
```

**Add to GitHub:**

1. Copy the entire output (starts with `ssh-ed25519`)
2. Go to https://github.com/settings/keys
3. Click **"New SSH key"**
4. Title: "My Computer"
5.  Paste the key
6. Click **"Add SSH key"**

**Test connection:**

```bash
ssh -T git@github.com
# Should say: "Hi username! You've successfully authenticated..."
```

#### 🔐 Method B: Personal Access Token (Alternative)

**Generate token:**

1. Go to https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Note: "Auto Commit Generator"
4.  Expiration: Choose duration (90 days recommended)
5. ✅ Check **"repo"** (full control of private repositories)
6. Click **"Generate token"**
7. **COPY THE TOKEN NOW** (you won't see it again!)

**Save token safely:**

```bash
# You'll use this token as a password when pushing
# Format: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### Step 6: Clone the Auto-Commit Generator

**Create a projects folder:**

```bash
# Windows:
cd C:\Users\YourUsername\Documents
mkdir GitHub
cd GitHub

# Mac/Linux:
cd ~/Documents
mkdir GitHub
cd GitHub
```

**Clone this repository:**

```bash
git clone https://github.com/hirachand04/auto-commit-generator.git
cd auto-commit-generator
```

**Verify files:**

```bash
ls
# Should show: main.py, README.md, LICENSE, requirements.txt, . gitignore
```

---

### Step 7: Connect to Your Repository

Now we'll connect this script to **your** repository (where commits will be pushed).

**Option A: If you created a NEW repository in Step 4**

```bash
# Remove the original remote
git remote remove origin

# Add YOUR repository (replace USERNAME and REPO_NAME)
# For SSH (if you set up SSH keys):
git remote add origin git@github.com:USERNAME/REPO_NAME. git

# For HTTPS (if you're using Personal Access Token):
git remote add origin https://github.com/USERNAME/REPO_NAME.git
```

**Option B: If you want to use an EXISTING repository**

```bash
# Navigate out of auto-commit-generator
cd .. 

# Clone YOUR existing repository
git clone git@github.com:USERNAME/YOUR_REPO. git
# OR with HTTPS:
git clone https://github.com/USERNAME/YOUR_REPO.git

cd YOUR_REPO

# Copy the main.py script here
cp ../auto-commit-generator/main. py . 
```

**Verify remote is set correctly:**

```bash
git remote -v
# Should show YOUR repository URL
```

**Examples:**

```bash
# Example with SSH:
git remote add origin git@github.com:johndoe/my-test-repo.git

# Example with HTTPS:
git remote add origin https://github.com/johndoe/my-test-repo. git
```

---

### Step 8: Run the Auto-Commit Generator

You're ready!  🎉

```bash
python main.py
```

**You'll see:**

```
============================================================
  Auto Commit Generator with Backdate Support
  Educational Use Only
============================================================
🔍 Checking Git configuration...
✓ Git user: Your Name
✓ Git email: your.email@example.com

🔍 Checking Git repository...
✓ Remote: git@github.com:USERNAME/REPO_NAME.git

🤔 Select time period for backdated commits:
   1. Past month (30 days, 0-10 commits/day)
   2. Past year (365 days, 0-10 commits/day)

Enter your choice (1/2):
```

**Choose your option:**

- Type `1` for **past month** (~150 commits)
- Type `2` for **past year** (~1,800 commits)

**Watch the magic happen!  ✨**

```
📅 Creating backdated commits for the past year... 
⚠️  This will create 0-10 random commits per day

✓ 2024-12-07: Created 7 commits
✓ 2024-12-08: Created 3 commits
✓ 2024-12-09: Created 9 commits
... 
✓ 2025-12-06: Created 5 commits

📊 Total commits created: 1847

⬆️  Pushing to remote... 
✓ Successfully pushed to remote! 

============================================================
  ✅ Success!  Commits created and pushed. 
============================================================

🌟 Check your GitHub contribution graph!
   It may take a few minutes to update. 
```

---

### Step 9: Check Your Results

**View your repository:**

```bash
# Open your repository in browser
# Replace USERNAME and REPO_NAME:
https://github.com/USERNAME/REPO_NAME
```

You should see:
- ✅ A new file called `commits.txt`
- ✅ Hundreds or thousands of commits
- ✅ All commits dated in the past

**View your contribution graph:**

```bash
# Open your profile:
https://github.com/USERNAME
```

You should see:
- 🟩 Green squares filled in for the past month or year! 
- 📊 Your commit count increased significantly

---

## 🎯 How It Works

### The Process

1. **Calculate Date Range**: Script determines 30 or 365 days back from today
2. **Random Generation**: For each day, randomly picks 0-10 commits
3. **Random Timing**: Each commit gets a random hour:minute:second
4. **File Update**: Appends timestamp to `commits.txt`
5. **Git Date Magic**: Uses environment variables to set commit date:
   ```bash
   GIT_AUTHOR_DATE="2024-06-15 14:23:45"
   GIT_COMMITTER_DATE="2024-06-15 14:23:45"
   ```
6. **Commit Creation**: Creates commit with custom date
7. **Force Push**: Pushes all commits to GitHub (rewrites history)

### Expected Results

| Option | Days | Avg Commits/Day | Total Commits | Time |
|--------|------|-----------------|---------------|------|
| Month  | 30   | 5               | ~150          | 1min |
| Year   | 365  | 5               | ~1,800        | 5min |

---

## 🔧 Git Commands Reference

Here are all the Git commands this script uses:

```bash
# Check Git configuration
git config user.name
git config user.email

# Verify Git repository
git rev-parse --git-dir

# Check remote URL
git remote get-url origin

# Stage file
git add commits.txt

# Create commit with custom date
GIT_AUTHOR_DATE="2024-12-07 10:30:00" \
GIT_COMMITTER_DATE="2024-12-07 10:30:00" \
git commit -m "Auto-commit: 2024-12-07 10:30:00"

# Push to remote (force push to rewrite history)
git push origin HEAD --force

# View commit history
git log --oneline

# View contribution stats
git shortlog -sn
```

---

## 🐛 Troubleshooting

### Problem: "python: command not found"

**Solution:**

```bash
# Try python3 instead:
python3 main.py

# Or reinstall Python from python.org
```

---

### Problem: "git: command not found"

**Solution:**

```bash
# Install Git:
# Windows: https://git-scm.com/download/win
# Mac: brew install git
# Linux: sudo apt install git
```

---

### Problem: "Permission denied (publickey)"

**Solution:**

```bash
# Test SSH connection:
ssh -T git@github.com

# If fails, check SSH key is added:
cat ~/.ssh/id_ed25519.pub
# Copy and add to https://github.com/settings/keys

# Or use HTTPS with Personal Access Token instead
git remote set-url origin https://github.com/USERNAME/REPO. git
```

---

### Problem: "Authentication failed" (HTTPS)

**Solution:**

```bash
# Make sure you're using token as password, not your GitHub password
# Token format: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# On Windows, you might need to update stored credentials:
# Control Panel → Credential Manager → Windows Credentials
# Remove GitHub credentials and try again
```

---

### Problem: "Updates were rejected"

**Solution:**

```bash
# Pull latest changes:
git pull origin main --allow-unrelated-histories

# Or force push (WARNING: overwrites remote):
git push origin main --force
```

---

### Problem: "Not a git repository"

**Solution:**

```bash
# Make sure you're in the right directory:
cd ~/Documents/GitHub/auto-commit-generator

# Check if . git folder exists:
ls -la
# Should show . git folder

# If not, initialize:
git init
git remote add origin git@github.com:USERNAME/REPO. git
```

---

### Problem: "Script runs but no commits appear on GitHub"

**Solution:**

```bash
# Check if commits were created locally:
git log --oneline

# Check remote URL is correct:
git remote -v

# Try pushing manually:
git push origin main --force

# Wait a few minutes - GitHub can take time to update contribution graph
```

---

## 📊 Using with Different Repositories

### Scenario 1: Test Repository (Recommended)

```bash
# Create dedicated test repo on GitHub
# Clone it
git clone git@github.com:USERNAME/test-commits.git
cd test-commits

# Copy main.py here
curl -o main.py https://raw.githubusercontent.com/hirachand04/auto-commit-generator/main/main.py

# Run
python main.py
```

### Scenario 2: Existing Private Repository

```bash
# Clone your existing repo
git clone git@github.com:USERNAME/my-private-repo.git
cd my-private-repo

# Create a new branch (optional, safer)
git checkout -b auto-commits

# Copy main.py here
# Run script
python main.py

# Merge to main if desired (optional)
git checkout main
git merge auto-commits
```

### Scenario 3: Multiple Repositories

```bash
# You can run this on multiple repos! 
cd ~/Documents/GitHub/repo1
python path/to/main.py

cd ~/Documents/GitHub/repo2
python path/to/main. py
```

---

## ⚙️ Advanced Usage

### Custom Commit Range

Edit `main.py` and modify the `create_backdated_commits()` function:

```python
# For 90 days:
success = create_backdated_commits(days=90)

# For 6 months (180 days):
success = create_backdated_commits(days=180)

# For 2 years (730 days):
success = create_backdated_commits(days=730)
```

### Change Commit Frequency

Edit the random range in `main.py`:

```python
# Current: 0-10 commits per day
num_commits = random.randint(0, 10)

# For 1-5 commits per day (lighter):
num_commits = random.randint(1, 5)

# For 5-15 commits per day (heavier):
num_commits = random.randint(5, 15)
```

### Customize Commit Messages

Edit `create_commit_for_date()` function:

```python
# Current format:
commit_message = f"Auto-commit: {date_str}"

# Custom messages:
commit_message = f"Daily update: {date_str}"
commit_message = f"Learning progress: {date_str}"
commit_message = f"Code practice: {date_str}"
```

---

## 🔐 Security & Privacy

### ✅ Best Practices

- Use **private repositories** for testing
- Never commit sensitive data (passwords, keys, tokens)
- Keep SSH keys in `~/.ssh/` with proper permissions (600)
- Don't share your Personal Access Token
- Use tokens with minimal required permissions

### 🗑️ Cleaning Up

**Remove all auto-generated commits:**

```bash
# Reset to before script ran (WARNING: loses all commits)
git reset --hard COMMIT_HASH

# Or delete the repository and start fresh
```

**Revoke Access Token:**

```bash
# Go to https://github.com/settings/tokens
# Click "Delete" on the token you created
```

---

## ⚖️ Ethical Guidelines

### ✅ DO Use This For:

- Learning how Git dates work
- Understanding Git internals
- Practicing Python automation
- Testing in your own repositories
- Educational experiments

### ❌ DON'T Use This For:

- Deceiving employers or recruiters
- Misrepresenting your actual work
- Public projects with collaborators
- Violating GitHub Terms of Service
- Claiming false expertise

### 💭 Remember:

> "The green squares don't define you. Your actual skills, projects, and contributions do."

Employers can:
- Check commit quality and code
- Review actual projects and PRs
- Verify contributions through interviews
- See through artificial patterns

**Focus on building real skills and real projects. ** 🌟

---

## 📚 Learning Resources

- **Git Basics**: https://git-scm. com/book/en/v2
- **GitHub Docs**: https://docs.github.com/
- **Python Subprocess**: https://docs.python.org/3/library/subprocess.html
- **Git Internals**: https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain
- **SSH Keys Guide**: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

---

## 🤝 Contributing

Found a bug?  Have a suggestion? 

1. Fork this repository
2. Create a branch (`git checkout -b feature/improvement`)
3. Make your changes
4.  Commit (`git commit -am 'Add new feature'`)
5. Push (`git push origin feature/improvement`)
6. Open a Pull Request

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file

You're free to use, modify, and distribute this code.

---

## 🙏 Acknowledgments

- Built for educational purposes
- Inspired by curiosity about Git internals
- Thanks to the open-source community

---

## ⭐ Final Thoughts

This project teaches you about:
- Git commit mechanics
- Date manipulation in Git
- Python subprocess automation
- GitHub API interactions
- Random number generation

But remember: **Your real value as a developer comes from:**

- 💡 Solving real problems
- 📖 Continuous learning
- 🤝 Helping others
- 🏗️ Building meaningful projects
- 🌱 Growing your skills genuinely

Use this tool to **learn**, not to **deceive**. 

Happy coding! 🚀✨

---

**Made with ❤️ for education and learning**
