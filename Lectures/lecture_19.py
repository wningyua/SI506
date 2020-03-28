import random as rdm
import uuid

# LECTURE 19 Objectives

# Objectives
# 1. Buld a text-based command line game.
# 2. Work with class supertypes and subtypes.
# 3. Learn about the Force, a fictional Star Wars franchise concepts.

class TheForce:
    """The Force is an energy field that connects everything in the universe,
    and is known by a variety of names throughout galactic history.

    The Force is created by life, and therefore, resides in all lifeforms.
    It is especially powerful in a select group of individuals. These
    beings were deemed Force-sensitive, and were capable of consciously
    sensing the Force. With this conscious sense of the Force came the ability
    to harness it, accessing various Force powers. Unlike organic beings, droids
    and other artificial constructs existed outside of the Force.

    The light side of the Force, is an aspect of the Force. The light side is
    aligned with calmness and was used for knowledge and defense.

    The dark side of the Force, was also an aspect of the Force. Individuals
    who used the dark side drew their power from more intense, raw and darker
    emotions such as fear, anger, hatred, passion, and aggression.

    See: https://starwars.fandom.com/wiki/The_Force,
         https://starwars.fandom.com/wiki/Light_side_of_the_Force,
         https://starwars.fandom.com/wiki/Dark_side_of_the_Force

    Attributes:
        aspects: the two sides of the Force: light and darkness
    """

    aspects = ('the light side', 'the dark side')


class ForceSensitive():
    """Force-sensitives, also known also known as Force-users,
    Force wielders, or Force Adepts, were sentient and non-sentient
    lifeforms that possessed a strong connection to the mystical
    energy field known as the Force.

    See https://starwars.fandom.com/wiki/Force-sensitive

    Attributes:
        name: name of force-sensitive being
        strength: current strength
        force: chosen aspect of the Force

    Methods:
        change_strength: change current strength
    """

    def __init__(self, name, strength, force):
        """Initialize instance of force-sensitive being.

        Parameters:
            name (str): name of individual
            strength (int): current strength
            force (TheForce): aspect of the Force embraced by individual

        Returns:
            None
        """

        self.name = name
        self.strength = strength
        self.force = force # component


    def change_strength(self, value):
        """Increment/decrement current strength. Positive or negative
        whole numbers accepted.

        Parameters:
            value (int): add/subtract strength by this value

        Returns:
            None
        """

        self.strength += value


    def __str__(self):
        """Informal string representation of instance.

        Parameters:
            None

        Returns:
            str: name of instance
        """

        return f"{self.name}, a Force-sensitive or Force-wielder"


class Jedi(ForceSensitive):
    """Member of the Jedi Order; protectors united in their devotion to
    the light side of the Force.

    See https://starwars.fandom.com/wiki/Jedi_Order
    """

    def __init__(self, name, strength, force):
        """Initialize instance of force-sensitive being.

        Parameters:
            action (tuple): move, aim, and controlling Force aspect

        Returns:
            None
        """

        super().__init__(name, strength, force)

        self.action = None


    def wield_lightsaber(self, action):
        """Move and aim lightsaber under the controlling influence
        of the Force.

        Parameters:
            action (tuple): current move, aim, and controlling Force aspect

        Returns:
            None
        """

        self.action = action



    def __str__(self):
        """Informal string representation of instance.

        Parameters:
            None

        Returns:
            str: name of instance
        """

        return self.name


