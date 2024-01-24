import requests
from bs4 import BeautifulSoup

def scrape_goodreads(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting information from the page
        title_element = soup.find('h1', {'class': 'Text Text__title1'})
        title = title_element.text.strip() if title_element else None

        # Extracting author names
        author_elements = soup.find('div', {'class': 'ContributorLinksList'})
        authors = author_elements.find('span', {'data-testid': 'name'}).text.strip() if author_elements else None

        author_img_element = soup.find('div', {'class': 'FeaturedPerson__avatar'})
        author_img_url = author_img_element.find('img')['src'] if author_img_element else None

        bookplot_element = soup.find('div', {'class': 'TruncatedContent'})
        bookplot = bookplot_element.text.strip() if bookplot_element else None

        genres_list = soup.find('div', {'data-testid': 'genresList'})
        genre_elements = genres_list.find_all('span', {'class': 'Button__labelItem'})
        genres = [genre.text.strip() for genre in genre_elements] if genre_elements else None

        book_details_element = soup.find('div', {'class': 'BookDetails'})
        pages_format = book_details_element.find('p', {'data-testid': 'pagesFormat'}).text.strip() if book_details_element else None
        publication_info = book_details_element.find('p', {'data-testid': 'publicationInfo'}).text.strip() if book_details_element else None

        cover_image_element = soup.find('img', {'class': 'ResponsiveImage'})
        cover_image_url = cover_image_element['src'] if cover_image_element else None

        rating_stats_element = soup.find('div', {'class': 'RatingStatistics__meta'})
        ratings_count = rating_stats_element.find('span', {'data-testid': 'ratingsCount'}).text.strip() if rating_stats_element else None
        reviews_count = rating_stats_element.find('span', {'data-testid': 'reviewsCount'}).text.strip() if rating_stats_element else None

        # Creating a dictionary to store the information
        book_details = {
            'title': title,
            'authors': authors,
            'author_img': author_img_url,
            'book_plot': bookplot,
            'book_image_cover': cover_image_url,
            'pages_format': pages_format,
            'publication_info': publication_info,
            'ratings_count': ratings_count,
            'reviews_count': reviews_count,
            'genres': genres
        }

        return book_details
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

