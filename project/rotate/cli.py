import click
import os


@click.command('rotate', short_help='Shows file changes.')
@click.arguement('component', default='all', type=click.Choices(['screen', 'touch', 'all']))
@click.option('--flip/--default', default=None)
def cli(component, flip):
    pass

    