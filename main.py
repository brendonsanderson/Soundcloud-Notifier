import soundcloud
import time

# create a client object with your app credentials
client = soundcloud.Client(client_id=YOUR_CLIENT_ID)

# create a list of SoundCloud user IDs for the accounts you want to track
user_ids = [USER_ID_1, USER_ID_2, USER_ID_3]

# create a Discord client
discord_client = discord.Client()

# create a function that will be called when a new track is uploaded by one of the tracked accounts
def on_track_upload(track):
  # get the user who uploaded the track
  user = client.get('/users/{}'.format(track.user_id))

  # create a link to the track on SoundCloud
  track_link = 'https://soundcloud.com/{}/{}'.format(user.username, track.permalink)
  
  # send a message to the Discord channel
  discord_client.send_message(DISCORD_CHANNEL_ID, '{} just uploaded a new track: {}'.format(user.username, track_link))

# start listening for new tracks from the tracked accounts
while True:
  for user_id in user_ids:
    client.listen('/users/{}/tracks'.format(user_id), on_track_upload)
    
  # sleep for one hour
  time.sleep(3600)
