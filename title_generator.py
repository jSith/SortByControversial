import markovify
import pickle

from api_accessor import get_controversial_posts
from clean_data import read_file


def generate_titles(training_data=None, title=None, num_titles=5):
    if training_data and title:
        model = create_model(training_data)
        save_model(model, title)
    elif title:
        model = load_model(title)
    else:
        raise ValueError("One of training data or model location expected")

    titles = list(model.make_sentence() for i in range(num_titles))
    return titles


def create_model(training_data):
    model = markovify.Text(training_data)
    return model


def save_model(model, title):
    model_location = f'data\\{title}.sav'
    with open(model_location, 'wb') as rw_file:
        pickle.dump(model, rw_file)


def load_model(title):
    model_location = f'data\\{title}.sav'
    try:
        with open(model_location, 'wb') as rw_file:
            return pickle.load(rw_file)
    except FileNotFoundError:
        return None


def get_data_reddit(subreddit):
    posts = get_controversial_posts(subreddit)
    controversial_titles = list(post['title'] for post in posts if post is not None)
    return controversial_titles


def get_data_file(filename):
    content = read_file(filename)
    return content


if __name__ == '__main__':
    file_location = 'data\\bee_movie_script.txt'
    trump_speeches = get_controversial_posts(subreddit="politics")
    trump_sentences = generate_titles(training_data=trump_speeches, title="r/politics_model")
    generated_speech = ' '.join(trump_sentences)
    print(generated_speech)
