# Error Explainer

Error Explainer is a small Streamlit app that helps beginners understand common developer errors. Paste an error message into the UI and the app will try to match it against a built-in database using case-insensitive partial keyword matching.

## Project Description

The project is structured like a simple real-world Python app:

```text
.
|-- app.py
|-- core/
|   |-- database.py
|   |-- formatter.py
|   `-- matcher.py
|-- requirements.txt
|-- README.md
`-- .gitignore
```

It currently explains these error types:

- `git push rejected` / `failed to push some refs`
- `module not found`
- `permission denied`

## Setup Instructions

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:

   Mac/Linux:

   ```bash
   source .venv/bin/activate
   ```

   Windows:

   ```powershell
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

## Example Input and Output

Example input:

```text
failed to push some refs to origin
```

Example output:

```text
Meaning:
Your local branch cannot be pushed because the remote branch has changes that your local copy does not have yet.

Fix:
Pull the latest remote changes first, resolve any merge or rebase conflicts, and then push again.

Why it happened:
Someone else pushed new commits, or the remote branch changed after your last pull, so Git blocked the push to avoid overwriting work.
```

## Matching Logic

- Matching is case insensitive
- Phrase matches score higher than loose word overlap
- Partial keyword overlap is enough to find a useful match

## Roadmap

- Add more Python, Git, and JavaScript errors
- Add tests for the matcher and formatter
- Support custom user-defined error entries
- Add a fallback explanation flow for unknown errors
