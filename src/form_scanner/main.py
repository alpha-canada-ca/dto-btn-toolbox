import requests
from bs4 import BeautifulSoup
import json
import csv
from tqdm import tqdm

def scrape_url( url ):
    comments = ''
    form_title = None  # Initialize form_title
    try:
        response = requests.get( url )

        if response.status_code == 404:
            comments = '404 Not Found'
            return { 'url': url, 'comments': comments }

        response.raise_for_status()
        soup = BeautifulSoup( response.content, 'html.parser' )

        # Retrieve the h1 of the page
        page_title = soup.find( 'h1#wb-cont' ).text.strip() if soup.find( 'h1#wb-cont' ) else None

        # Find the form and check for a heading preceding the form
        form = soup.find( 'main form' )
        if form:
            preceding_heading = form.find_previous_sibling( [ 'h2', 'h3', 'h4', 'h5', 'h6' ] )
            if preceding_heading:
                form_title = preceding_heading.text.strip()
            elif form.find( 'legend' ):
                form_title = form.find( 'legend' ).text.strip()

        # Scrape the institution name
        meta_tags = [ 'author', 'dcterms.creator', 'dcterms.identifier' ]
        institution_name = None
        for tag in meta_tags:
            meta_tag = soup.find( 'meta', attrs={ 'name': tag } )
            if meta_tag and meta_tag.get( 'content' ):
                institution_name = meta_tag[ 'content' ].strip()
                break

        # Scrape the alternate language URL
        alternate_language_url = soup.select_one( '#wb-lng a' )[ 'href' ] if soup.select_one( '#wb-lng a' ) else None

        return {
            'url': url,
            'page_title': page_title,
            'form_title': form_title,
            'institution_name': institution_name,
            'alternate_language_url': alternate_language_url,
            'comments': comments
        }
    except requests.exceptions.HTTPError as e:
        comments = f'HTTP error: { str( e ) }'
    except Exception as e:
        comments = f'Error: { str( e ) }'

    return { 'url': url, 'comments': comments }

# Read URLs from file
with open( 'forms.txt', 'r' ) as file:
    urls = [ line.strip( ) for line in file ]

# Process each URL with a progress bar
results = [ scrape_url( url ) for url in tqdm( urls, desc="Processing URLs" ) ]

# Write results to a JSON file
json_file = 'scraped_data.json'
with open( json_file, 'w', encoding='utf-8' ) as file:
    json.dump( results, file, indent=4 )

# Write results to a CSV file
csv_file = 'scraped_data.csv'
headers = [ 'url', 'page_title', 'form_title', 'institution_name', 'alternate_language_url', 'comments' ]  # Adjust headers as needed

with open( csv_file, 'w', newline='', encoding='utf-8' ) as file:
    writer = csv.DictWriter( file, fieldnames=headers )
    writer.writeheader()
    for result in results:
        writer.writerow( result )
