import streamlit as st

# Main function
def main():
    st.title("Digital Art Donation for Charity Auction")

    # Sidebar for user input
    st.sidebar.header("Submit Artwork")
    artwork_title = st.sidebar.text_input("Artwork Title")
    artist_name = st.sidebar.text_input("Artist")
    description = st.sidebar.text_area("Description")
    google_drive_link = st.sidebar.text_input("Google Drive Link")

    if st.sidebar.button("Submit"):
        st.sidebar.success("Artwork submitted successfully!")

    # Display submitted artwork details and embedded Google Drive link
    st.header("Submitted Artworks")
    if artwork_title and artist_name and description and google_drive_link:
        st.subheader(f"{artwork_title} by {artist_name}")
        st.write(description)
        st.components.v1.iframe(google_drive_link, height=400)

if __name__ == "__main__":
    main()
