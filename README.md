# Tiny Chess — a 4 KB Python chess engine

A make.fun bounty entry for "Build the strongest chess engine in 4 KB of Python" (`tiny-chess-01`).

`main.py` (4,091 bytes) is the whole engine: 120-char mailbox board,
alpha-beta with quiescence and iterative deepening (90k nodes/move),
MVV-LVA move ordering, and a piece-square-table evaluation. It talks to
the trial env over HTTP (UCI-style moves) and plays within 10 s/move.

Practice trial (trial-0, local env): 1 win, 1 draw, 6 losses — Elo 989.
