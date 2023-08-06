"""Checks for gcloud and homebrew installations."""
import subprocess
from shutil import which
from sys import platform

import questionary as q
from returns.pipeline import is_successful
from returns.result import Failure
from returns.result import Result
from returns.result import Success


def check_brew() -> Result[str, str]:
    """Check if Homebrew is installed."""
    brew_exists = which("brew") is not None

    if not brew_exists:
        failure = "\n".join(
            [
                "You are using MacOS, but you seem to be missing Homebrew...🍺",
                "Please install Homebrew (https://brew.sh/) and verify your "
                "installation by running 'brew doctor'. Then rerun this command.",
            ]
        )

        return Failure(failure)

    brew_version = subprocess.run(["brew", "--version"], text=True, capture_output=True)

    if brew_version.stderr:
        return Failure("   ❌ Homebrew is installed, but seems to be unavailable...")

    success = brew_version.stdout.split("\n")[0]
    return Success(f"   ✅ {success} installed!")


def install_gcloud(success_str: str) -> Result[str, str]:
    """Install gcloud CLI."""
    gcloud_permission = q.confirm("The gcloud CLI is missing, do you want to install it?").ask()
    if not gcloud_permission:
        return Failure(f"{success_str}\n   ❌ You did not install gcloud")

    print("Installing the gcloud CLI...")

    gcloud_installer = subprocess.run(
        ["brew", "install", "--cask", "google-cloud-sdk"],
        capture_output=False,
        text=True,
        shell=False,
        check=True,
    )

    if gcloud_installer.stderr:
        return Failure(f"{success_str}\n   ❌ Error installing the gcloud CLI")

    gcloud_version = subprocess.run(["gcloud", "--version"], capture_output=True, text=True, shell=False, check=True)

    if gcloud_version.stderr:
        return Failure("{success_str}\n   ❌ gcloud installation seemingly succeeded, but gcloud is not available")

    version = gcloud_version.stdout.split("\n")[0]
    return Success(f"{success_str}\n   ✅ {version} installed")


def check_gcloud() -> Result[str, str]:
    """Check if the gcloud CLI is installed."""
    gcloud_exists = which("gcloud") is not None
    if gcloud_exists:
        return Success("✅ gcloud CLI installed")

    if platform != "darwin":
        return Failure(
            "❌ The gcloud CLI is required, but not installed.\n"
            "   Please follow the installation instructions at https://cloud.google.com/sdk/docs/install"
        )

    result = check_brew().bind(install_gcloud)
    if is_successful(result):
        return Success(f"✅ gcloud CLI installed\n{result._inner_value}")
    else:
        return Failure(f"❌ gcloud not installed\n{result._inner_value}")
