# Automation for [*The Farmer Was Replaced*](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/)

Automates the drone via a state machine. The state machine is designed
using a pattern learned from Rob Pike's [talk on lexical scanning in
Go](https://www.youtube.com/watch?v=HxaD_trXwRE), i.e. each state
returns the next state to execute. This turned out to be a really
neat way of separating out behaviours.

The maze solver could probably be simplified and optimized more.

Dinosaurs TBD when unlocked :-)

