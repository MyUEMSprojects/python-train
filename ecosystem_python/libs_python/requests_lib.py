# requests (HTTP para humanos)
import requests

response = requests.get("https://api.github.com")
print(response.json())

# Equivalente C++: libcurl, mas muito mais simples
# click ou argparse (CLI)
import click


@click.command()
@click.option("--count", default=1, help="Número de saudações")
def hello(count):
    for _ in range(count):
        click.echo("Hello World!")


if __name__ == "__main__":
    hello()

# Comparação: Similar a getopt/getopt_long, mas declarativo
