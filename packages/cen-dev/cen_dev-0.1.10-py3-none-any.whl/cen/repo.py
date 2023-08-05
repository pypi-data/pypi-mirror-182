import json
import os.path
from dataclasses import dataclass

from cookiecutter.main import cookiecutter

from cen import CURRENT_DIR


@dataclass
class CenConf:
    app: str
    kind: str


def try_read_cen_conf_file(work_dir: str) -> CenConf:
    """
    Читает файл с описание репозитория
    """
    dir_ = work_dir if work_dir else CURRENT_DIR
    cen_conf_file = os.path.join(dir_, 'cen.json')
    if not os.path.exists(cen_conf_file):
        raise ValueError('Expected cen.json file in root project directory')

    with open(cen_conf_file, 'r') as f:
        return CenConf(json.loads(f.read()))


class Repo:

    def sync(self, work_dir: str = ""):
        """
        :param dir: If empty - current dir
        """
        conf = try_read_cen_conf_file(work_dir)
        print(conf)
        print(str(conf))
        cookiecutter('git@gitlab.centra.ai:centra/bundle_template.git', overwrite_if_exists=True, directory='overwrite')
