from doctest import run_docstring_examples
from os import path
import requests
from shutil import unpack_archive
from subprocess import run
from tempfile import TemporaryDirectory


def get_file(url, out_file):
    r = requests.get(url, allow_redirects=True)
    open(out_file, 'wb').write(r.content)

def dir_exists(directory):
    return path.isdir(directory)

def unpack_example():
    """
    >>> unpack_example()
    """
    with TemporaryDirectory() as temp_dir:
        get_file(
            "https://codeload.github.com/TryGhost/Casper/zip/refs/tags/3.1.3",
            f"{temp_dir}/Casper-3.1.3.zip"
        )
        unpack(f"{temp_dir}/Casper-3.1.3.zip", target_dir=temp_dir)
        assert dir_exists(f"{temp_dir}/Casper-3.1.3")

    assert dir_exists(temp_dir) is False

def unpack(archive, target_dir="."):
    unpack_archive(archive, target_dir)

def example_make_casper_pwa():
    """
    >>> example_make_casper_pwa()
    """
    get_file("https://gitlab.com/kocielnik/ghost-pwa/-/archive/master/ghost-pwa-master.zip", "ghost-pwa-master.zip")
    get_file("https://codeload.github.com/TryGhost/Casper/zip/refs/tags/3.1.3", "Casper-3.1.3.zip")

    unpack("ghost-pwa-master.zip")
    unpack("Casper-3.1.3.zip")

    run(["chmod", "+x", "ghost-pwa-master/make_pwa", "ghost-pwa-master/update_default_hbs.py"], check=True)
    run(["ghost-pwa-master/make_pwa", "Casper-3.1.3.zip"], check=True)

def make_pwa(file_name):
    with TemporaryDirectory() as temp_dir:
        ghost_pwa_temp=f"{temp_dir}/ghost-pwa-master.zip"
        get_file(
            "https://gitlab.com/kocielnik/ghost-pwa/-/archive/master/ghost-pwa-master.zip",
            ghost_pwa_temp
        )
        unpack(ghost_pwa_temp, target_dir=temp_dir)

        run([
            "chmod", "+x",
            f"{temp_dir}/ghost-pwa-master/make_pwa",
            f"{temp_dir}/ghost-pwa-master/update_default_hbs.py"
          ], check=True)
        run([f"{temp_dir}/ghost-pwa-master/make_pwa", file_name], check=True)
