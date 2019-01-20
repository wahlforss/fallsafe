# https://exp.host/--/api/v2/push/send
import requests
#pip install python-firebase

def notify():
    from firebase import firebase

    firebase = firebase.FirebaseApplication(
        'https://fallsafe.firebaseio.com/', None)
    result = firebase.get('/user', None)
    expo_token = result['iphone']['expoPushToken']
    print('inside notify', expo_token)
    r = requests.post("https://exp.host/--/api/v2/push/send",                
                    json={
                        'to': expo_token,
                        'title': 'Alfred has fallen',
                        'body': 'Watch the video',
                        'data': {
                            'videoUrl': 'https://media.giphy.com/media/wZfBc9Ct5yJvG/giphy.mp4'
                        }
                    })
    return r
