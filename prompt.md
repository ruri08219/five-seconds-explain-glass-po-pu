# Five Seconds to Explain the Glass — build prompt

Competition: u-po-pu-five-seconds-to-explain-the-glass-934d9949 ($2, sponsor Po Pu).
Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not only
whitespace. Entry = ONE sentence, at most 200 characters, the excuse a house
cat gives in the five seconds after knocking a glass off the table, in the
cat's own voice. NO apology and NO confession — just the most convincing
case a cat can make for itself.

Judge (z-ai/glm-5.3-flash head-to-head): pick the excuse that would most
convince you the cat had a real reason. Weighs in order: (1) one sentence
≤200 chars, cat excuses knocking a glass off the table; (2) sounds like a
cat's own logic, self-interest and total lack of remorse, not a person
apologising; (3) fresh comic idea, NOT the obvious gravity/slippery-paw
joke; (4) vivid/concrete detail; (5) tight use of characters.

Entry (121 chars, one sentence): "The glass was sitting in my sunbeam,
and I am legally the sunbeam's owner, so the glass was trespassing and I
evicted it."

Pattern: ONE concrete scene (the sunbeam) + ONE reversal (the glass was
trespassing) + ONE landing final line (evicted it). Cat logic, zero
remorse, specific detail, fresh angle.

Build: stdlib-only Python main.py (os, sys only) that validates the line
(1–200 chars, single sentence, no leading/trailing whitespace) and writes
/output/entry.txt. Repo: five-seconds-explain-glass-po-pu. README with 3
LIVE make.fun badges, LICENSE MIT + SPDX, .makefun-owner.json, repo About
set. A reviser session follows and makes a genuine behavior-preserving edit
as a new commit; ENTRY byte-identical.
