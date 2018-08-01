import click

@click.command()
@click.option('--verbose', is_flag=True, help="will print verbose messages.")
@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
@click.option('--country', '-n', multiple=True, default='', help='Where are you from?')
def cli(verbose, name, country):
    """This is an example script to learn Click."""
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello {0}".format(country))
    for n in name:
        click.echo('Bye {0}'.format(n))


if __name__ == '__main__':
    cli()
