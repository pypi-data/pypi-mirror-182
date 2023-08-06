from setuptools import setup, find_packages

setup(name='snake_game_mvc',
      version='1.0.0',
      description='MVC Snake game',
      packages=find_packages(),
      install_requires = ['pygame==2.1.2'],
      include_package_data=True,
      package_data={"": ["*.txt", "assets/bg.jpg"]},
      author='ScreamProx',
      author_email='kasperekd7@yandex.ru',
      entry_points={
      "console_scripts": ["snake_game_mvc=snake_game_mvc:__init__"],
      },
      zip_safe=False)
