class Messenger:
    def use_keyboard(self):
        print("Using keyboard")

    def send_message(self):
        print("Text message sent")

    def receive_message(self):
        print("Text message received")



class WhatsApp(Messenger):
    def send_message(self):
        print("Text, video, and audio message sent using WhatsApp")

    def receive_message(self):
        print("Text, video, and audio message received using WhatsApp")

    def send_live_location(self):
        print("Live location sent using WhatsApp")



class FacebookMessenger(Messenger):
    def send_message(self):
        print("Text, video, and audio message sent using Facebook Messenger")

    def receive_message(self):
        print("Text, video, and audio message received using Facebook Messenger")

    def use_builtin_apps(self):
        print("Using built-in apps in Facebook Messenger")



class InstaMessenger(Messenger):
    def send_message(self):
        print("Text, video, and audio message sent using Instagram")

    def receive_message(self):
        print("Text, video, and audio message received using Instagram")

    def add_filters(self):
        print("Applying filters using Instagram")



def use_messenger(ref):
    ref.use_keyboard()
    ref.send_message()
    ref.receive_message()

    
    if isinstance(ref, WhatsApp):
        ref.send_live_location()
    elif isinstance(ref, FacebookMessenger):
        ref.use_builtin_apps()
    elif isinstance(ref, InstaMessenger):
        ref.add_filters()



wa = WhatsApp()
fb = FacebookMessenger()
insta = InstaMessenger()

print("--- WhatsApp ---")
use_messenger(wa)

print("\n--- Facebook Messenger ---")
use_messenger(fb)

print("\n--- Instagram Messenger ---")
use_messenger(insta)
