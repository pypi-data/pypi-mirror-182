import time
import random
from vk_api.longpoll import VkEventType
from vk_api.keyboard import VkKeyboard
from vk_api_rucod import VkBot


class VkSpamer(VkBot):
    def __init__(self, token):

        """Initializing all data"""

        super().__init__(token)
        # Letters for spam
        self.spam_letters = "qwertyuiopasdfghjklzxcvbnm"

    def run(self):

        """This method run app"""

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
                                start_kb.add_button("Старт", self.keyboard_colors[0])
                                self.send_msg(id, f"👋Здравствуй, {name}", keyboard=start_kb)

                            if msg == "старт":
                                # Warning
                                self.send_msg(id,
                                              "Внимание! Сейчас вам придет 1000 сообщений. Отменить это действие нельзя!")
                                time.sleep(2)

                                # Spam
                                for i in range(1000):
                                    spam = random.choices(self.spam_letters, k=random.randint(1, 10))
                                    self.send_msg(id, "".join(spam))

            except:
                print("Error")
                continue
