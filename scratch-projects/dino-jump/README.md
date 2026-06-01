# Dino Jump

## Project Summary

The player controls a dinosaur that jumps over incoming obstacles.

## Concepts Covered

- Events
- Gravity
- Variables
- Collision detection
- Loops
- Game over logic

## Sprites

| Sprite | Role |
| --- | --- |
| Dino | Player character |
| Cactus | Obstacle |
| Ground | Visual base |

## Variables

| Variable | Purpose |
| --- | --- |
| VelocityY | Controls jump movement |
| Score | Tracks survival score |

## Scratch Logic

```text
when green flag clicked
set Score to 0
set VelocityY to 0
go to x: -120 y: -100
forever
  if space key pressed and touching ground then
    set VelocityY to 15
  end
  change y by VelocityY
  change VelocityY by -1
  if touching ground then set y to ground level
  if touching Cactus then stop all
end
```

## Teaching Notes

This is a great project for explaining real-world simulation. Gravity pulls the dino down, and jump force pushes it up.

## Extension Ideas

- Make obstacles faster over time.
- Add clouds and background movement.
- Add high score.