class Sith(ForceSensitive):
    """The Sith, also referred to as the Sith Order, was an ancient
    religious order of Force-sensitives or Force-wielders devoted to
    the dark side of the Force.

    The dark side of the Force, also known as Bogan, was an aspect
    of the Force. Individuals who used the dark side drew their
    power from more intense, raw and darker emotions such as fear,
    anger, hatred, passion, and aggression.

    See https://starwars.fandom.com/wiki/Sith;
        https://starwars.fandom.com/wiki/Dark_side_of_the_Force
    """


    def __init__(self, name, strength, force):
        """Initialize instance of force-sensitive being.

        Parameters:
            action (tuple): move, aim, and controlling Force aspect

        Returns:
            None
        """

        super().__init__(name, strength, force)

        self.action = None


    def wield_lightsaber(self, action):
        """Aim and move lightsaber under the controlling influence
        of the Force.

        Parameters:
            action (tuple): current move, aim, and controlling Force aspect

        Returns:
            None
        """

        self.action = action


    def __str__(self):
        """Informal string representation of instance.

        Parameters:
            None

        Returns:
            str: name of instance
        """

        return self.name


class GameEngine:
    """The game engine.

    Attributes:
        id_: game instance identifer
        opponents: combatants TODO NEXT VERSION

    Methods:
        saber_aim: user selects zone in which to move lightsaber
        saber_move: user moves lightsaber
    """

    def __init__(self):
        """Initialize instance of force-sensitive being.

        Parameters:
            id_ (UUID): game identifier
            opponents (tuple): combatants TODO NEXT VERSION

        Returns:
            None
        """

        self.id_ = uuid.uuid4()


    def saber_aim(self):
        """Aim lightsaber. User supplies value via built-in input() function

        Parameters:
            None

        Returns:
            None
        """

        options = ('h', 'c', 'l', 'q')
        prompt = 'Aim high (h), center (c), or low (l): type h, c, or l: '
        selection = ''

        while selection.lower() not in options:
            selection = input(prompt)

        return selection.lower()


    def saber_move(self):
        """Move lightsaber. User supplies value via built-in input() function.

        Parameters:
            None

        Returns:
            None
        """

        options = ('c', 't', 'p', 'q')
        prompt = 'Cut (c), thrust (t), or parry (p) with your lightsaber: type c, t, or p: '
        selection = ''

        while selection.lower() not in options:
            selection = input(prompt)

        return selection.lower()


    def random_saber_action(self):
        """Randomly selected lightsaber aim and move.

        Parameters:
            None

        Returns:
            None
        """

        options = [
            ('c', 'h'), ('c', 'c'), ('c', 'l'),
            ('t', 'h'), ('t', 'c'), ('t', 'l'),
            ('p', 'h'), ('p', 'c'), ('p', 'l')
        ]

        return rdm.choice(options) # select list element randomly


    def score_matrix(self, x, y):
        """Process selections and award scores.

        Parameters:
            x (ForceSensitive): being controlled by user
            y (ForceSensitive): being controlled by engine

        Returns:
            tuple: score for x, score for y
        """

        if x[0] == 'p' and y[0] == 'p':
            print(f"Both parry: {x} vs {y}")
            return 0, 0

        if x[0] in ('c', 't') and x[1] == 'h':
            if y[0] == 'p' and y[1] == 'h':
                print(f"Parry successful: {x} vs {y}")
                return -1, 0
            if y[0] == 'p' and y[1] in ('c', 'l'):
                print(f"Parry unsuccessful: {x} vs {y}")
                return 0, -1
            if y[0] in ('c', 't') and y[1] in ('h', 'c', 'l'):
                print(f"Both score: {x} vs {y}")
                return -1, -1

        if x[0] == 'p' and x[1] == 'h':
            if y[0] in ('c', 't') and y[1] == 'h':
                print(f"Parry successful: {x} vs {y}")
                if 'light' in x[2]:
                    return 2, -1
                else:
                    return 0, -1
            if y[0] in ('c', 't') and y[1] in ('c', 'l'):
                print(f"Parry unsuccessful: {x} vs {y}")
                return -1, 0

        if x[0] in ('c', 't') and x[1] == 'c':
            if y[0] == 'p' and y[1] == 'c':
                print(f"Parry successful: {x} vs {y}")
                return -1, 0
            if y[0] == 'p' and y[1] in ('h', 'l'):
                print(f"Parry unsuccessful: {x} vs {y}")
                return 0, -1
            if y[0] in ('c', 't') and y[1] in ('h', 'c', 'l'):
                print(f"Both score: {x} vs {y}")
                return -1, -1

        if x[0] == 'p' and x[1] == 'c':
            if y[0] in ('c', 't') and y[1] == 'c':
                print(f"Parry successful: {x} vs {y}")
                if 'light' in x[2]:
                    return 2, -1
                else:
                    return 0, -1
            if y[0] in ('c', 't') and y[1] in ('h', 'l'):
                print(f"Parry unsuccessful: {x} vs {y}")
                return -1, 0

        if x[0] in ('c', 't') and x[1] == 'l':
            if y[0] == 'p' and y[1] == 'l':
                print(f"Parry successful: {x} vs {y}")
                return -1, 0
            if y[0] == 'p' and y[1] in ('h', 'c'):
                print(f"Parry unsuccessful: {x} vs {y}")
                return 0, -1
            if y[0] in ('c', 't') and y[1] in ('h', 'c', 'l'):
                print(f"Both score: {x} vs {y}")
                return -1, -1

        if x[0] == 'p' and x[1] == 'l':
            if y[0] in ('c', 't') and y[1] == 'l':
                print(f"Parry successful: {x} vs {y}")
                if 'light' in x[2]:
                    return 2, -1
                else:
                    return 0, -1
            if y[0] in ('c', 't') and y[1] in ('h', 'c'):
                print(f"Parry unsuccessful: {x} vs {y}")
                return -1, 0


