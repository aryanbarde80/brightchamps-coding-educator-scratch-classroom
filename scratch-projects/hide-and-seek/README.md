# Hide And Seek

## Project Summary

The player searches for a hidden sprite. When clicked, the sprite moves to a new random position and the score increases.

## Concepts Covered

- Mouse click events
- Random positions
- Score variable
- Timer
- Broadcast messages
- Game loop

## Sprites

| Sprite | Role |
| --- | --- |
| Hidden Character | Target to find |
| Background | Play area |
| Timer Display | Time pressure |

## Scratch Logic

```text
when green flag clicked
set Score to 0
set Timer to 30
go to random position
show

when this sprite clicked
change Score by 1
go to random position

when green flag clicked
repeat until Timer = 0
  wait 1 second
  change Timer by -1
end
say "Game Over"
stop all
```

## Teaching Notes

Use this project to show how a game can react to mouse clicks and randomize positions.

## Extension Ideas

- Make the sprite smaller after each click.
- Add sound effects.
- Add a target score to win.

