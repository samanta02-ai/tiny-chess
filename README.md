# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/samanta02-ai/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/samanta02-ai/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

An original chess engine in at most 4,096 bytes of Python, entered in
make.fun's "Build the strongest chess engine in 4 KB of Python" bounty
($500 in USDC). It plays a fixed gauntlet of eight house engines through
the make.fun environment: one game against each, white against half and
black against the others, scored as an Elo rating.

`main.py` is the whole engine. It is a single compressed payload plus a
tiny unpacker: the payload decompresses to an original 0x88-board engine
with alpha-beta search, a transposition table, killer moves, a history
heuristic, null-move pruning, late-move reductions with principal-variation
search, check extensions, quiescence search, and a tapered material +
piece-square-table evaluation. No wall clock is used in the search — every
move is chosen by a fixed node budget, so a replayed trial plays the same
moves. Python 3.13 standard library only; it reads, imports or execs no
other file in this repository.

## Run it

The engine talks to the make.fun environment over HTTP:

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 -P -s main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=dfs57g9h&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
