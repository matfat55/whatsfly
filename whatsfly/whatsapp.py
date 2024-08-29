import os
import time
import uuid
from typing import Callable

from .whatsmeow import (
    new_whatsapp_client_wrapper,
    connect_wrapper,
    disconnect_wrapper,
    message_thread_wrapper,
    send_message_protobuf_wrapper,
    send_image_wrapper,
    send_video_wrapper,
    send_audio_wrapper,
    send_document_wrapper,
    get_group_invite_link_wrapper,
    join_group_with_invite_link_wrapper,
    set_group_announce_wrapper,
    set_group_locked_wrapper,
    set_group_name_wrapper,
    set_group_topic_wrapper,
    get_group_info_wrapper
)
from .proto.waE2E import WAWebProtobufsE2E_pb2
import ctypes
import json
import threading
import warnings
import functools
import qrcode

def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)  # reset filter
        return func(*args, **kwargs)
    return new_func


class WhatsApp:
    """
    The main whatsapp handler
    """

    def __init__(
        self,
        phone_number: str = "",
        media_path: str = "",
        machine: str = "mac",
        browser: str = "safari",
        on_event: Callable[[dict], None] =None,
        on_disconnect: Callable[[None], None]=None,
        print_qr_code: bool=True
    ):
        """
        Import the compiled whatsmeow golang package, and setup basic client and database.
        Auto run based on any database (login and chat info database), hence a user phone number are declared.
        If there is no user login assigned yet, assign a new client.
        Put the database in current file whereever this class instances are imported. database/client.db
        :param phone_number: User phone number. in the Whatsmeow golang are called client.
        :param media_path: A directory to save all the media received
        :param machine: OS login info (showed on the whatsapp app)
        :param browser: Browser login info (showed on the whatsapp app)
        :param on_event: Function to call on event
        :param on_disconnect: Function to call on disconnect
        :param print_qr_code: Setting to true will print the qr code to terminal on connection
        """

        self.user_name = None
        self.machine = machine
        self.browser = browser
        self.wapi_functions = browser
        self.connected = None
        self._messageThreadRunner = threading.Thread(target=self._messageThread)
        self._userEventHandlers = [on_event]
        self._methodReturns = {}
        self.print_qr_code = print_qr_code

        if media_path:
            if not os.path.exists(media_path):
                os.makedirs(media_path)
            for subdir in ["images", "audios", "videos", "documents", "stickers"]:
                full_media_path = media_path + "/" + subdir
                if not os.path.exists(full_media_path):
                    os.makedirs(full_media_path)


        CMPFUNC_NONE_STR = ctypes.CFUNCTYPE(None, ctypes.c_char_p)
        CMPFUNC_NONE = ctypes.CFUNCTYPE(None)

        self.C_ON_EVENT = (
            CMPFUNC_NONE_STR(self._handleMessage)
            if callable(on_event)
            else ctypes.cast(None, CMPFUNC_NONE_STR)
        )
        self.C_ON_DISCONNECT = (
            CMPFUNC_NONE(on_disconnect)
            if callable(on_disconnect)
            else ctypes.cast(None, CMPFUNC_NONE)
        )

        self.c_WhatsAppClientId = new_whatsapp_client_wrapper(
            phone_number.encode(),
            media_path.encode(),
            self.C_ON_DISCONNECT,
            self.C_ON_EVENT,
        )

        self._messageThreadRunner.start()

    def connect(self):
        """
        Connects the whatsapp client to whatsapp servers. This method SHOULD be called before any other.
        """
        connect_wrapper(self.c_WhatsAppClientId)

    def disconnect(self):
        """
        Disconnects the whatsapp client to whatsapp servers.
        """
        disconnect_wrapper(self.c_WhatsAppClientId)

    @deprecated
    def runMessageThread(self):
        """
        Legacy method that used to run the message thread, does nothing anymore
        """
        print("This method does nothing anymore, it has been automatised")

    def _messageThread(self):
        """
        New method for runMessageThread
        """
        while True:
            message_thread_wrapper(self.c_WhatsAppClientId)

    def _handleMessage(self, message):
        try:
            message = message.decode()
        except:
            print(message)
            pass
        try:
            message = json.loads(message)
        except:
            print(message)
            pass

        match message["eventType"]:
            case "linkCode":
                if self.print_qr_code:
                    print(message["code"])
            case "qrCode":
                if self.print_qr_code:
                    print(message["code"])
                    qr = qrcode.QRCode()
                    qr.add_data(message["code"])
                    qr.print_ascii()
            case "methodReturn":
                self._methodReturns[message["callid"]] = message
                return


        for handler in self._userEventHandlers:
            handler(message)

    def sendMessage(self, phone: str, message, group: bool = False):
        """
        Sends a text message
        :param phone: The phone number or group number to send the message.
        :param message: The message to send. It can be a string with the message, or a protobuf message
        :param group: Is the message sent to a group ?
        """
        if type(message) == str:
            message1 = WAWebProtobufsE2E_pb2.Message()
            message1.conversation = message
            message = message1

        ret = send_message_protobuf_wrapper(
            self.c_WhatsAppClientId, phone.encode(), message.SerializeToString(), group
        )
        return ret == 0

    def sendImage(
        self, phone: str, image_path: str, caption: str = "", group: bool = False
    ):
        """
        Sends an image message
        :param phone: The phone number or group number to send the message.
        :param image_path: The path to the image to send
        :param caption: The caption for the image
        :param group: Is the message sent to a group ?
        """
        ret = send_image_wrapper(
            self.c_WhatsAppClientId,
            phone.encode(),
            image_path.encode(),
            caption.encode(),
            group,
        )
        return ret == 1

    def sendVideo(
        self, phone: str, video_path: str, caption: str = "", group: bool = False
    ):
        """
        Sends a video message
        :param phone: The phone number or group number to send the message.
        :param video_path: The path to the video to send
        :param caption: The caption for the video
        :param group: Is the message sent to a group ?
        """
        ret = send_video_wrapper(
            self.c_WhatsAppClientId,
            phone.encode(),
            video_path.encode(),
            caption.encode(),
            group,
        )
        return ret == 1

    def sendAudio(self, phone: str, audio_path: str, group: bool = False):
        raise NotImplementedError
        return send_audio_wrapper(
            self.c_WhatsAppClientId, phone.encode(), audio_path.encode(), group
        )

    def sendDocument(
        self, phone: str, document_path: str, caption: str, group: bool = False
    ):
        """
        Sends a document message
        :param phone: The phone number or group number to send the message.
        :param document_path: The path to the document to send
        :param caption: The caption for the document
        :param group: Is the message sent to a group ?
        """
        return send_document_wrapper(
            self.c_WhatsAppClientId,
            phone.encode(),
            document_path.encode(),
            caption.encode(),
            group,
        )

    def getGroupInviteLink(
            self, group: str, reset: bool = False
    ) -> str:
        """
        Get invite link for group.
        Also sends an event to queue for legacy clients
        :param group: Group id
        :param reset: If true, resets the old link before generating the new one
        :return: Invite link
        """
        return_uuid = uuid.uuid1()

        error = get_group_invite_link_wrapper(
            self.c_WhatsAppClientId,
            group.encode(),
            reset,
            str(return_uuid).encode()
        )

        while not str(return_uuid) in self._methodReturns:
            time.sleep(0.001)

        response = self._methodReturns[str(return_uuid)]["return"]

        return response

    def joinGroupWithInviteLink(self, code: str):
        """
        Joins a group with an invite link
        :param code: The link
        """
        return join_group_with_invite_link_wrapper(
            self.c_WhatsAppClientId,
            code.encode(),
        )

    def setGroupAnnounce(self, group: str, announce: bool = True):
        """
        Set a group's announce mode (only admins can send message)
        :param group: Group id
        :param announce: Enable or not the announcement mode
        """
        return set_group_announce_wrapper(
            self.c_WhatsAppClientId,
            group.encode(),
            announce
        )

    def setGroupLocked(self, group: str, locked: bool = True):
        """
            Set a group's lock mode (only admins can change settings)
            :param group: Group id
            :param locked: Enable or not the lock mode
        """
        return set_group_locked_wrapper(
            self.c_WhatsAppClientId,
            group.encode(),
            locked
        )

    def setGroupName(self, group:str, name:str):
        """
            Set a group's name
            :param group: Group id
            :param name: Name
        """
        return set_group_name_wrapper(
            self.c_WhatsAppClientId,
            group.encode(),
            name.encode()
        )

    def setGroupTopic(self, group:str, topic:str):
        """
        Set a group's topic
        :param group: Group id
        :param topic: Topic
        """
        return set_group_topic_wrapper(
            self.c_WhatsAppClientId,
            group.encode(),
            topic.encode()
        )

    def getGroupInfo(
            self, group: str
    ) -> dict:
        """
        Get info for a link
        :param group: Group id
        :return: Group information
        """
        return_uuid = uuid.uuid1()

        error = get_group_info_wrapper(
            self.c_WhatsAppClientId,
            group.encode(),
            str(return_uuid).encode()
        )

        while not str(return_uuid) in self._methodReturns:
            time.sleep(0.001)

        response = self._methodReturns[str(return_uuid)]["return"]

        return response





if __name__ == "__main__":
    client = WhatsApp()
    message = "Hello World!"
    phone = "6283139000000"
    client.sendMessage(message=message, phone=phone)
