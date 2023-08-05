import click
from autumn8.cli import options

from autumn8.cli.commands import models, cloud
from autumn8.cli.interactive import fetch_user_data
from autumn8.common._version import __version__


@options.use_environment
def test_connection(environment):
    """
    Test AutoDL connection with the current API key.
    Displays the user's email address upon successful connection.
    """
    user_data = fetch_user_data(environment)
    print(f"Hello! You're authenticated as {user_data['email']}")


@click.group()
@click.version_option(version=__version__)
def main():
    pass


main.command()(test_connection)

main.command()(models.submit_model)
main.command()(models.login)

main.command()(cloud.list_deployments)
main.command()(cloud.deploy)
main.command()(cloud.terminate_deployment)

if __name__ == "__main__":
    main()
