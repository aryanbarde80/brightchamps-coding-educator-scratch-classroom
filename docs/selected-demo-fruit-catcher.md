# Selected Demo: Fruit Catcher Scratch Class

## Why This Is The Main Selection

Fruit Catcher is the recommended primary demo because it is simple, visual, interactive, and easy to teach in a 30-minute mock interview. It does not compromise the selection because it stays inside the exact project list provided in the BrightChamps document.

## 30-Minute Class Plan

| Time | Segment | What To Do |
| --- | --- | --- |
| 0-3 min | Greeting and objective | Explain that the class will build a fruit catching game |
| 3-6 min | Show final game | Demonstrate basket movement, falling fruit, and score |
| 6-10 min | Sprites and stage | Explain basket, fruit, backdrop, and coordinates |
| 10-15 min | Basket controls | Teach keyboard events and x-axis movement |
| 15-21 min | Fruit falling logic | Teach loops, random x position, and y movement |
| 21-25 min | Score logic | Teach touching/collision and score variable |
| 25-28 min | Student interaction | Ask what happens if speed changes or fruit misses basket |
| 28-30 min | Recap | Review events, loops, variables, conditions, and collision |

## Teacher Opening Script

Hello everyone. Today we are going to create a Fruit Catcher game in Scratch. By the end of the class, you will know how to control a sprite, make another sprite move automatically, detect touching, and increase the score.

## Learning Objectives

- Understand the green flag event.
- Move a sprite using arrow keys.
- Use a forever loop for continuous game behavior.
- Use a score variable.
- Use random positions to make the game interesting.
- Detect when the fruit touches the basket.

## Final Game Behavior

The basket stays near the bottom of the screen. Fruits fall from random positions at the top. The player uses left and right arrow keys to catch fruits. When a fruit touches the basket, the score increases by 1 and a new fruit appears.

## Full Scratch Build Steps

### Step 1: Create Sprites

Use these sprites:

- Basket
- Apple or any fruit
- Optional backdrop such as park, sky, or plain color

### Step 2: Create Variables

Create:

- `Score`
- `Speed`

### Step 3: Basket Code

```text
when green flag clicked
go to x: 0 y: -140
forever
  if key right arrow pressed then
    change x by 10
  end
  if key left arrow pressed then
    change x by -10
  end
end
```

Explain:

- The green flag starts the game.
- The forever loop keeps checking the keyboard.
- Changing x moves left and right.

### Step 4: Fruit Code

```text
when green flag clicked
set Score to 0
set Speed to 5
forever
  go to x: pick random -220 to 220 y: 170
  repeat until touching Basket or y position < -170
    change y by Speed * -1
  end
  if touching Basket then
    change Score by 1
  end
end
```

Explain:

- Random x position makes the fruit fall from different places.
- The repeat-until block keeps fruit falling until it touches the basket or reaches the bottom.
- Score changes only when the basket catches the fruit.

## Student Engagement Questions

- What will happen if we increase speed from 5 to 10?
- Why should the fruit start at a random x position?
- Which direction is x movement?
- Which direction is y movement?
- What condition should increase the score?

## Expected Interview Explanation

This project teaches beginner programming concepts through a game. The basket uses keyboard input, the fruit uses a loop and random positions, and the score uses a variable. The most important logic is collision detection: when the fruit touches the basket, the score increases.

## Backup Modifications

If the interviewer asks for improvement ideas:

- Add a timer.
- Add a lives variable.
- Add a bad fruit that reduces score.
- Increase speed after every 5 points.
- Add sound when fruit is caught.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| Basket does not move | Check if keyboard blocks are inside forever loop |
| Fruit does not fall | Check y position change is negative |
| Score does not increase | Check touching condition uses Basket sprite |
| Fruit starts outside screen | Keep random x between -220 and 220 |
| Game feels too fast | Reduce Speed variable |

