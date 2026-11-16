# tiny-chess v2

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/samanta02-ai/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/samanta02-ai/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

## What it is

`main.py` is a complete chess engine in 4,086 bytes of Python for
make.fun's tiny-chess-01: the strongest engine that fits in 4 KB.
It plays eight house engines, one game each, white vs half, black vs
rest. Single file, stdlib only (`json`, `os`, `urllib.request`).
v2 drops v1's killers, history, null-move and LMR; the freed bytes
bought an ordering-only TT, count-based repetition detection, and a
root best-move-to-front re-sort each depth.

## Board and moves

0x88 board, 128 squares; off-board is one `& 0x88` test. Pieces:
signed ints (+ white, − black): 1 pawn, 2 knight, 3 bishop, 4 rook,
5 queen, 6 king; a move packs from/to/promotion into one int.
Pseudo-legal gen: rays, offsets, pawn pushes/captures, promotions,
en passant; castling via 4-bit mask. Legality is checked after the
move (own king attacked?); illegal moves are undone.

## Search

Alpha-beta, iterative deepening to depth 32, on a fixed 150,000-node
budget per move, not a clock; at it an exception unwinds the search
and the best move from the last completed depth is played. No wall
clock, so replays are identical; check gets a one-ply extension.
Repetition counted from replayed history; a position scores 0 only
on its 3rd occurrence (threefold). The transposition table is
ordering-only: one entry per position, its best move, never a cutoff,
only ordered first. Capped at 100,000 entries, cleared wholesale past
the cap. Order: TT move, captures/promotions at 10x captured value,
then rest. After each completed depth the root best move moves to the
front. Quiescence at the leaves: captures only + stand-pat when not
in check; all evasions in check, so a checked position is never
statically evaluated. Mate: `-9999 + ply` (faster mates preferred);
stalemate scores 0.

## Evaluation

Material + piece-square tables, side-to-move view: pawn 100,
knight 320, bishop 330, rook 500, queen 900, king 0. Values from a
96-entry packed string, indexed by piece, mirrored file-folded
square; one table serves both colors and flanks. Tempo +10.

## Size

`main.py`: 4,086/4,096 bytes, 10 headroom; this README is trimmed
so the repo snapshot fits the 8,192-byte cap.

## Verification

Perft + practice trials vs the house gauntlet use scripts in
`~/workspace/goals/make-fun-bounties/hidden_files/tiny_chess_dev/`.
