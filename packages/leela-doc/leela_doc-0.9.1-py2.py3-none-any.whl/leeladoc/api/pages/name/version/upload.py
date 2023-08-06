import os
from tempfile import NamedTemporaryFile

import magic
from boltons.fileutils import mkdir_p
from filelock import FileLock, Timeout
from flasket import client, endpoint

from leeladoc import rootdir

VALID_EXTENSIONS = {
    "application/gzip": "gztar",
    "application/x-bzip2": "bztar",
    "application/x-tar": "tar",
    "application/zip": "zip",
}

import shutil


@endpoint
def post(*, app, body, name, version, data, **_kwargs):
    for char in ["/", "\\"]:
        if char in name:
            raise app.BadRequest("Invalid project name")
        if char in version:
            raise app.BadRequest("Invalid project version")

    path = os.path.join(rootdir, "static", name, version)
    mkdir_p(path)

    lockfile = os.path.join(path, "..", f"{version}.lockfile")
    try:
        with FileLock(lockfile, timeout=3), NamedTemporaryFile() as file:
            data.save(file.name)

            ext = magic.from_file(file.name, mime=True)
            if ext not in VALID_EXTENSIONS.keys():
                raise app.BadRequest("Invalid file format")

            shutil.unpack_archive(file.name, path, VALID_EXTENSIONS[ext])

    except Timeout:
        raise app.ServiceUnavailable("Timeout while waiting to grab project lock")
