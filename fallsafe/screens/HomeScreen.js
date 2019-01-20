import React from 'react';
import {
  Image,
  Platform,
  ScrollView,
  StyleSheet,
  Text,
  Linking,
  TouchableOpacity,
  View,
  Button,
  YellowBox,
  ActivityIndicator
} from 'react-native';

import _ from 'lodash';
import * as firebase from 'firebase'
import {
  Video,
  Permissions,
  Notifications
} from 'expo'

const loadingVideo = require('./giphy.mp4')
// Initialize Firebase
const firebaseConfig = {
apiKey : "AIzaSyB4S-rsmyGvtZxXI8Q6ThhvqcRmlFGz_Ks",
  authDomain : "fallsafe.firebaseio.com/",
  databaseURL: "https://fallsafe.firebaseio.com/",
  storageBucket: "gs://fallsafe.appspot.com/"
};

firebase.initializeApp(firebaseConfig);
const database = firebase.database();

const storage = firebase.storage();
var storageRef = storage.ref();

const video = storageRef.child('video/video.mp4');

YellowBox.ignoreWarnings(['Setting a timer']);
const _console = _.clone(console);
console.warn = message => {
  if (message.indexOf('Setting a timer') <= -1) {
    _console.warn(message);
  }
};


export default class HomeScreen extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      notificiation: '',
      videoUrl: ''
    }
    console.ignoredYellowBox = [
      'Setting a timer'
    ];

  }

  downloadVideo = async () => {
    const url = await video.getDownloadURL()
    this.setState({
      videoUrl: url
    })
  }

  componentDidMount() {
    this.registerForPushNotifications()      
    this._notificationSubscription = Notifications.addListener(this._handleNotification);    
    this.downloadVideo()        
  }
  
  _handleNotification = (notification) => {
    this.downloadVideo()
    this.setState({ 
      notification,
      videoUrl: ''
     });
  };

  registerForPushNotifications = async () => {
    const {status} = await Permissions.getAsync(Permissions.NOTIFICATIONS)
    let finalStatus = status
    console.log(status);
    
    if (status !== 'granted') {
      const { status } = await Permissions.askAsync(Permissions.NOTIFICATIONS)
      finalStatus = status 
    }

    // if (finalStatus !== 'granted') {
    //   return
    // }


    let token = await Notifications.getExpoPushTokenAsync()

    // add token to firebase
    database.ref('user').child('iphone').update({
      expoPushToken: token
    })        
  }

  buttonClick = () => {
    console.log('clicked button');
    Linking.openURL('tel:+46705872161')
  }

  playHaha = async () => {
    const soundObject = new Expo.Audio.Sound();
    console.log('HAHA SEND');
    
    try {
      await soundObject.loadAsync(require('./haha2.mp3'));
      await soundObject.playAsync();
      // Your sound is playing!
    } catch (error) {
      // An error occurred!
    }
  }

  render() {    
    
    return (
      <View style={styles.container}>
        <Text style={styles.header}>Alfred has just fallen</Text>        
        <View
          style={styles.videoBackground}
        >
        {this.state.videoUrl.length === 0 ? 
            <View style={styles.spinner}>
              <ActivityIndicator
                size="small" color="#6ACDBC" />
            </View>
            :
            <Video
              source={{ uri: this.state.videoUrl }}
              rate={1.0}
              volume={1.0}
              isMuted={false}
              resizeMode="cover"
              shouldPlay
              isLooping
              style={{height: 240, width: 320}}
            />
          }
        </View>
        <TouchableOpacity 
          onPress={this.buttonClick}          
          style={styles.buttonCall}
        >
          <Text style={styles.buttonCallText}>
            Call Alfred
          </Text>
        </TouchableOpacity>                  
        <TouchableOpacity 
          onPress={this.playHaha}          
          style={{...styles.buttonCall, ...styles.buttonEmergency}} 
        >                  
        <Text style={{...styles.buttonCallText, color: 'white'}}>
          Notify emergency services
        </Text>
        </TouchableOpacity>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#6ACDBC',    
    justifyContent: 'space-around',
    alignItems: 'center'
  },
  header: {
    color: 'white',
    textAlign: 'center',
    fontSize: 35,
    fontWeight: 'bold'
  },
  spinner: {
    // postion: 'absolute',    
  },
  videoBackground: {
    backgroundColor: 'white',
    padding: 10,
    borderRadius: 10,
    // width: 320,
    // height: 240,
  },
  buttonCall: {
    backgroundColor: 'white',
    borderRadius: 10,
    width: 320,
    padding: 10,    
  },
  buttonCallText: {
    color: '#6ACDBC', 
    textAlign: 'center',
    fontSize: 35,
    fontWeight: 'bold',
    
  },
  buttonEmergency: {
    backgroundColor: '#D48080',
    height: 150,
    justifyContent: 'center'    
  },
  
});
