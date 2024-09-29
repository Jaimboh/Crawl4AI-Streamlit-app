 Function to generate a download link for the extracted markdown content
def download_markdown(content, filename="Web_extracted_content.md"):
    # Encode the content as base64
    b64 = base64.b64encode(content.encode()).decode()
    # Create a download link for the markdown file
    href = f'<a href="data:file/markdown;base64,{b64}" download="{filename}">Download Markdown File</a>'
    return href


# Function to display personal info in the sidebar
def display_personal_info_in_sidebar():
    # Display your picture in the sidebar
    st.sidebar.image("profile.jpg", width=150)  # Replace with the path to your image

    # Display your name and LinkedIn information in the sidebar
    st.sidebar.write("Tom Odhiambo")  
    st.sidebar.write(
        "[Connect with me on LinkedIn](https://linkedin.com/in/https://www.linkedin.com/in/tom-odhiambo-4b89b11a1/)") 

    # Add any other personal info, such as GitHub or website links in the sidebar
    st.sidebar.write("[GitHub](https://github.com/Jaimboh)")  
    st.sidebar.write("[Medium](https://medium.com/@odhitom09)") 


# Streamlit App
def main():
    st.title("Crawl4AI Selenium Based Web Scraper")

    # Display personal information in the sidebar
    display_personal_info_in_sidebar()

    # URL input
    url = st.text_input("Enter the URL you want to scrape:")

    # Button to start the crawl
    if st.button("Run Crawl"):
        if url:
            # Create an instance of WebCrawler and warm it up (load necessary models)
            crawler = WebCrawler()
            crawler.warmup()

            # Run the crawler and display the result in markdown format
            result = crawler.run(url=url)
            st.markdown(result.markdown)

            # Download markdown file
            st.markdown(download_markdown(result.markdown), unsafe_allow_html=True)
        else:
            st.warning("Please enter a valid URL.")


if __name__ == "__main__":
    main()
