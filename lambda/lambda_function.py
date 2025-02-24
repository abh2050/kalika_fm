"""
 Copyright (C) 2025 pacemaker.ai - All Rights Reserved
 You may use, distribute and modify this code under the
 terms and conditions defined in file 'LICENSE.txt', which
 is part of this source code package.
 
 For additional copyright information please
 visit : http://pacemaker.ai/copyright
"""

import logging
import json
import random

from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler, AbstractRequestInterceptor, AbstractResponseInterceptor
)
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_model.interfaces.audioplayer import (
    PlayDirective, PlayBehavior, AudioItem, Stream, AudioItemMetadata,
    StopDirective, ClearQueueDirective, ClearBehavior
)

# Initializing the logger and setting the level to "INFO"
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

""" 
Instructions to modify the code to play the stream of your choice:

1. Replace the current URL with your stream URL. Make sure that it has a valid SSL certificate and starts with 'https' and not 'http'.
2. Replace the title under metadata with the name of your stream or radio. Alexa speaks out this name before the stream begins.
3. Replace the subtitle under metadata with your stream's tagline. It is displayed on screen-enabled devices while the skill is playing.
4. Replace the URL under metadata>art>sources with an album art image of your choice (512x512 pixels).
5. Replace the URL under metadata>backgroundImage>sources with a background image of your choice (1200x800 pixels).
"""

# Kalika FM Audio Stream Metadata
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

# Intent Handlers

class CheckAudioInterfaceHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        if handler_input.request_envelope.context.system.device:
            return handler_input.request_envelope.context.system.device.supported_interfaces.audio_player is None
        return False

    def handle(self, handler_input):
        return handler_input.response_builder.speak("Your device does not support audio streaming.").set_should_end_session(True).response

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        stream = STREAMS[0]
        return handler_input.response_builder.speak(f"Starting {stream['metadata']['title']}").add_directive(
            PlayDirective(
                play_behavior=PlayBehavior.REPLACE_ALL,
                audio_item=AudioItem(
                    stream=Stream(
                        token=stream["token"],
                        url=stream["url"],
                        offset_in_milliseconds=0,
                        expected_previous_token=None
                    ),
                    metadata=stream["metadata"]
                )
            )
        ).set_should_end_session(True).response

class ResumeStreamIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("PlaybackController.PlayCommandIssued")(handler_input) or is_intent_name("AMAZON.ResumeIntent")(handler_input)

    def handle(self, handler_input):
        stream = STREAMS[0]
        return handler_input.response_builder.add_directive(
            PlayDirective(
                play_behavior=PlayBehavior.REPLACE_ALL,
                audio_item=AudioItem(
                    stream=Stream(
                        token=stream["token"],
                        url=stream["url"],
                        offset_in_milliseconds=0,
                        expected_previous_token=None
                    ),
                    metadata=stream["metadata"]
                )
            )
        ).set_should_end_session(True).response

class CancelOrStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input) or is_intent_name("AMAZON.PauseIntent")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.add_directive(ClearQueueDirective(clear_behavior=ClearBehavior.CLEAR_ALL)).add_directive(StopDirective()).set_should_end_session(True).response

class PlaybackFailedIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("AudioPlayer.PlaybackFailed")(handler_input)

    def handle(self, handler_input):
        stream = STREAMS[0]
        return handler_input.response_builder.add_directive(
            PlayDirective(
                play_behavior=PlayBehavior.REPLACE_ALL,
                audio_item=AudioItem(
                    stream=Stream(
                        token=stream["token"],
                        url=stream["url"],
                        offset_in_milliseconds=0,
                        expected_previous_token=None
                    ),
                    metadata=stream["metadata"]
                )
            )
        ).set_should_end_session(True).response

class FallbackIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.speak("I'm sorry, I didn't understand that. Try saying 'open kalika f. m.'").response

class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response

class ExceptionEncounteredRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("System.ExceptionEncountered")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response

class RequestLogger(AbstractRequestInterceptor):
    def process(self, handler_input):
        logger.debug("Alexa Request: {}".format(handler_input.request_envelope.request))

class ResponseLogger(AbstractResponseInterceptor):
    def process(self, handler_input, response):
        logger.debug("Alexa Response: {}".format(response))

class CatchAllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)
        return handler_input.response_builder.speak("An error occurred. Please try again later.").response

# Skill Builder
sb = SkillBuilder()
sb.add_request_handler(CheckAudioInterfaceHandler())
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(ResumeStreamIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(PlaybackFailedIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

sb.add_global_request_interceptor(RequestLogger())
sb.add_global_response_interceptor(ResponseLogger())

lambda_handler = sb.lambda_handler()
