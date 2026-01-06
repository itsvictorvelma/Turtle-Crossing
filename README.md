# Turtle Crossing Game 🐢

Small Frogger-Style Game Built With **Python Turtle**  
This Is A Learning Project Meant To Show Progress, Not A Polished Release

---

## Demo 🎥
Apologies for the shitty quality and lagging, your smart fridge is more powerful than my pc :)

https://github.com/user-attachments/assets/0623acb6-c339-4d84-8e69-ad666d020c54


## About

A Simple Arcade Game Where The Player Moves A Turtle Vertically Across The Screen While Avoiding Cars  
Each Successful Crossing Increases The Level And Speeds The Game Up  
Collision Ends The Run

The Focus Here Was Structure And Logic, Not Visuals Or Polish

---

## What I Was Practicing

- Splitting Code Into Multiple Files  
- Separating Responsibilities Between Classes  
- Building A Real Game Loop With `ontimer`  
- Handling Continuous Input With Key State  
- Basic Collision Detection  
- Difficulty Scaling Per Level  
- Working Within Turtle’s Event-Driven System  

---

## Project Structure

```
├── main.py # Game Setup, Input, And Loop
├── player.py # Player Movement And Bounds
├── car_manager.py # Car Spawning, Movement, And Speed Scaling
├── scoreboard.py # Level Display And Game Over Text
└── input_state.py # Tracks Held Keyboard Input
```

---

## Controls 🎮

- Up Arrow   Move Up  
- Down Arrow Move Down  

Movement Is Continuous While The Key Is Held

---

## Design Notes

- Fixed Screen Size (600x600) For Predictable Math  
- Window Resizing Disabled To Avoid Collision Drift  
- Manual Rendering Using `tracer(0)` And `screen.update()`  
- Random Car Spawns To Prevent Predictable Patterns  
- Colors Chosen For Visibility On A Dark Background  

---

## Known Limitations

- Cars Are Never Removed After Leaving The Screen  
- Collision Is Distance-Based, Not Pixel-Perfect  

These Are Accepted Tradeoffs For Learning Speed And Clarity

---

## Why This Exists

This Project Exists To Document Progress From Beginner Scripts Toward Structured Programs  
The Focus Was On State Ownership, Timing, And Control Flow  
Not On Overengineering Or Premature Polish

This Lives Alongside Other Small Projects Tracking My Learning Curve

---

## Requirements

- Python 3  
- Standard Library Only  
- Turtle Module  

No External Dependencies

---

## How To Run ▶️
```
python main.py
```
or 
```
python3 main.py
```

Tested On Linux

---

## Future Improvements (Maybe)

- Remove Off-Screen Cars  
- Centralize Screen Bounds  
- Cleaner Separation Between Logic And Visuals  
- Smoother Difficulty Curve  

Not Required For The Purpose Of This Project

---

#### IF YOU HAVE ANY CRITICISM OR FUTURE PROJECT SUGGESTIONS DO NOT HESITATE TO PM ME
