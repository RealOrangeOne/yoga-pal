import click
import os
import subprocess


SCREEN_COMMAND = "xrandr -o {}"
SCREEN_FLIP = "inverted"
SCREEN_DEFAULT = "normal"

TOUCH_COMMAND = "xinput set-prop 'ELAN Touchscreen' 'Coordinate Transformation Matrix' {}"
TOUCH_FLIP = "-1 0 1 0 -1 1 0 0 1"
TOUCH_DEFAULT = "1 0 0 0 1 0 0 0 1"


@click.command('rotate', short_help='Rotate components.')
@click.argument('component', default='all', type=click.Choice(['screen', 'touch', 'all']))
@click.option('--flip/--default', default=None)
def cli(component, flip):
    if flip == None:  # If no rotation flag was given, flip the screen
        inverted = is_screen_currently_inverted()
        screen_addon = SCREEN_DEFAULT if inverted else SCREEN_FLIP
        touch_addon = TOUCH_DEFAULT if inverted else TOUCH_FLIP
    else:
        screen_addon = SCREEN_DEFAULT if not flip else SCREEN_FLIP
        touch_addon = TOUCH_DEFAULT if not flip else TOUCH_FLIP

    SCREEN = SCREEN_COMMAND.format(screen_addon)
    TOUCH = TOUCH_COMMAND.format(touch_addon)

    exit_code = 0
    if component in ['screen', 'all']:
        print("Rotating Screen...")
        exit_code = os.system(SCREEN)
    if exit_code == 0 and component in ['touch', 'all']:
        print("Rotating Touch Screen...")
        exit_code = os.system(TOUCH)

    return exit_code


def is_screen_currently_inverted():
    """ If setting the screen to normal rotation doenst change anything, then the screen is already the right way round.
    If it does, then it was inverted originally
    """
    original_output = subprocess.check_output("xrandr --query", shell=True)
    os.system("xrandr -o normal")
    new_output = subprocess.check_output("xrandr --query", shell=True)
    was_inverted =  not (new_output == original_output)
    if was_inverted:
        os.system("xrandr -o inverted")  # restore it to the way it was initially

    return was_inverted
