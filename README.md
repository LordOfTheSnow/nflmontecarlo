# NFL Monto-Carlo-Simulation

This is going to be my attempt to simulate the outcome of an NFL season (how possible is it that team xyz will make the playoffs, what needs to happen for team xyz to make the playoffs, who will win the Superbowl etc.).

The goal is to start with an empty schedule and simulate different outcomes of games.

Once the first games have been played, try to calculate team strengths and then re-simulate the rest of the remaining schedule but taking the calculated team strength into consideration, so that the outcome is getting more and more precise as the season progresses.

## (work in progress) Step 1: Set up the basics

* set up all the basic classes needed to hold the necessary data, such as 
  * league 
  * conferences
  * divisions
  * teams
  * games

* read the schedule from the ESPN website

* calculate standings and team data / statistics based upon real data

## (future) Step 2: Run hundreds / thousands / more(?) of simulations

* create possible outcomes
* rank the probabilities

## (future) Step 3: create human readable output

* HTML pages
* maybe a web app (Flask?)