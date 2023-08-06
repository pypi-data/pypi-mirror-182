import vk_api
from vk_api.longpoll import VkLongPoll
from vk_api.keyboard import VkKeyboardColor


class VkBot:

    """Parent VK bot class.
        Example init:
            class MyBot(VkBot):
                def __init__(self):
                    super().__init__()
    """

    def __init__(self, token):

        """Initializing all data"""

        self.token = token
        self.vk_session = vk_api.VkApi(token=self.token)
        self.longpoll = VkLongPoll(self.vk_session)
        self.keyboard_colors = [
            VkKeyboardColor.POSITIVE,
            VkKeyboardColor.NEGATIVE,
            VkKeyboardColor.PRIMARY,
            VkKeyboardColor.SECONDARY,
        ]

    def send_msg(self, id, text, keyboard=None):

        """This method send message to user.
            Example use:
                first_kb = VkKeyboard()
                first_kb.add_button("Button 1", self.keyboard_colors[0])
                self.send_msg(user_id, "Some text", first_keyboard)
                                or
                self.send_msg(user_id, "Some text")
        """

        if keyboard is not None:
            self.vk_session.method("messages.send", {
                "user_id": id,
                "message": text,
                "random_id": 0,
                "keyboard": keyboard.get_keyboard()
            })

        else:
            self.vk_session.method("messages.send", {
                "user_id": id,
                "message": text,
                "random_id": 0
            })

