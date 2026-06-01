# Maze Game

## Project Summary

The player controls a character and tries to reach the goal without touching the maze walls.

## Concepts Covered

- Coordinates
- Keyboard input
- If conditions
- Touching color detection
- Reset logic
- Level progression

## Sprites

| Sprite | Role |
| --- | --- |
| Player | Moves through the maze |
| Goal | End point |
| Maze Background | Wall layout |

## Scratch Logic

```text
when green flag clicked
go to start position
forever
  if right arrow pressed then change x by 4
  if left arrow pressed then change x by -4
  if up arrow pressed then change y by 4
  if down arrow pressed then change y by -4

  if touching wall color then
    go to start position
  end

  if touching Goal then
    say "You Win!"
    stop all
  end
end
```

## Teaching Notes

Explain that games constantly check rules. The player moves, then the program checks if the player touched a wall or reached the goal.

## Extension Ideas

- Add multiple levels.
- Add a timer.
- Add moving enemies.

