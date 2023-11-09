import click

def print_status(dsm, valid):
    click.echo(f'{dsm} is {"valid" if valid else "invalid"}')