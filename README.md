# Git Notes App

This repository contains a small Streamlit app for keeping Git study notes and common command examples.

## Repository structure

- `app.py`: Streamlit notes app
- `docs/`: notes about workflows, pull requests, conflict handling, and local operations

## Quick command cheat sheet

```bash
git status
git add -p
git commit
git log --oneline --graph --decorate
git push origin <branch-name>
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
