from pathlib import Path
from functools import partial
import shutil

from .template import Template


def match_files(patterns, root=".", apply=None, exclude=None, recursive=False, hidden=False, allow_empty=False):
    """Collects files matching a list of patterns"""
    if len(patterns) == 0 and not allow_empty:
        raise ValueError(f"no patterns or files provided")
    root = Path(root)
    if exclude is None:
        exclude = set()

    result = []
    matched_so_far = set()
    for pattern in patterns:
        anything_matched = False
        matched_total = 0
        matched_files = 0
        for match in (root.rglob if recursive else root.glob)(pattern):
            matched_total += 1
            if match.is_file() and match not in matched_so_far and (hidden or not match.name.startswith(".")):
                matched_so_far.add(match)
                matched_files += 1
                if match not in exclude:
                    if apply is not None:
                        match = apply(match)
                        if match is not None:
                            result.append(match)
                            anything_matched = True
                    else:
                        result.append(match)
                        anything_matched = True

        if not anything_matched:
            raise ValueError(f"pattern '{pattern}' in '{str(root)}' matched 0 files (matched total: {matched_total}, "
                             f"files: {matched_files})")
    return result


def _maybe_template(candidate):
    with open(candidate, 'r') as f:
        result = Template.from_file(f)
    if result.is_trivial():
        return
    return result


match_template_files = partial(match_files, apply=_maybe_template)


def write_grid(name_pattern, stack, files_static, files_grid, root, force_overwrite=False, dry_run=False):
    """Writes grid folder contents"""
    result = []
    root = Path(root)

    def _translate_path(p):
        return Path(name_pattern.format(name=Path(p).relative_to(root)))

    def _missing_dirs(what: Path):
        missing = [what]
        what = what.parent
        while not what.exists():
            missing.append(what)
            what = what.parent
        return missing[::-1]

    for src in files_static:
        dst = _translate_path(src)
        if dst.exists() and not force_overwrite:
            raise FileExistsError(f"file '{dst}' already exists")
        result.extend(_missing_dirs(dst))
        if not dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    for f in files_grid:
        src = f.name
        dst = _translate_path(src)
        if dst.exists() and not force_overwrite:
            raise FileExistsError(f"file or folder '{dst}' already exists")
        result.extend(_missing_dirs(dst))
        if not dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            with open(dst, "w") as ff:
                f.write(stack, ff)
            try:
                shutil.copystat(src, dst)
            except FileNotFoundError:
                pass  # virtual file

    return result
