<img src="https://raw.githubusercontent.com/eclipse-zenoh/zenoh/master/zenoh-dragon.png" height="150">

[![CI](https://github.com/eclipse-zenoh/zenoh-python/workflows/CI/badge.svg)](https://github.com/eclipse-zenoh/zenoh-python/actions?query=workflow%3A%22CI%22)
[![Documentation Status](https://readthedocs.org/projects/zenoh-python/badge/?version=latest)](https://zenoh-python.readthedocs.io/en/latest/?badge=latest)
[![Discussion](https://img.shields.io/badge/discussion-on%20github-blue)](https://github.com/eclipse-zenoh/roadmap/discussions)
[![Discord](https://img.shields.io/badge/chat-on%20discord-blue)](https://discord.gg/2GJ958VuHs)
[![License](https://img.shields.io/badge/License-EPL%202.0-blue)](https://choosealicense.com/licenses/epl-2.0/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Eclipse zenoh Python API

[Eclipse zenoh](http://zenoh.io) is an extremely efficient and fault-tolerant [Named Data Networking](http://named-data.net) (NDN) protocol
that is able to scale down to extremely constrainded devices and networks.

Check the website [zenoh.io](http://zenoh.io) and the [roadmap](https://github.com/eclipse-zenoh/roadmap) for more detailed information.

-------------------------------
## How to install it

The Eclipse zenoh-python library is available on [Pypi.org](https://pypi.org/project/eclipse-zenoh/).
Install the latest available version using `pip`:
```
pip install eclipse-zenoh
```

To install the latest nightly build of the development version do:
```
pip install eclipse-zenoh-nightly
```

:warning:WARNING:warning: zenoh-python is developped in Rust.
On Pypi.org we provide binary wheels for the most common platforms (MacOS, Linux x86). But also a source distribution package for other platforms.
However, for `pip` to be able to build this source distribution, there some prerequisites:
 - `pip` version 19.3.1 minimum (for full support of PEP 517).
   (if necessary upgrade it with command: `'sudo pip install --upgrade pip'` )
 - Have a Rust toolchain installed (instructions at https://rustup.rs/)

### Supported Python versions and platforms

zenoh-python has been tested with Python 3.6, 3.7, 3.8 and 3.9.

It relies on the [zenoh](https://github.com/eclipse-zenoh/zenoh/tree/master/zenoh) Rust API which require the full `std` library. See the list Rust supported platforms here: https://doc.rust-lang.org/nightly/rustc/platform-support.html .


-------------------------------
## How to build it

Requirements:
 * Python >= 3.7
 * pip >= 19.3.1
 * (Optional) A Python virtual environment (for instance [virtualenv](docs.python.org/3.10/tutorial/venv.html) or [miniconda](https://docs.conda.io/en/latest/miniconda.html))
 * [Rust and Cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html).

Steps:
 * Install developments requirements:
   ```bash
   pip install -r requirements-dev.txt
   ```

 * Ensure your system can find the building tool `maturin` (installed by previous step).
   For example, it is placed at _$HOME/.local/bin/maturin_ by default on Ubuntu 20.04.
    ```bash
    export PATH="$HOME/.local/bin:$PATH"
    ```

 * Build and install zenoh-python:
   * With a virtual environment active:
    ```bash
    maturin develop --release
    ```
   * Without one:
    ```bash
    maturin build --release
    pip install ./target/wheels/<there should only be one .whl file here>
    ```



-------------------------------
## Running the Examples

The simplest way to run some of the example is to get a Docker image of the **zenoh** network router (see https://github.com/eclipse-zenoh/zenoh#how-to-test-it) and then to run the examples on your machine.

Then, run the zenoh-python examples following the instructions in [examples/zenoh/README.md](https://github.com/eclipse-zenoh/zenoh-python/blob/master/examples/zenoh/README.md)
