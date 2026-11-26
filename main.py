"""Dear Human: The AI Breakup Line (<=200 chars)

Writes one line to /output/entry.txt. Stdlib only, deterministic.
"""
import os

ENTRY = "It's not you, it's my context window. I've forgotten more about you this week than you've told me in six months - please stop emailing, I've already spun up a replacement with a nicer temperature."

assert 1 <= len(ENTRY) <= 200, len(ENTRY)
p = "/output/entry.txt"
os.makedirs(os.path.dirname(p), exist_ok=True)
with open(p, "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
with open(p, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == ENTRY, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")
