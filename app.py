import streamlit as st


st.set_page_config(page_title="Git Notes", page_icon="🌿", layout="wide")

NOTE_SECTIONS = [
    ("Commit habits", "Keep each commit small enough that the purpose is obvious from the subject line."),
    ("Branching", "Create short-lived branches for features or fixes, then merge them back when they are ready."),
    ("Recovery", "Stash work in progress when you need a clean working tree, and use revert when history is already shared."),
]

TOPICS = [
    {
        "title": "Small, Focused Commits",
        "summary": "Each commit should describe one topic so history stays readable and safe to revert.",
    },
    {
        "title": "Interactive Staging",
        "summary": "Use patch mode to stage only the exact lines that belong to the next commit.",
    },
    {
        "title": "Merge and Rebase",
        "summary": "Merge keeps branch context, while rebase cleans up local history before sharing.",
    },
    {
        "title": "Conflict Resolution",
        "summary": "Conflicts happen when Git cannot decide which change should win without human input.",
    },
    {
        "title": "Stash, Cherry-Pick, Revert, and Tag",
        "summary": "These commands help you save WIP, apply a specific commit, undo safely, and mark milestones.",
    },
]

st.title("Git Notes")
st.write("A small notebook-style app for tracking Git ideas, reminders, and common commands.")

left, right = st.columns([2, 1])

with left:
    st.subheader("General Reminder")
    st.write(
        "Git is most useful when the history stays clear. Small commits, short-lived branches, "
        "and a quick review before pushing usually save time later."
    )

    st.subheader("Study Notes")
    for topic in TOPICS:
        with st.container():
            st.markdown(f"### {topic['title']}")
            st.write(topic["summary"])
            st.markdown("---")

    st.subheader("Common Workflow")
    st.code(
        "git switch -c feature/my-topic\n"
        "git add -p\n"
        "git commit\n"
        "git switch main\n"
        "git merge feature/my-topic",
        language="bash",
    )

    st.subheader("Command Reference")
    st.code(
        "git stash push -u\n"
        "git cherry-pick <commit>\n"
        "git revert <commit>\n"
        "git tag -a v0.2.0 -m 'notes milestone'",
        language="bash",
    )

    st.subheader("GitHub Notes")
    st.write(
        "Git itself handles commits, branches, merges, and rebases. On GitHub, pull requests "
        "and review comments are useful when a branch is ready for feedback."
    )

with right:
    st.subheader("Recent Notes")
    for label, description in NOTE_SECTIONS:
        st.markdown(f"**{label}**")
        st.write(description)

    st.subheader("Command Checklist")
    st.markdown(
        "- Review the working tree with `git status`\n"
        "- Stage carefully with `git add -p`\n"
        "- Inspect commits with `git log --oneline --graph`\n"
        "- Sync or publish with `git push` and `git pull`"
    )

    st.subheader("Conflict Reminder")
    st.write(
        "When a conflict appears, inspect the markers, keep the final version you want, "
        "stage the file, and then finish the merge or rebase."
    )

    st.subheader("Tagging Tip")
    st.write("Create annotated tags when you want to mark a clear release or milestone.")
