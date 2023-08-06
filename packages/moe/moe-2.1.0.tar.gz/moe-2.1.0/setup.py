# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['moe',
 'moe.add',
 'moe.duplicate',
 'moe.edit',
 'moe.library',
 'moe.moe_import',
 'moe.move',
 'moe.read',
 'moe.remove',
 'moe.util',
 'moe.util.cli',
 'moe.util.core']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.15,<2.0.0',
 'Unidecode>=1.2.0,<2.0.0',
 'alembic>=1.4.2,<2.0.0',
 'dynaconf>=3.1.4,<4.0.0',
 'mediafile>=0.11.0,<0.12.0',
 'musicbrainzngs>=0.7.1,<0.8.0',
 'pluggy>=0.13.1,<0.14.0',
 'questionary>=1.9.0,<2.0.0',
 'rich>=12.5.1,<13.0.0']

entry_points = \
{'console_scripts': ['moe = moe.cli:main']}

setup_kwargs = {
    'name': 'moe',
    'version': '2.1.0',
    'description': 'The ultimate tool for managing your music library.',
    'long_description': '###############\nWelcome to Moe!\n###############\nMoe is our resident Music-Organizer-Extraordinaire who\'s sole purpose is to give you full control over your music library by streamlining the process between downloading/ripping music to your filesystem and listening to it with your favorite music player.\n\nIn short, Moe maintains a database of your music library that can be updated with various metadata sources, queried, edited, etc. through either an API or command-line interface. All of these features, and more, are made available by a highly extensible plugin ecosystem.\n\nUsage\n=====\nMoe comes with a command-line interface which is how most users will take advantage of the library management features. Below is a screenshot of Moe importing an album from the filesystem and adding it to the underlying database all while fixing tags, relocating the files, and anything else you can imagine.\n\n.. image:: _static/import_example.png\n\nAlternatively, because all the core functionality is available via an API, the underlying music management system can be incorporated into any existing program or other user interface.\n\nFinally, although a lot of Moe\'s functionality exists around the idea of operating on a library database of your music, the database is entirely optional. In this case, Moe provides a convenient set of tools and functionality for handling music in a general sense. For example, below is a standalone python script that takes an album directory and Musicbrainz release ID from the command-line, and then updates the underlying files\' tags with any changes from Musicbrainz (utilizing the ``musicbrainz`` plugin).\n\n.. code:: python\n\n    #!/usr/bin/env python3\n\n    import argparse\n    import pathlib\n\n    from moe.config import Config, ConfigValidationError\n    from moe.library import Album\n    from moe.write import write_tags\n    import moe_musicbrainz\n\n    def main():\n        try:\n            config.Config(config_dir=Path.home() / ".config" / "my_script", init_db=False)\n        except config.ConfigValidationError as err:\n            raise SystemExit(1) from err\n\n        parser = argparse.ArgumentParser(\n            description="Update an album with musicbrainz tags."\n        )\n        parser.add_argument("path", help="dir of the album to update")\n        parser.add_argument("mb_id", help="musicbrainz id of the album to fetch")\n        args = parser.parse_args()\n\n        album = Album.from_dir(pathlib.Path(args.path))\n\n        album.merge(moe_musicbrainz.get_album_by_id(args.mb_id), overwrite=True)\n\n        for track in album.tracks:\n            write_tags(track)\n\n\n    if __name__ == "__main__":\n        main()\n\nThis is just a small taste of what Moe is capable of and how it can make your life easier when dealing with music in Python.\n\nIf you want to learn more, check out the `Getting Started <https://mrmoe.readthedocs.io/en/latest/getting_started.html>`_ docs.\n',
    'author': 'Jacob Pavlock',
    'author_email': 'jtpavlock@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MoeMusic/Moe',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
