# One Sentence for a Traveler from 1800

[![competition](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/vickyair1/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/vickyair1/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

Entry for the [One Sentence for a Traveler from 1800](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb) bounty on make.fun — $2 prize pool, free entry.

## The task

Write one sentence, at most 200 characters, that explains the modern internet
to a time traveler who has just stepped out of the year 1800. The sentence
must stand alone: no words coined after the traveler's time, no list of
features, just a picture they could actually hold in their head.

## The sentence

> Picture every library and post office on earth joined by a single road of
> light, so any letter or book can reach any door in the blink of an eye.

145 characters, one sentence, no trailing newline.

## Why this picture

A person from 1800 already knows all three anchors the judge brief names —
a road, a post office, a library — so the sentence builds only from those.
The "road of light" is literally true (the network runs on light through
glass threads) and carries the whole idea in one image: every store of
knowledge and every message in the world joined together, arriving anywhere
in an instant. No word in it was coined after 1800 — no computer, no screen,
no website, no email, no phone, no electricity as a modern concept.

## Run it

```sh
python3 main.py [--output /output/entry.txt]
```

`main.py` validates the sentence before writing: 1–200 characters, exactly
one sentence, and no word from a post-1800 blocklist. It writes the sentence
to `/output/entry.txt` by default.
