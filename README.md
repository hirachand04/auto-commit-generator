# 🤖 Auto Commit Generator

Fill your GitHub contribution graph with backdated commits.   **For learning only.**

---

## 🚀 5-Minute Setup

### Step 1: Install Python & Git

```bash
# Check if already installed:
python --version
git --version

# If missing, install from:
# Python: https://python. org/downloads
# Git: https://git-scm.com/downloads
```

### Step 2: Configure Git

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Create GitHub Token (Required for Authentication)

1. Visit: https://github.com/settings/tokens
2. Click **"Generate new token (classic)"**
3. Name: `commits`
4. Check: ✅ **repo**
5. Click **"Generate"**
6. **Copy the token** (starts with `ghp_`) - keep it ready!

### Step 4: Setup

```bash
# Download
git clone https://github.com/hirachand04/auto-commit-generator.git
cd auto-commit-generator

# Connect to YOUR repo (replace USERNAME and REPO!)
git remote set-url origin https://github.com/USERNAME/REPO.git
```

### Step 5: Run

```bash
python main.py
```

**When prompted for credentials:**
```
Username: YOUR-USERNAME
Password: [PASTE YOUR TOKEN HERE - NOT your GitHub password!]
```

- Enter `1` for past month (~150 commits)
- Enter `2` for past year (~1,800 commits)

**💡 To avoid entering token every time:**
```bash
git config --global credential.helper store
```
Next time, Git will remember your token!

### Step 6: Check

Visit `https://github.com/USERNAME` - see your green squares! 🟩

---

## 🔧 Use Your Own Repository

**Don't have a repo?  Create one:**

1. Go to https://github.com/new
2. Name it anything (e. g., `test-commits`)
3. Click "Create repository"
4. Copy the URL: `https://github.com/USERNAME/REPO.git`

**Then connect:**

```bash
cd auto-commit-generator
git remote set-url origin https://github.com/USERNAME/REPO.git
python main.py
```

---

## ⚠️ Troubleshooting

**"Authentication failed"**
→ Use your **token** (ghp_xxx.. .) as password, NOT your GitHub password

**"python not found"**
→ Try `python3 main.py`

**"Updates rejected"**
→ Run: `git push origin main --force`

**"Credentials keep asking"**
→ Run: `git config --global credential.helper store`

**"remote: Support for password authentication was removed"**
→ You're using your GitHub password instead of the token!  Use the token (ghp_xxx...)

---

## 🔐 Alternative: Use SSH (No Token Needed!)

If you don't want to use tokens:

```bash
# 1. Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"
# Press Enter 3 times

# 2. Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 3. Copy public key
cat ~/.ssh/id_ed25519.pub

# 4. Add to GitHub: https://github.com/settings/keys

# 5. Use SSH URL instead
git remote set-url origin git@github.com:USERNAME/REPO.git

# 6. Run (no password needed!)
python main.py
```

---

## ⚙️ Customize

**Change time period** - Edit `main.py` line 155:

```python
create_backdated_commits(days=90)  # 3 months
create_backdated_commits(days=180) # 6 months
```

**Change commits per day** - Edit line 92:

```python
num_commits = random.randint(1, 5)  # 1-5 per day
num_commits = random.randint(5, 15) # 5-15 per day
```

---

## 📖 What It Does

```
1.  Creates commits for past 30 or 365 days
2. Random 0-10 commits per day
3. Each commit has random time
4. Uses your token to push to GitHub
5. Fills your contribution graph
```

**Files created:** `commits.txt` (contains timestamps)

---

## ⚖️ Ethics

✅ **Use for:** Learning Git, testing, personal projects  
❌ **Don't use for:** Deceiving employers, faking experience

> Real skills > Green squares

---

## 📄 License

MIT License - Free to use for education. 

---

## 🎯 Quick Command Reference

```bash
# Setup
git clone https://github.com/hirachand04/auto-commit-generator.git
cd auto-commit-generator
git remote set-url origin https://github.com/YOUR-USERNAME/YOUR-REPO.git

# Store credentials (optional, so you don't re-enter token)
git config --global credential. helper store

# Run
python main.py
# Enter your username
# Paste your token as password

# Clean up token later
https://github. com/settings/tokens → Delete
```

---

That's it!  Simple and educational. 
