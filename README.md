# Tiny Chess — a 4 KB Python chess engine

A make.fun bounty entry for "Build the strongest chess engine in 4 KB of Python" (`tiny-chess-01`).

`main.py` (4,033 bytes) is the whole engine: a 120-char mailbox board with
full per-piece piece-square tables, incremental eval, a transposition table
with mate-score ply adjustment, killer-move ordering, check-aware
quiescence, and iterative deepening to a fixed 100,000-node budget per move
(no clock, fully deterministic). It talks to the trial env over HTTP
(UCI-style moves) and plays within 10 s/move.

v3 (this version): the v2 engine used a 180,000-node budget and its local
trial-0 took 1,635 s of the 1,800 s wall; on the slower grading container
it blew past the wall and scored 0 on every column. v3 keeps the v2 search
identical and only lowers the fixed budget to 100,000 nodes/move.
100,000 was picked as the largest budget that keeps the local trial under
~1,300 s, leaving ~500 s of headroom to the wall (the grading container
runs ~1.1-1.2x slower than local, so v3 grades at roughly 1,440-1,570 s);
a 120,000 budget would land near 1,500 s locally and risk the wall, so it
was not used for the last submission slot.

Practice trial (trial-0, local env): 3 wins, 1 draw, 4 losses — Elo 1326,
in 1,308 s total wall time. Beat depth-2, depth-3 and nodes-500k (all by
checkmate), drew nodes-1M, lost to depth-4, nodes-100k, nodes-250k and
nodes-2M. Clears the 1,154 practice floor and ties sunfish (~1,325).

Submission: round 3, the last of the 3 slots, deadline 2026-11-24T17:00:00Z.
Verification: perft passes (all 12 checks OK) and the random-game
eval/move check reports 0 mismatches; the packed engine is deterministic
(no wall clock in the search), so final replays are byte-identical.
