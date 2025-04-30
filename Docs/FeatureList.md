# Features

## Requirements
- Parse the txt file
- Use parsed data to navigate submarine
    - 2 axis of movement
        - horizontal: `forward`
            - positive value is forward, negative is backward
        - depth: `up`, `down`
            - `up` is negative depth
            - `down` is positive depth
- Output current/final position
    - horizontal * depth = position

## Kata 1
- Sub movements
    - horizontal: x values
    - depth: y values
        - `up` and `down` keywords are translational

## Kata 2
- Sub movements
    - horizontal: x values
    - depth: aim
        - `up` and `down` keywords are rotational

## Goals
- Write one set of functions that can work for either scenario
- Allow user to choose which scenario they want to run
- Have a graphical way to view the data
    - Does not need to be real-time
    - Main use will be to verify that the correct logic is run for the scenario
- Integrate testing
    - pytest for basic functions
    - unittest if mocking is needed

## Flow
- Data parsing
    - read file
    - convert commands into key/value pairs
        - keys:
            - horizontal
            - up
            - down
        - values: signed int
- Submarine class
    - initialization
        - starting location: horizontal, depth, aim
            - default: 0, 0, 0
    - horizontal: int
    - depth: int
    - position: int (calculated)
- Plotting
    - Optional post process to visualize data
- Running app
    - argument flags to decide state
    - scripts to set flags for user
- Output final location
    - print submarine position after all data has been parsed and run

### Notes
- Suggest removing `up` and `down` keywords and just use + and - values like horizontal
- Convert txt file to Json so that there is better error handling
- For real-time commands to be interpreted (such as over Serial, MQTT, etc) the main app would need to be updated to a while loop and another class added for retrieving data.