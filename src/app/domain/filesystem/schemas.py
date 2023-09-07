from dataclasses import dataclass, field

from typing import Union
from pathlib import Path


@dataclass
class DirObjBase:
    path: Union[Path, str] = field(default=None)

    @property
    def exists(self) -> bool:
        if not self.path.exists():
            return False
        else:
            return True

    def __post_init__(self):
        if not isinstance(self.path, Path):
            self.path = Path(self.path)


@dataclass
class DirObj(DirObjBase):
    pass
