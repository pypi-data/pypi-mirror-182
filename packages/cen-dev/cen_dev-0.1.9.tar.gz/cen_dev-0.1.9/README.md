# cen-command-line-tool

Консольная утилита cen для внутреннего использования

Основа для работы как command line tool от https://github.com/google/python-fire/


## Deploy

https://johnfraney.ca/blog/create-publish-python-package-poetry/
Заливается в https://pypi.org/ из под tech@centra.ai. Логин пароль у менеджмента в ключнице

```commandline
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry build
poetry publish -u __token__ -p '{TOKEN}'
```