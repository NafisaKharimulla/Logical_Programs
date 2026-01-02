# Base class
class Messenger:
    def use_keyboard(self):
        print("Using keyboard")

    def send_message(self):
        print("Text message sent")

    def receive_message(self):
        print("Text message received")


# Child class 1
class WhatsApp(Messenger):
    def send_message(self):
        print("WhatsApp: Text, voice, and video message sent")

    def receive_message(self):
        print("WhatsApp: Text, voice, and video message received")


# Child class 2
class FacebookMessenger(Messenger):
    def send_message(self):
        print("Facebook Messenger: Text, voice, and video message sent")

    def receive_message(self):
        print("Facebook Messenger: Text, voice, and video message received")


# Child class 3
class InstaMessenger(Messenger):
    def send_message(self):
        print("Instagram Messenger: Text, voice, and video message sent")

    def receive_message(self):
        print("Instagram Messenger: Text, voice, and video message received")


# Polymorphic function
def use_messenger(ref):
    ref.use_keyboard()
    ref.send_message()
    ref.receive_message()


whatsapp = WhatsApp()
facebook = FacebookMessenger()
instagram = InstaMessenger()


print("--- WhatsApp ---")
use_messenger(whatsapp)

print("\n--- Facebook Messenger ---")
use_messenger(facebook)

print("\n--- Instagram Messenger ---")
use_messenger(instagram)
