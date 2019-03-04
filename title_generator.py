import markovify

from api_accessor import get_controversial_posts
from clean_data import read_file


def generate_titles(training_data, num_titles=5):
    model = markovify.Text(training_data)
    titles = list(model.make_sentence() for i in range(num_titles))
    return titles


def get_data_reddit(subreddit):
    posts = get_controversial_posts(subreddit)
    controversial_titles = list(post['title'] for post in posts if post is not None)
    return controversial_titles


def get_data_file(filename):
    content = read_file(filename)
    return content


if __name__ == '__main__':
    file_location = 'data\\bee_movie_script.txt'
    trump_speeches = get_data_file(file_location)
    trump_sentences = generate_titles(trump_speeches, 15)
    generated_speech = ' '.join(trump_sentences)
    print(generated_speech)
