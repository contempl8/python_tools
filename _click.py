# https://github.com/pallets/click
import click

@click.group()
def cli():
    pass

@click.command()
def print_thing():
    '''Prints a thing'''
    print("Prints this thing")

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

cli.add_command(print_thing)
cli.add_command(hello)

if __name__ == '__main__':
    cli()