def main():
    """TODO"""

    # 1.0 INITIALIZE
    jedi = Jedi("Rey", 5, TheForce.aspects[0])
    sith = Sith("Kylo", 5, TheForce.aspects[1])
    game = GameEngine() # TODO pass opponents to engine

    # 1.1 START GAME
    print(f"\nSTAR WARS: JEDI vs SITH\n")

    print(
        'Rules',
        "1. Cut, thrust, parry with your lightsaber, aiming high, center, or low",
        '2. A successful lightsaber cut or thrust will cost the Sith strength (-1)',
        "3. Failing to parry a Sith's lightsaber cut or thrust will cost you strength (-1)",
        "4. Parrying a Sith's lightsaber will increase your strength (+2)",
        "5. Enter 'q' to break off combat",
        sep='\n'
        )

    print(f"\nUnsheath your lightsaber, a Sith approaches . . .\n")

    # 1.2 COMBAT COMMENCES
    while jedi.strength > 0 and sith.strength > 0:

        # 1.2.1 Quit game?
        move = game.saber_move()
        if move == 'q':
            print(f"Breaking off combat\n")
            break

        aim = game.saber_aim()
        if aim == 'q':
            print(f"Breaking off combat\n")
            break

        # 1.2.2 Jedi wields lightsaber
        jedi.wield_lightsaber((move, aim, jedi.force)) # pass a tuple

        # 1.2.3 Sith wields lightsaber
        random_move, random_aim = game.random_saber_action() # unpack
        sith.wield_lightsaber((random_move, random_Force, sith.force))

        print(f"\n{jedi.name} {jedi.action} vs {sith.name} {sith.action}")

        # 1.2.4 Score combat round
        jedi_score, sith_score = game.score_matrix(jedi.action, sith.action) # unpack
        jedi.change_strength(jedi_score)
        sith.change_strength(sith_score)

        print(f"{jedi.name} {jedi.strength} {sith.name} {sith.strength}")

        # 1.2.5 Check for winner
        # UNCOMMENT AND FIX
        if jedi.strength > 0 and sith.strength == 0:
            print(f"{jedi.name} wins\n")
        elif jedi.strength == 0 and sith.strength > 0:
            print(f"{sith.name} wins\n")
        elif jedi.strength == 0 and sith.strength == 0:
            print(f"{jedi.name} and {sith.name} draw\n")
        else:
            print('\n') # padding


if __name__ == '__main__':
    main()