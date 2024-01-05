# NFL Monto-Carlo-Simulation

This is going to be my attempt to simulate the outcome of an NFL season (how possible is it that team xyz will make the playoffs, what needs to happen for team xyz to make the playoffs, who will win the Superbowl etc.).

The goal is to start with an empty schedule and simulate different outcomes of games.

Once the first games have been played, try to calculate team strengths and then re-simulate the rest of the remaining schedule but taking the calculated team strength into consideration, so that the outcome is getting more and more precise as the season progresses.

## Disclaimer

### Work in progress

This project is _work in progress_. It is far from being finished, in fact I have just scratched the surface of what I have planned. So do not expect a fully working piece of software here (yet).

The releases published here are more to be seen as milestones than functional releases. Version numbers <1 indicate that I have not yet achieved what I want.

### Data

Though the NFL is a multi-billion (or even trillon) business, it seems that not even simple data such as games, scores, basic team data is available for free as an API.

Luckily ESPN kind of fills this space by offering NFL data thru open websites/webservices that provide JSON data. I have not yet checked the legal terms for downloading and using this data, so I take no responsibilty for any legal implications when using this data. **Therefore I strongly recommend not** using any of the code that downloads data from ESPN in public/commercial projects. 

## High Level Milestones

### (work in progress) Step 1: Set up the basics

* set up all the basic classes needed to hold the necessary data, such as 
  * league 
  * conferences
  * divisions
  * teams
  * games

* read the schedule from the ESPN website

* calculate standings and team data / statistics based upon real data

### (future) Step 2: Run hundreds / thousands / more(?) of simulations

* create possible outcomes
* rank the probabilities

### (future) Step 3: create human readable output

* HTML pages
* maybe a web app (Flask?)