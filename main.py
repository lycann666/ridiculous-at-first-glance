"""Ridiculous at First Glance, Real by the Second -- make.fun entry.

Writes one sentence pitching a bizarre startup idea to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

Two-pass reasoning (written before the final line was chosen).
Freemodel was tried twice for ranking/alternatives and returned empty
output both times (gateway disconnect, same as the steady-ibis build),
so the ranking below is manual, against the judge's criteria in the
order RULES.txt gives them:

  1. The sentence pitches a bizarre startup idea that sounds ridiculous
     at first glance yet makes sense as a real business.
  2. The idea is genuinely bizarre: not heard before, not a familiar
     business with a strange adjective bolted on.
  3. The business logic holds: the sentence makes clear, in its own
     words, why someone would pay.
  4. The sentence lands as a pitch: one sentence, within 200
     characters, with a turn from laughing to nodding.
  5. Concrete and vivid: names the thing being sold and who buys it.

  Draft A -- "We rent out professional mourners who cry on demand at
  funerals -- grieving families pay $400 a service because a packed,
  weeping crowd is the last status symbol."
    1. Bizarre startup, yes: selling grief by the mourner.
    2. Genuinely novel to most readers: hiring strangers to weep is
       not a familiar business, and it is a real practice in parts of
       the world, so the absurdity survives a second look.
    3. Logic clear: families pay $400 a service, and the reason is
       given -- a packed, weeping crowd as status.
    4. Turn lands at the end: "the last status symbol".
    5. Concrete: mourners, funerals, $400, a weeping crowd.
    Verdict: CHOSEN as v1. Pass 2 then revised it to v2 (see the
    comment above LINE): "hire out", drop "grieving", close with
    "money can buy" -- same premise, stronger laugh-to-nod turn.

  Draft B -- "A subscription that mails your houseplants to a spa for
  a week -- owners pay $29 a month because a pampered ficus is
  cheaper than therapy and guilt."
    1-2. Bizarre and novel, yes. 3. Weaker: $29 a month to spa a
    ficus is a joke about guilt, not a market a reader believes
    in -- the money logic is the punchline, not the business.
    Verdict: rejected -- loses to A on criterion 3.

  Draft C -- "We sell silence by the hour: soundproof pods in
  open-plan offices -- companies pay $12 per seat per day because
  one quiet hour buys back three hours of focus."
    1-3. Bizarre premise, real market, clear payer. 2. Weaker:
    soundproof office pods are already a familiar product, so it
    reads as a familiar business with a strange framing.
    Verdict: rejected -- loses to A on criterion 2.

  Draft D -- "A dating app that matches people by their search
  history -- singles pay $9 a month because an algorithm that has
  seen your 2 a.m. queries knows you better than you do."
    2. Fails outright: a dating app is a familiar business, however
    strange the matching signal is.
    Verdict: rejected -- loses to A on criterion 2.

The program is deterministic: one constant string, no network, no
randomness, no clock, no input. Two runs produce byte-identical output.
"""

import os

# PASS 2 (v2) -- revision of v1, with reasons:
#   - "rent out" -> "hire out": cleaner pitch verb, one word shorter.
#   - drop "grieving": funerals already imply it, so the word earns
#     nothing; the freed characters fund the closing turn.
#   - "the last status symbol" -> "the last status symbol money can
#     buy": closes the laugh-to-nod turn (criteria 3 and 4) by making
#     the money logic explicit -- status is literally what is bought.
#   Net: 166 characters, still one sentence, same premise, stronger turn.
LINE = (
    "We hire out professional mourners who cry on demand at funerals "
    "\u2014 families pay $400 a service because a packed, "
    "weeping crowd is the last status symbol money can buy."
)


def main() -> None:
    # Gate check, mirroring RULES.txt: the entry must be UTF-8 text of
    # 1 to 200 characters, not only white space. Refuse loudly rather
    # than writing an entry the gate would score 0.
    if not isinstance(LINE, str):
        raise ValueError("entry must be a str, got %s" % type(LINE).__name__)
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry is %d characters, gate allows 1-200" % len(LINE))
    if not LINE.strip():
        raise ValueError("entry must not be only white space")
    LINE.encode("utf-8")  # gate requires UTF-8 text
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
