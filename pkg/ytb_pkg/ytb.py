#!/usr/bin/python3

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

def youtube_search(options):
#if __name__ == "__main__":
	DEVELOPER_KEY = "AIzaSyD3CI1hwqpQUfvY1Qjw8KFQgiZcLMllK_Y"
	YOUTUBE_API_SERVICE_NAME = "youtube"
	YOUTUBE_API_VERSION = "v3"

	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

#	단독 실행시 파라미터 대신
#	options = "Butter"

# query term.
	search_response = youtube.search().list(
			q=options,
			part="id,snippet",
			maxResults=1
			).execute()
	video_id = []

# Add each result to the appropriate list, and then display the lists of
# matching videos, channels, and playlists.
	for search_result in search_response.get("items", []):
		if search_result["id"]["kind"] == "youtube#video":
			video_id.append("%s" % (search_result["id"]["videoId"]))

	print (video_id[0])

	return video_id[0]
