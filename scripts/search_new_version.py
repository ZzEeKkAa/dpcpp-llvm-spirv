import re

from conda.base.context import context
from conda.core.subdir_data import SubdirData
from conda.models.channel import Channel
from conda.models.match_spec import MatchSpec
from conda.models.version import VersionOrder


def search_dpcpp_impl(platform: str, version: str):
    spec = MatchSpec(f"dpcpp_impl_{platform}-64={version}")
    channel_urls = (Channel(f"intel/{platform}-64"),)

    matches = sorted(
        SubdirData.query_all(spec, channel_urls, context.subdirs),
        key=lambda rec: (rec.name, VersionOrder(rec.version), rec.build),
    )

    return matches[-1]


def main():
    with open("pkg/pyproject.toml", "r+") as file:
        # Reading from a file
        pyproject = file.read()
        version = re.search(r"dpcpp-cpp-rt==([0-9\.]+)", pyproject).group(1)

    win_pkg = search_dpcpp_impl("win", version)
    lin_pkg = search_dpcpp_impl("linux", version)

    win_build = win_pkg.build[6:]
    lin_build = lin_pkg.build[6:]
    win_md5 = win_pkg.md5
    lin_md5 = lin_pkg.md5

    with open("conda-recipe/meta.yaml", "r+") as file:
        meta = file.read()

    meta = re.sub(r"(set version = \")([0-9\.]+)(\")", f"\\g<1>{version}\\3", meta)
    meta = re.sub(
        r"(set intel_build_number = \")([0-9]+)(\".* # \[linux)",
        f"\\g<1>{lin_build}\\3",
        meta,
    )
    meta = re.sub(
        r"(set intel_build_number = \")([0-9]+)(\".* # \[win)",
        f"\\g<1>{win_build}\\3",
        meta,
    )
    meta = re.sub(r"(md5: )([0-9a-f]+)(.* # \[linux)", f"\\g<1>{lin_md5}\\3", meta)
    meta = re.sub(r"(md5: )([0-9a-f]+)(.* # \[win)", f"\\g<1>{win_md5}\\3", meta)

    with open("conda-recipe/meta.yaml", "w") as file:
        file.write(meta)


if __name__ == "__main__":
    main()
