from setuptools import setup, find_packages

setup(name='mvc_snake_game',
      version='1.1.8',
      description='MVC Snake game',
      packages=find_packages(),
      install_requires = ['pygame==2.1.2'],
      include_package_data=True,
      package_data={"": ["*.txt", "assets/bg.jpg"]},
      author='AbsoluteZero',
      author_email='kasperekd7@yandex.ru',
      entry_points={
      "console_scripts": ["mvc_snake_game=mvc_snake_game:__init__"],
      },
      zip_safe=False)
