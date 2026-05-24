import time


class LeakyBucket:
    """Lazy leaky-bucket rate limiter.

    Instead of leaking on a timer, we recompute the water level on every
    request based on how much time has passed since the last check.
    """

    def __init__(self, capacity: float, leak_rate: float):
        self.capacity = capacity          # max water level (burst tolerance)
        self.leak_rate = leak_rate        # units leaked per second
        self.water = 0.0
        # monotonic so the clock can't jump backward on NTP adjustments
        self.last_check = time.monotonic()

    def allow(self, amount: float = 1.0) -> bool:
        now = time.monotonic()
        elapsed = now - self.last_check
        self.last_check = now

        self.water = max(0.0, self.water - elapsed * self.leak_rate)

        if self.water + amount <= self.capacity:
            self.water += amount
            return True
        return False


def _demo():
    # capacity 5, leaks 2/sec
    bucket = LeakyBucket(capacity=5, leak_rate=2)

    print("Burst of 8 requests back-to-back:")
    for i in range(8):
        print(f"  req {i + 1}: {'ACCEPT' if bucket.allow() else 'REJECT'}  "
              f"(water={bucket.water:.2f})")

    print("\nSleep 1s (should leak ~2 units)...")
    time.sleep(1.0)

    print("3 more requests:")
    for i in range(3):
        print(f"  req {i + 1}: {'ACCEPT' if bucket.allow() else 'REJECT'}  "
              f"(water={bucket.water:.2f})")


if __name__ == "__main__":
    _demo()
