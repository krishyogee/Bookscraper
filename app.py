from flask import Flask, render_template, request
from scraper import scrape_goodreads

app = Flask(__name__)


@app.route('/')
def index_search():
    return render_template('index-search.html')

@app.route('/result', methods=['POST'])
def index_result():
    if request.method == 'POST':
        url = request.form['url']
        book_info = scrape_goodreads(url)
        return render_template('index-result.html', book_info=book_info)

if __name__ == '__main__':
    app.run(debug=True)








