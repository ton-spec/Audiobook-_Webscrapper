import pygame
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from gtts.tokenizer import pre_processors

# Define the Wikipedia URL to scrape
url = input("Enter page URL.eg: https://en.wikipedia.org/wiki/Web_scraping: ")

try:
    # Send a GET request to the URL and get the HTML content
    html_content = requests.get(url).content

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the main content of the Wikipedia page
    content = soup.find(id="mw-content-text")

    # Iterate over all the paragraphs in the main content
    for p in content.find_all("p"):
        # Get the text of the paragraph and split it into lines
        lines = p.get_text().split("\n")

        # Iterate over all the lines in the paragraph
        for line in lines:
            # Strip any leading or trailing whitespace
            line = line.strip()

            # Ignore any empty lines
            if line:
                # speak the non-empty line

                text = str(line)
                tts = gTTS(text, lang='en-US', slow=False, pre_processor_funcs=[pre_processors.abbreviations, pre_processors.end_of_line])
                # Save the audio in an mp3 file
                filename = 'good.mp3'
                tts.save(filename)

                # Play the audio
                pygame.mixer.init()
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()

                # Wait for the audio to be played
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

                # Clean up resources
                pygame.mixer.music.stop()
                pygame.mixer.quit()

except Exception as e:
    print(f"An error occurred: {e}")
