import streamlit as st
import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def display_articles(df, num, key_prefix, show_like_buttons=True):
    for index, row in df.iterrows():
        st.write(f"**{row['Title']}**")
        st.write(row['Summary'])
        st.write(f"[Read more]({row['Link']})")
        if show_like_buttons:
            button_key = f"{key_prefix}_like_button_{index}"
            if st.button(f'Like Article {index + 1}', key=button_key):
                liked_titles = [article['Title'] for article in st.session_state['liked_articles']]
                if row['Title'] in liked_titles:
                    st.warning('You have already liked this article.')
                else:
                    st.session_state['liked_articles'].append(row)
                    st.session_state['genre_list'].append(row['Label'])
                    st.experimental_rerun() #display the next set of articles

def max_genre(genre_list):
    if genre_list:
        return max(set(genre_list), key=genre_list.count)
    return None

def main():
    st.title('News Recommendation System')
    path = r'C:\Users\msaha\OneDrive\Desktop\news_crape\article2.csv'
    df = load_data(path)
    
    if 'liked_articles' not in st.session_state:
        st.session_state['liked_articles'] = []
    if 'genre_list' not in st.session_state:
        st.session_state['genre_list'] = []
    
    # Display the initial set of 5 articles 
    if 'displayed_articles' not in st.session_state:
        st.session_state['displayed_articles'] = df.sample(5)
    
    # Always display the same 5 articles
    display_articles(st.session_state['displayed_articles'], len(st.session_state['displayed_articles']), key_prefix="initial", show_like_buttons=True)

    # Determine the most liked genre and display additional articles
    frequent_genre = max_genre(st.session_state['genre_list'])
    
    if frequent_genre:
        st.header(f'Most Liked Genre: {frequent_genre}')
        
        # Display 1 article from the most liked genre and 1 random article
        genre_articles = df[df['Label'] == frequent_genre].sample(1)
        random_article = df.sample(1)
        new_articles = pd.concat([genre_articles, random_article])
        display_articles(new_articles, len(new_articles), key_prefix="recommended", show_like_buttons=True)
    
    st.write(f"List of liked genres: {st.session_state.get('genre_list', [])}")
    st.write(f"Number of liked articles: {len(st.session_state['liked_articles'])}")

if __name__ == '__main__':
    main()


