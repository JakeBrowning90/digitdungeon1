# DIGIT DUNGEON
#### Video Demo:  [<URL HERE>](https://youtu.be/DKmm-Vntznc)
#### Description:
**Overview**
*DIGIT DUNGEON* is an educational text-based game which quizzes the user on arithmetic to advance through turn-based combat. The game is written in Python and played in terminal. 

**Features**
  
The game currently features 4 modes (addition, subtraction, multiplication, and division) which determine the types of problems the player must solve to advance. 

A streak counting function keeps track of the highest number of questions solved correctly in a row, and multiplies that by the total number of correctly answered questions at the end of the game. 

A difficulty selector sets the player’s hitpoints and a score bonus at the end of the game, so players can give themselves less room for error in exchange for a greater final result.

Monster encounters are saved in a list of dictionaries, which is indexed at the start of each new encounter to call the monster’s name, attack text, and HP. 

During gameplay, the player is presented with 3 randomly-generated equations. On their turn, they must input the missing sum, difference, product or quotient to deal damage to the enemy, with bonus damage awarded for solving all 3 correctly. During the enemy’s turn, the player must instead input the missing addend, subtrahend, factor, or divisor to defend against incoming damage. Solving these 3 equations correctly awards an extra HP point to the player.

If the player successfully brings the enemy’s HP to 0, they gain a level, which is added to their bonus damage and is also used to call the next, harder monster from the list. The cap variable also increases, which increases the range of possible equations that can be generated during the next battle. For example, the first battle has a max sum of 10, the second 20, and so on.

**Origin**
  
I first started thinking about this game about 6 years ago when I was working as a teaching assistant at a primary school. One of my duties was to quiz students on arithmetic using flash cards and record their progress. Students were also expected to practice these flash cards as their nightly homework. During this time, I began thinking of how students that consistently performed well on a given set of cards were advanced to the next set, and how this was similar to leveling in role-playing games like *Dungeons and Dragons*. I was also reminded of action-RPGs like *Paper Mario* and *The Legend of Zelda: Breath of the Wild* where players need quick reflexes to make the most of their attack and defense. 

**Why it’s useful**
  
I believe a game such as this would be useful as a learning tool for children, particularly those that enjoy video games and fantasy play. It offers a fun way to memorize information such as multiplication tables, and has great replayability for chasing high-scores and attempting higher difficulties. 

**Future plans**
  
Despite the effort I’ve put into this version which I am submitting as my final project for CS50, I have ideas for other ways to expand this program beyond its current scope.
  
Mixed question types: in its current form, the player will only receive one of the four arithmetic types based on their game selection. In the future, I’d like to add the option to select multiple problem types for a given playthrough.
  
Endless mode: the game has 10 monster encounters, which results in a cap of 100 for any of the problem types. I’d like to add the option to continue beyond this limit for players that want an extra challenge.
  
Custom caps and floors: related to the above, I’d like to add options to let the user choose their own upper and lower limit to the equation generator. This would let players spend more time on a chosen set of problems, or skip over those which are too easy.
  
Difficulty balance: the difficulty setting only affects the player’s starting HP and their score bonus when they finish the game. In the future, I’d like this to also affect conditions such as which questions generate, how much damage monsters can cause, and even randomized loot drops.
  
GUI: my ultimate goal is to have this game’s logic sit at the core of a proper video game with animated graphics and sound effects, perhaps as an application for tablets given their ubiquity in schools and as toys for children.  

**Credits**
  
ASCII lettering comes from http://patorjk.com/

