#!/usr/bin/python3

import httplib2
import os
import sys
import time
import json

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets, AccessTokenCredentials
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

def create_playlist(playlist):
#if __name__ == '__main__':

	now = time.strftime('%Y년 %m월 %d일 %H시 %M분 %S초의 플레이리스트입니다.', time.localtime(time.time()))

	CLIENT_SECRETS_FILE = "client_secret_889441568964-7edmll9mihlcle8k0rok3og1to9c9dfd.apps.googleusercontent.com.json" # youtube account of shulphur31@gmail.com

	# This variable defines a message to display if the CLIENT_SECRETS_FILE is
	# missing.
	MISSING_CLIENT_SECRETS_MESSAGE = """
	WARNING: Please configure OAuth 2.0

	To make this sample run you will need to populate the client_secrets.json file
	found at:

	   %s

	with information from the API Console
	https://console.developers.google.com/

	For more information about the client_secrets.json file format, please visit:
	https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
	""" % os.path.abspath(os.path.join(os.path.dirname(__file__), CLIENT_SECRETS_FILE))

	# This OAuth 2.0 access scope allows for full read/write access to the
	# authenticated user's account.
	YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
	YOUTUBE_API_SERVICE_NAME = "youtube"
	YOUTUBE_API_VERSION = "v3"

	flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, message=MISSING_CLIENT_SECRETS_MESSAGE, scope=YOUTUBE_READ_WRITE_SCOPE)

	storage = Storage("%s-oauth2.json" % sys.argv[0])
	credentials = storage.get()

	if credentials is None or credentials.invalid:
		flags = argparser.parse_args()
		credentials = run_flow(flow, storage, flags)

	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, http=credentials.authorize(httplib2.Http()))


	# This code creates a new, public playlist in the authorized user's channel.
	playlists_insert_response = youtube.playlists().insert(
		part="snippet,status",
		body=dict(
			snippet=dict(
				#title="Test Playlist9",
				title= now,
				description="A public playlist created with the YouTube API v3"
			),
			status=dict(
				privacyStatus="public"
			)
		)
	).execute()


	playlistID=playlists_insert_response["id"]
	#playlist = ['WMweEpGlu_U', '4TWR90KJl84', 'HzOjwL7IP_o', '8GPAW4dMxsY', 'odY9BGCxG98'] # for test

	# This code add a new video in the authorized user's channel's playlist
	for i in range(5):
		videoID = str(playlist[i])
		#videoID = playlist[i]
		add_video_request=youtube.playlistItems().insert(
			part="snippet",
			body={
				'snippet': {
					'playlistId': playlistID,
					'resourceId': {
						'kind': 'youtube#video',
						'videoId': videoID
						}
					}
				}
		).execute()

	print("New playlist id: %s" % playlistID)
	content="playlistID = '[{"+"playlistID"+":"+playlistID+"}]';"
	with open('./static/playlistID.json', 'w', encoding='utf-8') as f:
		json.dump(content, f)
