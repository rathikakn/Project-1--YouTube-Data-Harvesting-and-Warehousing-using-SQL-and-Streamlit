
# YouTube Data Harvesting and Warehousing using SQL and Streamlit


This project aims to develop a user-friendly Streamlit application that utilizes the Google API to extract information on a YouTube channel, stores it in a SQL database, and enables users to search for channel details and join tables to view data in the Streamlit app.


## API Reference

#### Get all items for channels

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `part` | `string` | **Required**. contentDetails, snippet,statistics |

```http
  GET /api/items
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. id-YouTube channel ID. |


#### Get all items for videos

```http
  GET /api/items
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `part`      | `string` | **Required**. contentDetails,snippet,statistics |

```http
  GET /api/items
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id-video_id |

#### Get all items for commentThreads

```http
  GET /api/items
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `part`      | `string` | **Required**. snippet |

```http
  GET /api/items
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id - video_id |

```http
  GET /api/items
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `maxResults`      | `unsigned integer` | **Required**. 1-100 |

```http
  GET /api/items
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `pageToken`      | `string` | **Required**. nextPageToken |


## Lessons Learned

Python scripting, Data Collection, Streamlit, API integration, Data Management using SQL  


## Workflow

There are two files

1. ipynb file has the program for collecting data with the help of Google API of YouTube and inputing a YouTube channel ID to retrieve all the relevant data (Channel name, subscribers, description, total video count, total view count, playlist ID for each channel, video ID, video title, video description, publication date, thumblnails, views, likes, duration, caption and comments of each video, author name, comment text, published date for each comments).

2. .py file has the program for input a new channel ID to get details for additional channels and store them in the mysql and display in Streamlit application.


## Demo

https://www.linkedin.com/posts/rathika-kavitha-nagaraj-954b3219a_here-is-my-new-project-demo-video-in-python-activity-7188209368234917889-6MYE?utm_source=share&utm_medium=member_desktop

## Installation

Install my-project with pip

```bash
pip install mysql.connector
pip install pandas
pip install sqlalchemy
pip install streamlit


import googleapiclient.discovery
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import re
from googleapiclient.errors import HttpError
import streamlit as st

```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`- https://console.cloud.google.com/cloud-resource-manager it can be created using this link by creating a new project and enabling youtube v3

