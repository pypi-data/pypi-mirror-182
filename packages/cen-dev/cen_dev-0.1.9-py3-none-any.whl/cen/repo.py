import os.path

from cookiecutter.main import cookiecutter

from cen import CURRENT_DIR


class Repo:

    def sync(self):
        print('Repo sync xxxxx 2 ' + str(CURRENT_DIR))
        cen_conf_file = os.path.join(CURRENT_DIR, 'cen.json')
        print('cen_conf_file = ' + cen_conf_file)

        cookiecutter('git@gitlab.centra.ai:centra/bundle_template.git', overwrite_if_exists=True)
