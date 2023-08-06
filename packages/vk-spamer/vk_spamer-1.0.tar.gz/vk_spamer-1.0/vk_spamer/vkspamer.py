import time
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class VkSpamer:
    def __init__(self, main_token):
        self.main_token = main_token
        self.vk_session = vk_api.VkApi(token=self.main_token)
        self.longpoll = VkLongPoll(self.vk_session)
        self.colors = [
            VkKeyboardColor.POSITIVE,
            VkKeyboardColor.NEGATIVE,
            VkKeyboardColor.PRIMARY,
            VkKeyboardColor.SECONDARY,
        ]
        self.spam_letters = "qwertyuiopasdfghjklzxcvbnm"

    def send_text(self, id, text, kb=None):

        """This method send text to user"""

        if kb is not None:
            self.vk_session.method("messages.send", {
                "user_id": id,
                "message": text,
                "random_id": 0,
                "keyboard": kb.get_keyboard()
            })

        else:
            self.vk_session.method("messages.send", {
                "user_id": id,
                "message": text,
                "random_id": 0
            })

    def run(self):
        while True:
            try:
                for event in self.longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW:
                        if event.to_me:

                            # User message
                            msg = event.text.lower()

                            # User id
                            id = event.user_id

                            # User data
                            user = self.vk_session.method("users.get", {"user_ids": id})
                            name = user[0]['first_name']

                            if msg == "начать" or msg == "привет" or msg == "здравствуйте" or msg == "меню":
                                start_kb = VkKeyboard()
                                start_kb.add_button("Старт", self.colors[0])
                                self.send_text(id, f"👋Здравствуй, {name}", kb=start_kb)

                            if msg == "старт":
                                self.send_text(id,
                                               "Внимание! Сейчас вам придет 1000 сообщений. Отменить это действие нельзя!")
                                time.sleep(2)

                                # Spam
                                for i in range(1000):
                                    spam = random.choices(self.spam_letters, k=random.randint(1, 10))
                                    self.send_text(id, "".join(spam))

            except:
                print("Error")
                continue
