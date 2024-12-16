from pathlib import Path

from clld.web.assets import environment

import atlasclld


environment.append_path(
    Path(atlasclld.__file__).parent.joinpath("static").as_posix(), url="/atlasclld:static/"
)
environment.load_path = list(reversed(environment.load_path))
