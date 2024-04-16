import streamlit as st
import mysql.connector
import pandas as pd


def fetch_data(query):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="youtube")
    df = pd.read_sql(query, mydb)
    mydb.close()
    return df


def execute_query(question):
    query_mapping = {
        "What are the names of all the videos and their corresponding channels?": """
            SELECT videos.Video_title, channels.channel_name
            FROM videos
            JOIN channels ON videos.channel_id = channels.channel_id;
        """,
        "Which channels have the most number of videos, and how many videos do they have?": """
            SELECT channel_name, COUNT(*) AS video_count
            FROM videos
            JOIN channels ON videos.channel_id = channels.channel_id
            GROUP BY channel_name
            ORDER BY video_count DESC;
        """,
        "What are the top 10 most viewed videos and their respective channels?": """
            SELECT videos.Video_title, channels.channel_name
            FROM videos
            JOIN channels ON videos.channel_id = channels.channel_id
            ORDER BY videos.Video_viewcount DESC
            LIMIT 10;
        """,
        "How many comments were made on each video, and what are their corresponding video names?": """
            SELECT videos.Video_title, COUNT(*) AS comment_count
            FROM videos
            JOIN comments ON videos.Video_Id = comments.video_id
            GROUP BY videos.Video_title;
        """,
        "Which videos have the highest number of likes, and what are their corresponding channel names?": """
            SELECT videos.Video_title, channels.channel_name
            FROM videos
            JOIN channels ON videos.channel_id = channels.channel_id
            ORDER BY videos.Video_likecount DESC
            LIMIT 1;
        """,
        "What is the total number of likes for each video, and what are their corresponding video names?": """
            SELECT videos.Video_title, SUM(videos.Video_likecount) AS total_likes
            FROM videos
            GROUP BY videos.Video_title;
        """,
        "What is the total number of views for each channel, and what are their corresponding channel names?": """
            SELECT channels.channel_name, SUM(videos.Video_viewcount) AS total_views
            FROM videos
            JOIN channels ON videos.channel_id = channels.channel_id
            GROUP BY channels.channel_name;
        """,
        "What are the names of all the channels that have published videos in the year 2022?": """
            SELECT DISTINCT channels.channel_name
            FROM channels
            JOIN videos ON channels.channel_id = videos.channel_id
            WHERE YEAR(videos.Video_pubdate) = 2022;
        """,
        "What is the average duration of all videos in each channel, and what are their corresponding channel names?": """
            SELECT channels.channel_name, AVG(videos.Video_duration) AS average_duration
            FROM videos
            JOIN channels ON videos.channel_id = channels.channel_id
            GROUP BY channels.channel_name;
        """,
        "Which videos have the highest number of comments, and what are their corresponding channel names?": """
            SELECT videos.Video_title, channels.channel_name
            FROM videos
            JOIN channels ON videos.channel_id = channels.channel_id
            ORDER BY videos.Video_commentcount DESC
            LIMIT 1;
        """
    }

    query = query_mapping.get(question)
    if query:
        return fetch_data(query)
    else:
        return pd.DataFrame()


def main():
    st.title("YouTube Data Harvesting and Warehousing using SQL and Streamlit")
    st.sidebar.header("Tables")

    selected_option = st.sidebar.radio("Select Option", ("Channels", "Videos", "Comments", "Queries"))

    if selected_option == "Channels":
        st.header("Channels")
        channels_df = fetch_data("SELECT * FROM channels;")
        channels_df.index+=1
        st.dataframe(channels_df)

    elif selected_option == "Videos":
        st.header("Videos")
        videos_df = fetch_data("SELECT * FROM videos;")
        videos_df.index+=1
        st.dataframe(videos_df)

    elif selected_option == "Comments":
        st.header("Comments")
        comments_df = fetch_data("SELECT * FROM comments;")
        comments_df.index+=1
        st.dataframe(comments_df)

    elif selected_option == "Queries":
        st.header("Queries")
        query_question = st.selectbox("Select Query", [
            "What are the names of all the videos and their corresponding channels?",
            "Which channels have the most number of videos, and how many videos do they have?",
            "What are the top 10 most viewed videos and their respective channels?",
            "How many comments were made on each video, and what are their corresponding video names?",
            "Which videos have the highest number of likes, and what are their corresponding channel names?",
            "What is the total number of likes for each video, and what are their corresponding video names?",
            "What is the total number of views for each channel, and what are their corresponding channel names?",
            "What are the names of all the channels that have published videos in the year 2022?",
            "What is the average duration of all videos in each channel, and what are their corresponding channel names?",
            "Which videos have the highest number of comments, and what are their corresponding channel names?"
        ])
        if query_question:
            query_result_df = execute_query(query_question)
            query_result_df.index+=1   
            st.dataframe(query_result_df)


if __name__ == "__main__":
    main()
