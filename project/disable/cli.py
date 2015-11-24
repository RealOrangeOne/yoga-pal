import click
import os

TRACKPAD_COMMAND = "xinput {} 'SynPS/2 Synaptics TouchPad'"

@click.command('disable', short_help='Disable component.')
@click.argument('component', default='all', type=click.Choice(['trackpad', 'touch', 'all']))
@click.option('--enable/--disable', default=None)
def cli(component, enable):
    if component in ['trackpad', 'all']:
        exit_code = 0
        mode = "enable" if enable else "disable"
        exit_code = os.system(TRACKPAD_COMMAND.format(mode))
