import random
import time

import actors

ascii_art = '''
   ▄▄▄▄▄   █ ▄▄  ▄███▄   ▄███▄     ▄▀  █     ▄███▄   
  █     ▀▄ █   █ █▀   ▀  █▀   ▀  ▄▀    █     █▀   ▀  
▄  ▀▀▀▀▄   █▀▀▀  ██▄▄    ██▄▄    █ ▀▄  █     ██▄▄    
 ▀▄▄▄▄▀    █     █▄   ▄▀ █▄   ▄▀ █   █ ███▄  █▄   ▄▀ 
            █    ▀███▀   ▀███▀    ███      ▀ ▀███▀   
             ▀                                       
                                                     
            ▄████  ██   █▀▄▀█ ▄█ █    ▀▄    ▄        
            █▀   ▀ █ █  █ █ █ ██ █      █  █         
            █▀▀    █▄▄█ █ ▄ █ ██ █       ▀█          
            █      █  █ █   █ ▐█ ███▄    █           
             █        █    █   ▐     ▀ ▄▀            
              ▀      █    ▀                          
                    ▀                                
                ███   █▄▄▄▄ ██     ▄ ▄   █           
                █  █  █  ▄▀ █ █   █   █  █           
                █ ▀ ▄ █▀▀▌  █▄▄█ █ ▄   █ █           
                █  ▄▀ █  █  █  █ █  █  █ ███▄        
                ███     █      █  █ █ █      ▀       
                       ▀      █    ▀ ▀               
                             ▀                      
'''


def print_header():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(ascii_art)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('')


def game_loop(name: str):
    creatures = [
        actors.Creature('Darth', random.randint(2, 4), 'claw'),
        actors.Creature("Ghost of Gizmo", random.randint(2, 4), 'slime'),
        actors.Dog('Delilah', random.randint(2, 5), 'fart', (random.randint(1, 10) > 8)),
        # actors.Parent('Mom', random.randint(3, 7), 'nag', 'angry'),
        actors.Parent('Mom', random.randint(3, 7), 'nag', random.randint(0, 2)),
        # actors.Parent('Dad', random.randint(5, 10), 'burp', 'tired')
        actors.Parent('Dad', random.randint(5, 10), 'burp', random.randint(0, 2))
    ]

    player = actors.Hero(name, random.randint(3, 20), 'nerf gun')
    lives = 3

    print('\n{} was supposed to do homework,\n'
          'but went out front to play with friends instead.'
          .format(name))
    while True:

        active_creature = random.choice(creatures)

        print('\n{} of level {} has cornered {} in the kitchen...'
              .format(active_creature.name.title(), active_creature.level, name))

        cmd = input('{}, do you want to [a]ttack, [r]unaway, or [l]ook around? '
                    .format(name)).lower()

        if cmd == 'a':
            print('\n{} attacks {}!'.format(name, active_creature.name))
            if player.defeat(active_creature):
                print('{} has defeated {}'.format(name, active_creature.name))
                creatures.remove(active_creature)
            else:
                print('{} is defeated by {}!'.format(name, active_creature.name))
                lives -= 1
                print('{} has {} lives remaining'.format(name, lives))
                if lives <= 0:
                    print('\n{} is DEAD! Goodbye.'.format(name))
                    break

        elif cmd == 'r':
            print('{} has to poop and runs to the bathroom...'.format(name))
            time.sleep(3)
            print('{} is done pooping and returns feeling better than ever.'.format(name))

        elif cmd == 'l':
            print('\n{} looks around and sees:'.format(name))
            for c in creatures:
                print(' * {} (level: {})'.format(c.name.title(), c.level))

        else:
            quitter = input('\nDo you really want to quit like a [q]uiting quitter? ')
            if quitter.lower() in ['y', 'x', 'q']:
                print('\n{} has quit Family Brawl...\nYou LOOSE!'.format(name))
                break
            else:
                print("I knew you weren't a quitting quitter!")


def main():
    print_header()
    hero_name = input('What is your name? ').title()

    game_loop(hero_name)


if __name__ == '__main__':
    main()
