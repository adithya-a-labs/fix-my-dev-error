import streamlit as st

from core.formatter import format_error_output, format_no_match_message
from core.matcher import match_error


def render_section(title: str, content: str) -> None:
    """Render one explanation block in a consistent style."""
    with st.container(border=True):
        st.markdown(f"### {title}")
        st.markdown(content)


def main() -> None:
    st.set_page_config(page_title="Error Explainer", layout="centered")

    st.title("Error Explainer")
    st.write(
        "Paste a developer error message to see what it means, how to fix it, "
        "and why it happened."
    )

    with st.form("error_form"):
        error_message = st.text_area(
            "Error message",
            placeholder="Example: failed to push some refs to 'origin/main'",
            height=140,
        )
        submitted = st.form_submit_button("Explain Error", use_container_width=True)

    st.caption(
        "Try examples like `failed to push some refs`, `ModuleNotFoundError`, "
        "or `permission denied`."
    )

    if not submitted:
        return

    if not error_message.strip():
        st.warning("Please enter an error message before submitting.")
        return

    match = match_error(error_message)

    if match is None:
        st.warning(format_no_match_message(error_message))
        return

    st.success(f"Matched error: {match['name']}")

    for title, content in format_error_output(match):
        render_section(title, content)


if __name__ == "__main__":
    main()
