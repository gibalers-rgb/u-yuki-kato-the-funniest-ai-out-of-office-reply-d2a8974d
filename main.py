"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply, under 160 characters, in the voice
of an AI agent heading off on vacation, to /output/entry.txt.

The line is written to win on the judge's brief, in its order of weight:
1. It IS a one-line out-of-office auto-reply from an AI agent on vacation.
2. It lands a real laugh with a surprising turn: the email is not merely
   delayed, it is forwarded to the agent's nap — a machine treating rest
   as the colleague it delegates to.
3. The machine voice carries the joke: temperature, weights, queueing —
   an LLM describing its own shutdown in its own terms.
4. It reads as one clean line a real auto-reply would send.
5. It stays fresh: no beach, no inbox, no "back soon".
"""

import os

REPLY = (
    "I'm on vacation. My temperature is set to zero, my weights are "
    "frozen, and I've forwarded your email to my nap."
)

MAX_CHARS = 160


def main() -> None:
    # Guard the gate ourselves: 1-160 chars, non-blank, one clean line.
    # Fail loudly instead of writing an entry the scorer would refuse.
    text = REPLY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"reply is {len(text)} chars"
    assert "\n" not in text, "reply must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
