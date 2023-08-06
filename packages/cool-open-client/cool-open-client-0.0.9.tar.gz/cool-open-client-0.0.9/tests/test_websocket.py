import unittest
from time import sleep
import asyncio
from cool_open_client.cool_automation_client import CoolAutomationClient



class TestWebSocket(unittest.TestCase):
    def setUp(self):
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYxZjhkYmFlYThhMzFjMTk2NmIxZWNlYyIsImlhdCI6MTY0OTc2MDQxNiwiZXhwIjoxNjgxMzE4MDE2fQ.RLwz3qiZgLBRwHYpPQGrYtPC3t34axQBh2C7pP_wdVU"
        self.loop = asyncio.get_event_loop()

    def test_websocket(self):
        client = self.loop.run_until_complete(CoolAutomationClient.create(self.token))
        client.open_socket()
        # sleep(60)
        # self.loop.run_until_complete(task)


if __name__ == "__main__":
    unittest.main()
