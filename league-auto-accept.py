import pyautogui
import time
from datetime import datetime
from threading import Thread
from queue import Queue
import asyncio
import os
import DiscordBot


class Accept(Thread):

    def __init__(self, queue):
        super(Accept, self).__init__()
        self.queue = queue

    def run(self):
        while True:

            accept = pyautogui.locateCenterOnScreen('accept.png', confidence=0.4)

            if accept:
                pyautogui.moveTo(accept)
                # click multiple times just to make sure accept button gets clicked

                print(f'Match found. {datetime.now()}')

                self.queue.put("MATCH")
                time.sleep(1)
                action = self.queue.get()

                if action == "ACCEPT":
                    pyautogui.click(accept)
                elif action == "DECLINE":
                    decline = pyautogui.locateCenterOnScreen('decline.png', confidence=0.4)
                    pyautogui.moveTo(decline)
                    pyautogui.click(decline)

                time.sleep(10)
            else:
                print(datetime.now())
                time.sleep(1)


if __name__ == '__main__':

    queue = Queue()

    asyncio.get_child_watcher()
    loop = asyncio.get_event_loop()
    loop.create_task(DiscordBot.start(queue, os.getenv('TOKEN'), 365243942771490829))
    bot = Thread(target=DiscordBot.run_it_forever, args=(loop,))

    bot.start()
    auto_accept = Accept(queue).start()
