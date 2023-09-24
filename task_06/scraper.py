import requests
from bs4 import BeautifulSoup
import textwrap

def fetch_live_score():
    url = 'https://www.espncricinfo.com/live-cricket-score'

    print(url)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    specific_div = soup.find('div', class_='ds-flex ds-flex-col ds-mt-2 ds-mb-2')
    specific_paragraph = soup.find('p', class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')

    if specific_div and specific_paragraph:
        div_text = specific_div.get_text()
        paragraph_text = specific_paragraph.get_text()

        
        team_names = ['Sri Lanka', 'Bangladesh', 'New Zealand', 'Australia', 'West Indies'] 
        for team_name in team_names:
            div_text = div_text.replace(team_name, f'{team_name} ')

        
        words = div_text.split()
        for word in words:
            if word.istitle():
                div_text = div_text.replace(word, f'{word}\n')

        wrapper = textwrap.TextWrapper(width=80)

        div_lines = wrapper.wrap(div_text)
        paragraph_lines = wrapper.wrap(paragraph_text)

        formatted_div = '\n'.join(div_lines)
        formatted_paragraph = '\n'.join(paragraph_lines)

        result = f"\n{formatted_div}\n\n{formatted_paragraph}"
    else:
        if not specific_div:
            result = "No live scores available! Try again later"
        if not specific_paragraph:
            result = ""

    return result


print(fetch_live_score())
