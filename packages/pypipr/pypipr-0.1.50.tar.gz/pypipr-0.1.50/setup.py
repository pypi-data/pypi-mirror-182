# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypipr']

package_data = \
{'': ['*']}

install_requires = \
['colorama', 'cssselect', 'lxml', 'tzdata']

extras_require = \
{':platform_system == "Linux"': ['getch']}

setup_kwargs = {
    'name': 'pypipr',
    'version': '0.1.50',
    'description': 'The Python Package Index Project',
    'long_description': '# About\nThe Python Package Index Project (pypipr)\n\n\npypi : https://pypi.org/project/pypipr\n\n\n\n# Setup\nInstall with pip\n```\npython -m pip install pypipr\n```\n\nImport with * for fastest access\n```\nfrom pypipr.pypipr import *\n```\n\nTest with\n```python\nPypipr.test_print()\n```\n\n\n# Pypipr Class\n`test_print()` memastikan module sudah terinstal dan dapat dijalankan\n\n```python\nPypipr.test_print()\n```\n\n\n# functions\n`sets_ordered()` Hanya mengambil nilai unik dari suatu list\n\n```python\narray = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]\nprint([i for i in sets_ordered(array)])\n```\n\n\n`list_unique()` sama seperti `sets_ordered()`\n\n```python\narray = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]\nprint([i for i in list_unique(array)])\n```\n\n\n`chunck_array()` membagi array menjadi potongan dengan besaran yg diinginkan\n\n```python\narray = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]\nprint([i for i in chunck_array(array, 5)])\n```\n\n\n`print_colorize()` print ke console dengan warna\n\n```python\nprint_colorize("Print some text")\n```\n\n\n`@Log()` / `Log decorator` akan melakukan print ke console. Mempermudah pembuatan log karena tidak perlu mengubah fungsi yg sudah ada. Berguna untuk memberikan informasi proses program yg sedang berjalan.\n\n```python\n@log("Calling some function")\ndef some_function():\n    ...\n    return\n```\n\n\n`print_log` akan melakukan print ke console. Berguna untuk memberikan informasi proses program yg sedang berjalan.\n\n```python\nprint_log("Standalone Log")\n```\n\n\n`input_char()` meminta masukan satu huruf tanpa menekan enter. Char tidak ditampilkan.\n\n```python\ninput_char("Input Char without print : ")\n```\n\n\n`input_char()` meminta masukan satu huruf tanpa menekan enter. Char ditampilkan.\n\n```python\ninput_char_echo("Input Char n : ")\n```\n\n\n`datetime_now()` memudahkan dalam membuat tanggal dan waktu untuk suatu timezone\n\n```python\ndatetime_now("Asia/Jakarta")\ndatetime_now("GMT")\ndatetime_now("Etc/GMT+7")\n```\n\n\n`WINDOWS` True apabila berjalan di platform Windows\n\n```python\nprint(WINDOWS)\n```\n\n\n`LINUX` True apabila berjalan di platform Linux\n\n```python\nprint(LINUX)\n```\n\n\n`file_put_contents()` membuat file kemudian menuliskan contents ke file. Apabila file memiliki contents, maka contents akan di overwrite.\n\n```python\nfile_put_contents("ifile_test.txt", "Contoh menulis content")\n```\n\n\n`file_get_contents()` membaca contents file ke memory.\n\n```python\nprint(file_get_contents("ifile_test.txt"))\n```\n\n\n\n`write_file()` sama seperti `file_put_contents()`\n\n```python\nwrite_file("ifile_test.txt", "Contoh menulis content")\n```\n\n\n`read_file()` Sama seperti `file_get_contents()`\n\n```python\nprint(file_get_contents("ifile_test.txt"))\n```\n\n\n`create_folder()` membuat folder secara recursive.\n\n```python\ncreate_folder("contoh_membuat_folder")\ncreate_folder("contoh/membuat/folder/recursive")\ncreate_folder("./contoh_membuat_folder/secara/recursive")\n```\n\n\n`iscandir()` scan folder, subfolder, dan file\n\n```python\nfor i in iscandir():\n    print(i)\n```\n\n\n`scan_folder()` scan folder dan subfolder\n\n```python\nfor i in scan_folder():\n    print(i)\n```\n\n\n`scan_file()` scan file dalam folder dan subfolder\n\n```python\nfor i in scan_file():\n    print(i)\n```\n\n\n`regex_multiple_replace()` Melakukan multiple replacement untuk setiap list regex. \n\n```python\nregex_replacement_list = [\n    {"regex": r"\\{\\{\\s*(ini)\\s*\\}\\}", "replacement": r"itu dan \\1"},\n    {"regex": r"\\{\\{\\s*sini\\s*\\}\\}", "replacement": r"situ"},\n]\ndata = "{{ ini }} adalah ini. {{sini}} berarti kesini."\ndata = regex_multiple_replace(data, regex_replacement_list, re.IGNORECASE)\nprint(data)\n```\n\n\n`github_push()` simple github push dengan auto commit message\n\n```python\ngithub_push(\'Commit Message\')\n```\n\n\n`github_pull()` simple github pull\n\n```python\ngithub_pull()\n```\n\n\n`html_get_contents()` Mengambil content html dari url\n\n```python\n# Using XPATH\na = html_get_contents("https://google.com/", xpath="//a")\nfor i in a:\n    print(i.text)\n    print(i.attrib.get(\'href\'))\n\n# Using REGEX\na = html_get_contents("https://google.com/", regex=r"(<a.[^>]+>(?:(?:\\s+)?(.[^<]+)(?:\\s+)?)<\\/a>)")\nfor i in a:\n    print(i)\n\n# Using cssselect\na = html_get_contents("https://google.com/", css_select="a")\nfor i in a:\n    print(i.text)\n    print(i.attrib.get(\'href\'))\n\n```\n\n\n`get_filesize()` Mengambil informasi file size dalam bytes\n\n```python\nprint(get_filesize(__file__))\n```\n\n\n`get_filemtime()` Mengambil informasi last modification time file dalam nano seconds\n\n```python\nprint(get_filemtime(__file__))\n```\n\n\n`dict_first()` Mengambil nilai (key, value) pertama dari dictionary dalam bentuk tuple\n\n```python\nd = {\n    "key1": "value1",\n    "key2": "value2",\n    "key3": "value3",\n}\nprint(dict_first(d))\n```\n\n\n`random_bool()` Menghasilkan nilai random antara 1 atau 0\n\n```python\nprint(random_bool())\n```\n\n\n`run_multiprocessing()` Menjalankan program secara bersamaan\n```python\ndef gen(x):\n    return x * 10\n\ndef pertama(result, **kwargs):\n    print("pertama")\n    result["pop"] = gen(kwargs["number"])\n\ndef kedua(result, **kwargs):\n    print("kedua")\n    result["lo"] = gen(kwargs["text"])\n\nif __name__ == "__main__":\n    x = run_multiprocessing(\n        {\n            pertama: {"number": 55},\n            kedua: {"text": "po"},\n        }\n    )\n    for i in x:\n        print(i)\n```\n\n\n`set_timeout()` Menjalankan fungsi ketika sudah sekian detik.\n\n```python\nset_timeout(3, lambda: print("Timeout 3"))\nx = set_timeout(7, lambda: print("Timeout 7"))\nprint(x)\nprint("menghentikan timeout 7")\nx.cancel()\n```\n\n\n`wait()` Menunda kode program untuk menyelesaikan kode sebelumnya sampai beberapa waktu.\n\n```python\nwait(5)\nprint("wait 5")\n```\n',
    'author': 'ufiapjj',
    'author_email': 'ufiapjj@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
