# Submarine_Kata

## Overview
Test scenario where the user needs to parse commands from an input log to navigate a submarine to safety. There are multiple steering scenarios that are covered. Those scenarios are outlined in the `Docs` folder.

## Run application
The application can be run in multiple modes. Each of these modes have a specific bash script associated with them. These scripts are located in the `Scripts` folder. The code allows for the travel of the submarine to be plotted for visual reference. The basic navigation should only show straight horizontal and vertical lines. The graph for the advanced navigation (aim), will have diagonal lines because of the added trajectory component. NOTE: The scripts assume that they are being run from the root directory.
- Run the application using the basic navigation requirements:
    - `./Scripts/run_app.sh`
- Run the application using the basic navigation requirements and plot the locations:
    - `./Scripts/run_app_graph.sh`
- Run the application using the aim navigation requirements:
    - `./Scripts/run_app_aim.sh`
- Run the application using the aim navigation requirements and plot the locations:
    - `./Scripts/run_app_aim_graph.sh`

## Run Tests
Test for this application have been written using pytest. The test files are located in the `Tests` directory. A script has been written to run all tests. NOTE: The tests assume that they are being run from the root directory.
- To run all tests
    - `./Scripts/run_tests.sh`