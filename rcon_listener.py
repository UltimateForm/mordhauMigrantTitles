import asyncio
from reactivex import Subject, operators
from rcon import RconClient


class RconListener(Subject[str], RconClient):
    _event: str
    _port: int
    _password: str
    _address: str

    _listening: bool

    def __init__(self, event: str = "chat", listening: bool = False) -> None:
        self._event = event
        self._listening = listening
        Subject.__init__(self)
        RconClient.__init__(self)

    async def warmer(self):
        while True:
            await asyncio.sleep(100)
            try:
                print("Rewarming...")
                await self.rewarm()
            except Exception as e:
                print(f"FAILED TO REWARM! ERROR: {str(e)}")

    async def start(self):
        await self.authenticate()
        if not self._listening:
            r = await self.execute(f"listen {self._event}")
            print(r)
            self._listening = True
        asyncio.create_task(self.warmer())
        while True:
            pck = await self.recv_pkt()
            self.on_next(pck.body)


if __name__ == "__main__":
    login_listener = RconListener(event="login", listening=False)
    login_listener.pipe(operators.filter(lambda x: x.startswith("Login:"))).subscribe(
        on_next=lambda x: print(f"LOGIN: {x}")
    )

    chat_listener = RconListener(event="chat", listening=True)
    chat_listener.pipe(operators.filter(lambda x: x.startswith("Chat:"))).subscribe(
        on_next=lambda x: print(f"CHAT: {x}")
    )

    async def main():
        await asyncio.gather(chat_listener.start(), login_listener.start())

    asyncio.run(main())
