"""Known error messages and their explanations."""

KNOWN_ERRORS = [
    {
        "name": "Git push rejected",
        "keywords": [
            "git push rejected",
            "failed to push some refs",
            "fetch first",
            "non fast forward",
            "remote contains work",
        ],
        "meaning": (
            "Your local branch cannot be pushed because the remote branch has "
            "changes that your local copy does not have yet."
        ),
        "fix": (
            "Pull the latest remote changes first, resolve any merge or rebase "
            "conflicts, and then push again. A common flow is "
            "`git pull --rebase origin main` followed by `git push origin main`."
        ),
        "why_it_happened": (
            "Someone else pushed new commits, or the remote branch changed after "
            "your last pull, so Git blocked the push to avoid overwriting work."
        ),
    },
    {
        "name": "Module not found",
        "keywords": [
            "module not found",
            "modulenotfounderror",
            "no module named",
            "cannot find module",
        ],
        "meaning": (
            "Your program is trying to import or load a module that is not "
            "available in the current environment or path."
        ),
        "fix": (
            "Install the missing package, double-check the import name, and make "
            "sure the correct virtual environment is active. For Python, that "
            "often means running something like `pip install package-name`."
        ),
        "why_it_happened": (
            "The dependency may not be installed, the module name may be wrong, "
            "or the command is running in a different environment than expected."
        ),
    },
    {
        "name": "Permission denied",
        "keywords": [
            "permission denied",
            "access is denied",
            "operation not permitted",
            "eacces",
        ],
        "meaning": (
            "The operating system blocked the action because the current user or "
            "process does not have enough access rights."
        ),
        "fix": (
            "Check file or folder permissions, confirm the path is correct, close "
            "any program that may be locking the file, and rerun the command with "
            "the right permissions if needed."
        ),
        "why_it_happened": (
            "This usually happens when you try to read, write, execute, or modify "
            "something that your current user account is not allowed to access."
        ),
    },
]


def get_known_errors() -> list[dict[str, str | list[str]]]:
    """Return the in-memory error database."""
    return KNOWN_ERRORS
