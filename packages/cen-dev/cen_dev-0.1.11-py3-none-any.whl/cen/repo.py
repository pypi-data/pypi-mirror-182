import json
import os.path
from dataclasses import dataclass
from os.path import expanduser
import shutil
from pathlib import Path

from cookiecutter.main import cookiecutter

from cen import CURRENT_DIR


@dataclass
class CenConf:
    app: str
    # kind: str


def try_read_cen_conf_file(dir_: str) -> CenConf:
    """
    Читает файл с описание репозитория
    """
    cen_conf_file = os.path.join(dir_, 'cen.json')
    if not os.path.exists(cen_conf_file):
        raise ValueError('Expected cen.json file in root project directory')

    with open(cen_conf_file, 'r') as f:
        data = json.loads(f.read())
        return CenConf(**data)


class Repo:

    def sync(self, work_dir: str = ""):
        """
        :param dir: If empty - current dir
        """
        dir_ = work_dir if work_dir else CURRENT_DIR
        # user_dir = expanduser("~")
        # clone_dir = os.path.join(user_dir, '.cen', 'clones')

        conf = try_read_cen_conf_file(dir_)

        curr_dir_name = os.path.basename(dir_)

        cookiecutter(
            'git@gitlab.centra.ai:centra/bundle_template.git',
            output_dir=os.path.join(dir_, '..'),
            overwrite_if_exists=True,
            directory='overwrite',
            extra_context={
                'app': conf.app,
                'app_dir': curr_dir_name,
            },
            no_input=True
        )
