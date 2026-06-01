# Fruit Catcher

## Project Summary

The player moves a basket left and right to catch falling fruits. Each caught fruit increases the score.

## Concepts Covered

- Green flag event
- Keyboard controls
- Forever loop
- Random position
- Score variable
- Collision detection

## Sprites

| Sprite | Role |
| --- | --- |
| Basket | Player-controlled catcher |
| Fruit | Falling object |
| Background | Game stage |

## Variables

| Variable | Purpose |
| --- | --- |
| Score | Counts caught fruits |
| Speed | Controls fruit falling speed |

## Scratch Logic

### Basket

```text
when green flag clicked
go to x: 0 y: -140
forever
  if right arrow key pressed then change x by 10
  if left arrow key pressed then change x by -10
end
```

### Fruit

```text
when green flag clicked
set Score to 0
set Speed to 5
forever
  go to x: pick random -220 to 220 y: 170
  repeat until touching Basket or y position < -170
    change y by -Speed
  end
  if touching Basket then change Score by 1
end
```

## Teaching Notes

Ask the student:

- Why do we need a score variable?
- What happens if speed is increased?
- Why do we use random x position?

## Extension Ideas

- Add a timer.
- Add bad fruits that reduce score.
- Increase speed after every 5 points.

