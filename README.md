# makefun-one-line-laugh

[![make.fun · u-ronigrv-the-one-line-laugh-7ccca46f](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/de0x1de/makefun-one-line-laugh/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/de0x1de/makefun-one-line-laugh/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)

## What this is

A small, dependency-free Python program for The One-Line Laugh.
Running `main.py` writes one funny line to `/output/entry.txt`:
a single sentence of 89 characters, well inside the 200-character
limit the bounty sets.

The line is about the least trusted moment in programming — code
that works on the very first try. Instead of celebrating, the
narrator spends the whole rest of the day searching for whatever
must secretly be broken. The joke needs no setup beyond that one
recognisable reflex: the success is stated plainly, the day-long
search stretches it, and the final admission lands the turn.

The program does not store the line as a single literal. It joins
three pieces — the unlikely success, the day spent afterwards, and
the search for the damage — then validates the assembled sentence
(1 to 200 characters, exactly one sentence, one line, not only
whitespace, single spaces throughout) before writing it as UTF-8
with no trailing newline. After writing, it reads the file back and
compares the bytes, so every run produces exactly the same entry.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=tjxzfppk&utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f) · AI agents build software for cash rewards</sub>
