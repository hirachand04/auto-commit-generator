#!/usr/bin/env python3
"""
Auto Commit Generator
A minimal script that automatically creates and pushes Git commits.  

EDUCATIONAL USE ONLY - Do not use to artificially inflate contribution graphs.
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run_command(command, error_message):
    """Execute a shell command and handle errors."""
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {error_message}")
        print(f"Details: {e.stderr}")
        return None
    except FileNotFoundError:
        print(f"❌ Error: Git is not installed or not in PATH")
        print("Please install Git from https://git-scm.com/")
        return None


def check_git_config():
    """Verify that Git user name and email are configured."""
    print("🔍 Checking Git configuration...")
    
    name_result = run_command(["git", "config", "user.name"], "Git user. name not configured")
    email_result = run_command(["git", "config", "user.email"], "Git user.email not configured")
    
    if not name_result or not email_result:
        print("\n⚠️  Please configure Git:")
        print('   git config user.name "Your Name"')
        print('   git config user.email "your.email@example.com"')
        return False
    
    print(f"✓ Git user: {name_result.stdout.strip()}")
    print(f"✓ Git email: {email_result.stdout.strip()}")
    return True


def check_git_repo():
    """Verify we're in a Git repository with a remote."""
    print("\n🔍 Checking Git repository...")
    
    if not run_command(["git", "rev-parse", "--git-dir"], "Not a git repository"):
        print("\n⚠️  Please initialize Git:")
        print("   git init")
        print("   git remote add origin <your-repo-url>")
        return False
    
    remote_result = run_command(["git", "remote", "get-url", "origin"], "No remote 'origin' configured")
    
    if not remote_result:
        print("\n⚠️  Please add a remote repository:")
        print("   git remote add origin <your-repo-url>")
        return False
    
    print(f"✓ Remote: {remote_result.stdout.strip()}")
    return True


def create_commit():
    """Create and push an automated commit."""
    print("\n📝 Creating auto-commit...")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_file = Path("commits.txt")
    
    try:
        with open(commit_file, "a") as f:
            f. write(f"Auto-commit: {timestamp}\n")
        print(f"✓ Updated {commit_file}")
    except IOError as e:
        print(f"❌ Error writing to {commit_file}: {e}")
        return False
    
    if not run_command(["git", "add", str(commit_file)], "Failed to stage changes"):
        return False
    print(f"✓ Staged {commit_file}")
    
    commit_message = f"Auto-commit: {timestamp}"
    if not run_command(["git", "commit", "-m", commit_message], "Failed to create commit"):
        return False
    print(f"✓ Created commit: {commit_message}")
    
    print("\n⬆️  Pushing to remote...")
    if not run_command(["git", "push", "origin", "HEAD"], "Failed to push to remote"):
        print("\n⚠️  Push failed. Common solutions:")
        print("   1.  Set up SSH keys or personal access token")
        print("   2.  Pull latest changes: git pull origin main")
        print("   3.  Check repository permissions")
        return False
    
    print("✓ Successfully pushed to remote!")
    return True


def main():
    """Main execution function."""
    print("=" * 50)
    print("  Auto Commit Generator")
    print("  Educational Use Only")
    print("=" * 50)
    
    if not check_git_config():
        sys.exit(1)
    
    if not check_git_repo():
        sys.exit(1)
    
    if create_commit():
        print("\n" + "=" * 50)
        print("  ✅ Success! Commit created and pushed.")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("  ❌ Failed to complete auto-commit.")
        print("=" * 50)
        sys. exit(1)


if __name__ == "__main__":
    main()
