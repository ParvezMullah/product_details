import typer


def scrape_products(name: str):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(scrape_products)
