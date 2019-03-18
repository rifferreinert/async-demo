import asyncio
import time


class AsyncRateLimit:
    def __init__(self, tokens, time_period):
        self.tokens_per_period = tokens
        self.tokens = tokens
        self.time_period = time_period
        self.next_update = time.time() + time_period

    async def limit(self):
        if self.tokens > 0:
            self.tokens -= 1
            return
        now = time.time()
        if now < self.next_update:
            await asyncio.sleep(self.next_update - now)
            return await self.limit()
        self.tokens = self.tokens_per_period
        self.next_update = now + self.time_period
        return await self.limit()
