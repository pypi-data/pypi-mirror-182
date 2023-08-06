"""Doctor related commands.

Commands invoked by dpteam doctor <some-command> are defined here.
"""

from returns.pipeline import is_successful
from rich.console import Console
from rich.style import Style

from dapla_team_cli.doctor.gcloud import check_gcloud
from dapla_team_cli.doctor.keycloak import check_keycloak


console = Console()

styles = {
    "normal": Style(blink=True, bold=True),
    "error": Style(color="red", blink=True, bold=True),
    "success": Style(color="green", blink=True, bold=True),
    "warning": Style(color="dark_orange3", blink=True, bold=True),
}


def doctor() -> None:
    """Check your system for potential problems.

    This could be e.g. if some required tooling is missing.
    The command provides advice and pointers to how to fix issues.
    Will exit with a non-zero status if any potential problems are found.
    """
    console.print("Checking for uninstalled dependencies...", style=styles["normal"])

    checks = [check_gcloud(), check_keycloak()]

    print("Summary:")

    for check in checks:
        print(check._inner_value)

    all_good = all(is_successful(check) for check in checks)
    if all_good:
        print("✅ You are good to go")
    else:
        print("❌ There were some errors")
