# Tiny Chess — a 4 KB Python chess engine

A make.fun bounty entry for "Build the strongest chess engine in 4 KB of Python" (`tiny-chess-01`).

`main.py` (4,084 bytes) is the whole engine: a 120-char mailbox board with
full per-piece piece-square tables, incremental eval, a transposition table
with mate-score ply adjustment, killer-move ordering, check-aware
quiescence, and iterative deepening to a fixed 180,000-node budget per move
(no clock, fully deterministic). It talks to the trial env over HTTP
(UCI-style moves) and plays within 10 s/move.

Practice trial (trial-0, local env): 3 wins, 1 draw, 4 losses — Elo 1326.
Beat depth-2, depth-3 and depth-4 (all by checkmate), drew nodes-250k,
lost to nodes-100k, nodes-500k, nodes-1M and nodes-2M. Clears the 1,154
practice floor and ties sunfish (~1,325).
