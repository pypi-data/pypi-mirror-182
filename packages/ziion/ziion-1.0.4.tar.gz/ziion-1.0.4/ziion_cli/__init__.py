import os
from ziion_cli.constants import (
    SOLC_SELECT_DIR,
    ARTIFACTS_DIR,
)

if not os.path.exists(SOLC_SELECT_DIR):
    os.mkdir(path=SOLC_SELECT_DIR)
    os.mkdir(path=ARTIFACTS_DIR)
