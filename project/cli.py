import os.path
import click
import logging


FORMAT = "[%(levelname)s]: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logging.getLogger("requests").setLevel(logging.WARNING)


class YogaPalCLI(click.MultiCommand):

    def list_commands(self, ctx):
        return ['rotate', 'disable', 'enable', 'mode']

    def get_command(self, ctx, name):
        ns = {}
        if name not in self.list_commands(ctx):
            return
        try:
            fn = os.path.join(os.path.dirname(__file__), name + '/cli.py')
            with open(fn) as f:
                code = compile(f.read(), fn, 'exec')
                eval(code, ns, ns)
            return ns['cli']
        except:
            return

cli = YogaPalCLI(help='This tool\'s subcommands are loaded from a plugin folder dynamically.')

if __name__ == '__main__':
    cli()


@click.command(cls=YogaPalCLI)
def cli():
    pass
