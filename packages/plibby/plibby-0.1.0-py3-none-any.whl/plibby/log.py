from __future__ import annotations

import sys
from functools import partial
from typing import cast
from pathlib import Path

import appdirs
import rich
import zstandard
from loguru import logger as loguru_logger
from loguru._logger import Logger


def get_project_name() -> str | None:
    """Get the project name from the current working directory.

    The project name is found by looking for a pyproject.toml file.
    The following directories are searched, in order:
        - The directory in which sys.argv[0] is located
        - The current working directory

    Each directory is searched for a pyproject.toml file. Searches go up the directory tree
    until a pyproject.toml file is found or the root is reached. If no pyproject.toml file is found
    for any of the directories, None is returned.

    Returns:
        The project name, or None if no pyproject.toml file is found.
    """

    candidates = [p if p.is_dir() else p.parent for p in (Path(sys.argv[0]), Path.cwd())]

    for current_dir in candidates:
        while True:
            if (f := current_dir / "pyproject.toml").exists():
                with f.open("r") as file:
                    for line in file:
                        if line.startswith("name ="):
                            name = line.split("name =")[1].strip().strip('"')
                            return name
            else:
                current_dir = current_dir.parent
                if current_dir == Path("/"):
                    break
    return None


class MyLogger(Logger):
    """Dummy class to make mypy happy."""

    def important(self, msg: str, *args, **kwargs) -> None:
        ...

    def neat(self, msg: str, *args, **kwargs) -> None:
        ...


def log_compress(log_file: str) -> None:
    """Compress a string using zstandard."""

    if not isinstance(log_file, Path):
        log_file = Path(log_file)

    zstandard.ZstdCompressor().copy_stream(
        ifh=log_file.open("rb"),
        ofh=(log_file.with_suffix(".log.zst")).open("wb"),
    )

    # Verify that the contents of the compressed file are the same as the original
    with zstandard.open(log_file.with_suffix(".log.zst"), "rb") as f:
        assert f.read() == log_file.read_bytes()

    log_file.unlink()


def get_logger(name: str) -> MyLogger:
    """Get a logger for use in projects.

    This will set up a logger with a rich handler and a file handler.
    """
    loguru_logger.remove()
    logger_ = loguru_logger.bind(name=name)
    logger_.opt(colors=True)

    logger_.level("IMP", no=28, color="<bold><black><BLUE>", icon="📣")
    logger_.important = partial(logger_.log, "IMP")
    logger_.important.__doc__ = "Log an important message."

    logger_.level("NEAT", no=27, color="<bold><black><GREEN>", icon="🐛")
    logger_.neat = partial(logger_.log, "NEAT")
    logger_.neat.__doc__ = "Log a neat message."

    log_dir = Path(project_appdirs.user_log_dir)
    log_dir.mkdir(exist_ok=True, parents=True)
    file_log = f"{log_dir}/application.log"

    logger_.add(sys.stderr, level="TRACE")
    logger_.add(file_log, level="INFO", enqueue=True, rotation="1 week", compression=log_compress)
    return cast(MyLogger, logger_)


project_name = get_project_name() or "app"
project_console = con = rich.console.Console()
project_appdirs = appdirs.AppDirs(appname=project_name)
project_logger = log = get_logger(project_name)

__all__ = (
    "con",
    "log",
    "project_appdirs",
    "project_console",
    "project_logger",
    "project_name",
)


if __name__ == "__main__":
    log.info(f"Running log.py as a script. Info:")
    log.info(f"project_name: {project_name}")

    log.info(f"project_appdirs:")
    for attr in ("user_cache_dir", "user_config_dir", "user_data_dir", "user_log_dir"):
        log.info(f"    {attr}: {getattr(project_appdirs, attr)}")
    log.info(f"project_logger: {project_logger}")
    log.info(f"project_console: {project_console}")

    log.trace("This is a trace message")
    log.debug("This is a debug message")
    log.info("This is an info message")
    log.success("This is a success message")
    log.warning("This is a warning message")
    log.error("This is an error message")
    log.critical("This is a critical message")
    log.important("This is an important message")
    log.neat("This is a neat message")
