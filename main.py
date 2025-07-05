import subprocess


def git_push_subprocess(repo_path, commit_message, branch='main'):
    try:
        # Change directory to the repository
        subprocess.run(['git', 'add', '.'], cwd=repo_path, check=True)
        subprocess.run(['git', 'commit', '-m', commit_message], cwd=repo_path, check=True)
        subprocess.run(['git', 'push', 'origin', branch], cwd=repo_path, check=True)
        print("Successfully pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing to GitHub: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
git_push_subprocess('path/to/your/repo', 'Automated commit via subprocess')