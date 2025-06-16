# Combat
True to the wargaming roots of Tabletop Roleplaying, Combat is enough of A Thing to make a set of custom rules for the resolution of combat encounters preferable.  The following section details the basics of resolving a combat encounter in HUBRIS.

# The Initiative Wheel 

To track the resolution of a real-time, chaotic experience like a combat encounter, HUBRIS uses a structured time method known as the **Initiative Wheel**

## Structured Time
In HUBRIS, whoever has the highest **initiative** takes the next action.  They spend **ticks** to take that action, decreasing their initiative by that amount, and then the cycle repeats.  If I have significantly more ticks than the next-highest participant, I can take multiple actions before they get a turn.

## The Wheel

To make this comprehensible at the table, the **initiative** is computed modulo 32.  That is to say, there is a wheel with 32 spaces on it, markers for each participant are arranged relatively based on the initial disposition, and then wrap around once they get low enough.  By having the wheel be this size, it is generally always obvious who is next to act, and how much time they have.

## Beginning Combat
At the beggining of combat, each player will make an **initiative** check.  This skill check will determine how quickly a character will react to the onset of hostilities.

### BAG
In bag, your initiative score is equal to the number of **successes** you draw times two, plus the number of **partials** you draw
2 * Successes + Partials

## Actions in Combat

The following is a list of standard actions that everyone has access to in combat.  If an action not listed here or elsewhere in the rules is attempted, it is up to the Gamemaster to determine how many ticks it takes.  The default number of ticks for an otherwise 'normal' action is 10, and 5 ticks represents a generally 'quick' action

### Move
To move, you spend a number of ticks, and then move that number of feet * 5.  You cannot move multiple times in a row.
#### Dash
To Dash, you spend a number of ticks, and then move that number of feet * 10.  This movement provokes **opportunity attacks**, which allow anyone within melee range of you to make a **normal attack**, as detailed below, for only 5 ticks.  They move down the wheel even though it is not their turn.
### Attack

To attack someone, you make the appropriate **Weapon Skill** check against their **Dodge**.  If you get a partial success (A success with any number of partials) you score a **Glancing Hit**, which allows them to make any attack as a **reaction**.  You may choose to forgo a glancing hit, and instead treat it as a miss.

There are three kinds of basic melee attacks:
#### Fast Attack
This attack takes 7 ticks, and deals a point of Fatigue Damage.  You only add half of your **Damage** skill when making a damage check, as detailed below.
#### Normal Attack
This attack takes 10 ticks, and deals a point of Fatigue Damage.  You add your **Damage** skill when making a damage check, as detailed below.
#### Heavy Attack
This attack takes 13 ticks, and deals a point of Fatigue Damage.  You add one and a half times your **Damage** skill when making a damage check, as detailed below.
### Ranged Attacks
Ranged attacks take 7 ticks to perform.  Different weapons have different modifiers to the damage check, which does not use the **Damage** skill for ranged weapons by default, and different reload times.  Some ranged weapons do not deal faitgue damage, instead only checking to damage hit points.  

## Reactions
If an ability allows someone to make a **reaction**, they can take the specified action for half its normal tick cost (unless otherwise specified) when the trigger condition occurs, even if it is not their turn.  You can only take one **reaction** between turns.

# Hit Points, Fatigue and Damage
HUBRIS has a combined system to represent both long-term damage and short-term exhaustion.  

## Fatigue 
Each character has a number of **Faitgue Points**, which begins at 3 and increases every time they increase their **Endurance** score.  **Fatigue Points** count down to 0, and any character with 0 **Fatigue Points** is knocked unconscious.  **Fatigute Points** are restored to their maximum whenever a character takes a **Short Rest**, and most attacks generally deal 1 point of **Fatigue Damage**

## Injury
Each character can also suffer injuries, represented as **Damage**.  When a character is hit with an attack, they make an **Endurance** check, opposed by the **Damage** of the attacker.  Many kinds of armor can give bonuses to the **Endurance** check.  If they fail, they take a point of **Damage**.

Rather than be lost from a set pool, **Damage** accumulates on a character, and is not healed until a character takes a **Long Rest.** When a character's remaining **Fatigue Points** are equal to the amount of **Damage** marked on their character, they are knocked out.  

A character can also gain **Hit Points**, which offset **damage**, preventing it from being marked on a character,   

As an example:

Alex has 7 **Fatigue Points**, and 2 **Hit Points**.  They are worn down in a long, gruelling duel, and drop to 0 **Fatigue Points** after suffering 7 attacks from their opponent.  Even though they are wearing heavy armor, and thus their opponent did 0 points of **damage** to them, they are knocked out.

Dani has 3 **Fatigue Points**, and 0 **Hit Points**.  They suffer a critical injury from a single Heavy Attack, losing one **Fatigue Point** but taking 2 points of **damage**.  Since they have 2 **Fatigue** remaining, and have 2 **damage** marked, they are knocked out.

Jos has 5 **Fatigue Points**, and 1 **Hit Point**.  They suffer in combat, losing three **Fatigue Points** and taking two points of **damage**.  Their **Hit Point** is lost first, leaving them with 2 **Fatigue** remaining, and 1 **damage** marked on their character, and thus remain in the fight.















