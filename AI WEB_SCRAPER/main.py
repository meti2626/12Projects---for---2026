import streamlit as st
from scrape import scrape_website


st.title("AI Web Scraper")
url = st.text_input("Enter a website URL:")

if st.button("Scrape Site"):
  st.write(f"Scraping the website: {url}")
  result = scrape_website(url)
  print(result)