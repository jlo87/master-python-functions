#!/usr/bin/env python3
"""Use Click to build out a CLI for the wiki_news_keywords.py library."""

import click  # type: ignore
from funcLog import wiki_news_keywords as wnk


# Build a click group
@click.group()
def cli():
    """Search for keywords in wikipedia articles.

    Example:
    $ wiki-keywords search "python"
    $ wiki-keywords content "fix bankruptcy"
    """


# Build a click command for the search function
@click.command("search")
@click.argument("search_term", type=str, default="ftx bankruptcy")
def search(search_term):
    """Search for a wikipedia article.

    Example:
    $ wiki-keywords search "python"
    """
    search_results = wnk.wiki_search(search_term)
    click.echo(search_results)


# Build a click command for the content function
@click.command("keywords")
@click.argument("search_term", type=str, default="ftx bankruptcy")
@click.option("--limit", type=int, default=3)
def keywords_cli(search_term, limit):
    """Return the top 10 keywords from a wikipedia article.

    Example:
    $ wiki-keywords keywords "ftx bankruptcy"
    """
    # Return the top limit keywords in color green
    keywords = wnk.wiki_keywords(search_term)
    for keyword in keywords[:limit]:
        click.echo(click.style(keyword[0], fg="green"))


# Invoke the app
if __name__ == "__main__":
    cli.add_command(search)
    cli.add_command(keywords_cli)
    cli()
