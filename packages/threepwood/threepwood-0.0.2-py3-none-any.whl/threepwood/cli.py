from threepwood.version import __version__
import click
import tomllib
from pathlib import Path


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group()
@click.version_option(version=__version__)
def thrpwd():
    print("hi")
    pass


@thrpwd.command()
@click.option('--name', default='Guybrush Threepwood', help='The name of the pirate.')
@click.option('--caps', is_flag=True, help='Shout it')
def hello(**kwargs):
    '''Says hello'''
    out = "Hi! My name's {0}, and I want to be a pirate!".format(kwargs['name'])
    if kwargs['caps']:
        out = out.upper()
    click.echo(out)
    if config is not None:
        click.echo(config['title'])


@thrpwd.command()
@click.argument('name')
def goodbye(**kwargs):
    '''Says goodbye'''
    click.echo("Nice place you have here.")
    click.echo("Well, goodbye, {name}!".format(**kwargs))


def lchuck():
    '''A second executable'''
    click.secho("There's nothing like the hot winds of hell blowing in your face", fg='red', bold=True)


toml_path = Path.home() / '.threepwood.toml'
try:
    with open(toml_path, 'rb') as f:
        config = tomllib.load(f)
except FileNotFoundError:
    config = {}
    pass


if __name__ == "__main__":
    thrpwd()
