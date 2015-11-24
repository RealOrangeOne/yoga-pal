import click
import os

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
