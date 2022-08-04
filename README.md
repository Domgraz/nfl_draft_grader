# NFL Draft Grade Program

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How it works](how-it-works)
* [Example graph](#example-graph)
* [Example output](example-output)

## General info
This project was made in my free time after the 2022 NFL Draft in order to compare where players were selected in comparision to their concensus rank in the draftable class. This was to see which teams had the best percieved value out of their picks.
	
## Technologies
Project is created with:
* Python 3.9.6
* Pandas
* Matplotlib
	
## How it works
* Once the program is run the user will input a player chosen in the 2022 NFL Draft 

* The user will then input the pick number the player was picked with in the draft
* The program will prompt the user to repeat the process or type "end" to exit the loop
* Once the input is recorded then there will be a generated plot displayed, the grades shown as output, and a csv of this same output

## Example graph
This is the graph generated using the Ravens selections in the draft, if the number of the y axis is positive it shows they were picked later than expected and therefore good value and if it is negative, the player was picked before they were expected and would be bad value.

<img width="1792" alt="Screen Shot 2022-08-04 at 5 14 59 PM" src="https://user-images.githubusercontent.com/78738370/182954173-85a39abe-b31f-43e4-9224-af66dd94a99c.png">

## Example output
This shows the output for the same data displayed above 

<img width="380" alt="Screen Shot 2022-08-04 at 5 15 10 PM" src="https://user-images.githubusercontent.com/78738370/182954298-a1f154c8-c137-4c2a-8551-2036650e3617.png">
