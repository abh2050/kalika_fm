# Kalika FM Alexa Skill
![](https://cache.usercontentapp.com/logo/mjpg/7552.jpg?format=png&enlarge=0&quality=90&width=960)

An Alexa skill that streams **Kalika FM**, a live radio station from Bharatpur, Chitwan, Nepal.
https://www.amazon.in/dp/B0DYF9CPTM/

## 🎯 Quick Start

To launch the skill, simply say:

> **"Alexa, open Kalika F. M."**

## 🌟 Features

- **Live streaming** of Kalika FM
- **Multi-language support** (US, GB, IN, CA, AU)
- **Playback controls** (play, pause, resume, stop)
- **Screen display support** for Alexa devices with screens

## 🎙️ Voice Commands

| Command | Action |
|---------|--------|
| **"Alexa, open Kalika F. M."** | Starts playing Kalika FM |
| **"Alexa, play Kalika F. M."** | Starts playing Kalika FM |
| **"Alexa, start Kalika F. M."** | Starts playing Kalika FM |
| **"Alexa, stop"** | Stops playback |
| **"Alexa, pause"** | Pauses playback |
| **"Alexa, resume"** | Resumes playback |

## 🌍 Supported Regions

- **United States** (en-US)
- **United Kingdom** (en-GB)
- **India** (en-IN)
- **Canada** (en-CA)
- **Australia** (en-AU)

---

## 🛠️ Technical Details

| Component | Technology Used |
|-----------|----------------|
| **Programming Language** | Python 3.7+ |
| **Framework** | ASK SDK for Python |
| **Backend** | AWS Lambda |
| **Speech Recognition** | Alexa Voice Service |
| **Audio Playback** | Alexa **AudioPlayer Interface** |
| **Deployment** | AWS Lambda, ASK CLI |

---

## 📡 Stream Information

The skill streams **Kalika FM** from its official online source.

- **Streaming URL:** `https://streaming.softnep.net:10828/;stream.nsv&type=mp3&volume=70`
- **Audio Format:** MP3
- **Bitrate:** Adaptive based on network speed

---

## 🏗️ Project Structure

```plaintext
├── lambda/                      # AWS Lambda function directory
│   ├── lambda_function.py       # Main Alexa skill handler
│   └── languages/               # Multi-language support files
│       ├── en-US.json
│       ├── en-GB.json
│       ├── en-IN.json
│       ├── en-CA.json
│       ├── en-AU.json
│       └── en.json
├── interactionModels/           # Alexa skill interaction models
│   └── custom/
│       ├── en-US.json
│       ├── en-GB.json
│       ├── en-IN.json
│       ├── en-CA.json
│       └── en-AU.json
└── skill.json                   # Alexa skill configuration file
```

---

## 🚀 Deployment Guide

### **1. AWS Lambda Setup**
- Create a new AWS Lambda function
- Use **Python 3.7+** runtime
- Add the **ASK SDK layer** or include dependencies manually
- Set the **handler** to:  
  ```plaintext
  lambda_function.lambda_handler
  ```

### **2. Alexa Skill Setup**
- Create a new skill in **Alexa Developer Console**
- Set **invocation name** as **"Kalika F. M."**
- Import the **interaction models** from `interactionModels/custom/`
- Configure endpoints with your **Lambda ARN**

### **3. Image Assets**
- **512x512** skill icon
- **1200x800** background image
- Update image URLs in **lambda_function.py**

---

## 📢 Kalika FM Audio Stream Metadata

```json
STREAMS = [
    {
        "token": "kalika_fm_token",
        "url": "https://streaming.softnep.net:10828/;stream.nsv&type=mp3&volume=70",
        "metadata": {
            "title": "Kalika FM",
            "subtitle": "Bharatpur-10, Chitwan, Nepal",
            "art": {
                "sources": [
                    {
                        "contentDescription": "Kalika FM Logo",
                        "url": "https://example.com/path/to/kalika_fm_logo_512x512.jpg",
                        "widthPixels": 512,
                        "heightPixels": 512
                    }
                ]
            },
            "backgroundImage": {
                "sources": [
                    {
                        "contentDescription": "Kalika FM Background",
                        "url": "https://example.com/path/to/kalika_fm_background_1200x800.jpg",
                        "widthPixels": 1200,
                        "heightPixels": 800
                    }
                ]
            }
        }
    }
]
```

---

## 🔑 Endpoint Configuration

The Alexa Skill is configured to support **multiple regions**, ensuring a smooth experience worldwide.

```json
"apis": {
  "custom": {
    "endpoint": {
      "uri": "arn:aws:lambda:us-east-1:XXXXXXXXXXXXXX:function:YYYYYYYYYYYYYYY"
    },
    "interfaces": [
      {
        "type": "AUDIO_PLAYER"
      }
    ],
    "regions": {
      "NA": {
        "endpoint": {
          "uri": "arn:aws:lambda:us-east-1:XXXXXXXXXXXXXX:function:YYYYYYYYYYYYYYY"
        }
      },
      "EU": {
        "endpoint": {
          "uri": "arn:aws:lambda:eu-west-1:XXXXXXXXXXXXXX:function:YYYYYYYYYYYYYYY"
        }
      },
      "FE": {
        "endpoint": {
          "uri": "arn:aws:lambda:us-west-2:XXXXXXXXXXXXXX:function:YYYYYYYYYYYYYYY"
        }
      }
    }
  }
}
```

---

## 📜 License

**© 2025 pacemaker.ai - All Rights Reserved**

---

## 🏁 Support

For additional information or support:

- **Website:** [Kalika FM](http://kalikafm.com.np)
- **Privacy Policy:** [Privacy Policy](http://kalikafm.com.np/privacy-policy)
- **Terms of Use:** [Terms of Use](http://kalikafm.com.np/terms-of-use)

---

**Made with ❤️ for Nepali radio listeners worldwide!** 🎵🇳🇵
