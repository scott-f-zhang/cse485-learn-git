import streamlit as st


st.set_page_config(page_title="Git Learning Journey", page_icon="🌿")

WEEKLY_PLAN = [
    ("Week 1", "Repository setup, staging, commit messages, and reviewing changes."),
    ("Week 2", "Branches, merge vs rebase, conflict handling, and pull requests."),
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
]

st.title("Git Learning Journey")
st.write("This small app introduces a two-week plan for learning Git in English.")

st.subheader("Why Git matters")
st.write(
    "Git is more than a backup tool. It helps developers organize changes, "
    "work safely in branches, and collaborate through clear history."
)

st.subheader("Two-Week Study Plan")
for label, description in WEEKLY_PLAN:
    st.markdown(f"**{label}**")
    st.write(description)

st.subheader("Core Topics")
for topic in TOPICS:
    with st.container(border=True):
        st.markdown(f"### {topic['title']}")
        st.write(topic["summary"])

st.subheader("Workflow Notes")
st.code(
    "git switch -c feature/my-topic\n"
    "git add -p\n"
    "git commit\n"
    "git switch main\n"
    "git merge feature/my-topic",
    language="bash",
)

st.subheader("GitHub Collaboration")
st.write(
    "Git itself handles commits, branches, merges, and rebases. Pull requests, "
    "review comments, and branch protection rules are platform features from GitHub."
)

st.subheader("Conflict Reminder")
st.write(
    "When a conflict appears, inspect the markers, write the final version you want, "
    "stage the file, and complete the merge or rebase."
)
