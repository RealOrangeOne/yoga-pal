import click
from project.rotate.cli import cli as rotate_cli
from project.disable.cli import cli as disable_cli
from project.enable.cli import cli as enable_cli


MODES = ['laptop', 'tablet']


@click.group('mode', short_help='Rotate components.')
def cli():
    pass


@cli.command('tablet')
@click.pass_context
def tablet(ctx):
    exit_code = ctx.invoke(rotate_cli, component='all', flip=True)
    if exit_code == 0:
        exit_code = ctx.invoke(disable_cli, component='trackpad')
    return exit_code


@cli.command('laptop')
@click.pass_context
def laptop(ctx):
    exit_code = ctx.invoke(rotate_cli, component='all', flip=False)
    if exit_code == 0:
        exit_code = ctx.invoke(enable_cli, component='all')
    return exit_code


@cli.command('list')
def list():
    print("Supported Modes:", ', '.join(MODES))
