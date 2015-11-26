import click
import os


TRACKPAD_COMMAND = "xinput disable 'SynPS/2 Synaptics TouchPad'"
TOUCH_COMMAND = "xinput disable 'ELAN Touchscreen'"


@click.command('disable', short_help='Disable component.')
@click.argument('component', default='all', type=click.Choice(['trackpad', 'touch', 'all']))
def cli(component):
    exit_code = 0
    if component in ['trackpad', 'all']:
        exit_code = os.system(TRACKPAD_COMMAND)

    if exit_code != 0 and component in ['touch', 'all']:
        exit_code = os.system(TOUCH_COMMAND)

    return exit_code
