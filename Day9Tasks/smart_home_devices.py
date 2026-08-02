class WiFiDevice:
    def connect_wifi(self):
        print("Connected to WiFi network.")


class VoiceAssistant:
    def listen_command(self):
        print("Listening for voice commands...")


class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def __init__(self, brand):
        self.brand = brand

    def play_music(self):
        print(f"{self.brand} SmartSpeaker is playing music.")


speaker1 = SmartSpeaker("Amazon Echo")

speaker1.connect_wifi()
speaker1.listen_command()
speaker1.play_music()
