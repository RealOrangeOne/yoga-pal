import click
import os


TRACKPAD_COMMAND = "xinput {} 'SynPS/2 Synaptics TouchPad'"
TOUCH_COMMAND = "xinput {} 'ELAN Touchscreen'"


@click.command('disable', short_help='Disable component.')
@click.argument('component', default='all', type=click.Choice(['trackpad', 'touch', 'all']))
@click.option('--enable/--disable', default=None)
def cli(component, enable):
    exit_code = 0
    mode = "enable" if enable else "disable"
    print("Mode", mode)
    if component in ['trackpad', 'all']:
        exit_code = os.system(TRACKPAD_COMMAND.format(mode))

    if exit_code != 0 and component in ['touch', 'all']:
        exit_code = os.system(TOUCH_COMMAND.format(mode))

    return exit_code
