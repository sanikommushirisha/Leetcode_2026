import time


class TokenBucket:
    """Lazy token-bucket rate limiter.

    Bucket starts full and refills at a steady rate up to capacity. Each
    request consumes tokens; if not enough are available, it's rejected.
    Refill is computed on demand instead of on a timer.
    """

    def __init__(self, capacity: float, refill_rate: float):
        self.capacity = capacity          # max tokens (also the burst size)
        self.refill_rate = refill_rate    # tokens added per second
        self.tokens = float(capacity)     # start full
        self.last_check = time.monotonic()

    def allow(self, cost: float = 1.0) -> bool:
        now = time.monotonic()
        elapsed = now - self.last_check
        self.last_check = now

        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)

        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False


def _demo():
    # capacity 5, refills 2/sec
    bucket = TokenBucket(capacity=5, refill_rate=2)

    print("Burst of 8 requests back-to-back (bucket starts full):")
    for i in range(8):
        print(f"  req {i + 1}: {'ACCEPT' if bucket.allow() else 'REJECT'}  "
              f"(tokens={bucket.tokens:.2f})")

    print("\nSleep 1s (should refill ~2 tokens)...")
    time.sleep(1.0)

    print("3 more requests:")
    for i in range(3):
        print(f"  req {i + 1}: {'ACCEPT' if bucket.allow() else 'REJECT'}  "
              f"(tokens={bucket.tokens:.2f})")


if __name__ == "__main__":
    _demo()
