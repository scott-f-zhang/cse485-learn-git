import streamlit as st


st.set_page_config(page_title="Git Learning Journey", page_icon="🌿")

WEEKLY_PLAN = [
    ("Week 1", "Repository setup, staging, commit messages, and reviewing changes."),
    ("Week 2", "Branches, merge vs rebase, conflict handling, and pull requests."),
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
