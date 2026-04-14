# Getting Started — SCM 478

Follow these steps before the first day of class.

---

## Step 1: Install Python

Download and install **Python 3.11 or higher** from [python.org](https://www.python.org/downloads/).

During installation on Windows, check **"Add Python to PATH"**.

Verify in a terminal:
```bash
python --version
```

---

## Step 2: Install Git

Download from [git-scm.com](https://git-scm.com/downloads) and install with defaults.

Verify:
```bash
git --version
```

---

## Step 3: Create a GitHub Account

Go to [github.com](https://github.com) and create a free account if you don't have one. Use your BYU-Idaho email.

---

## Step 4: Clone the Course Repository

```bash
git clone https://github.com/[instructor-repo-url]/scm478-course.git
cd scm478-course
```

*(The exact URL will be provided on Canvas.)*

---

## Step 5: Create Your Own Course Repo

1. On GitHub, create a **new public repository** named `scm478-[yourname]`
2. Clone it locally
3. This is where you will submit all homework and in-class work

---

## Step 6: Install Python Packages

From inside your local copy of the course repo:

```bash
pip install streamlit pandas plotly openpyxl
```

For SQLite weeks (Week 3+), no extra install needed — SQLite ships with Python.

---

## Step 7: Run the Self-Check

```bash
python setup/self_check.py
```

You should see all green checkmarks. If anything fails, see [self-check-setup.md](self-check-setup.md) for troubleshooting.

---

## Recommended Tools

- **VS Code** — free editor with great Python support
  - Install the Python and Pylance extensions
- **GitHub Desktop** — visual Git client if you prefer not to use the terminal

---

## Getting Help

- Post in the Canvas discussion board
- Ask a classmate
- Come to office hours (see Canvas for times)
