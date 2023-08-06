""" PYPIPR Module """

"""PYTHON Standard Module"""
import datetime
import zoneinfo
import re
import subprocess
import platform
import pathlib
import urllib.request
import random
import webbrowser
import json
import shutil
import uuid
import time
import threading
import multiprocessing
import os
import timeit
import operator
import asyncio

# import math

_platform_system = platform.system()
WINDOWS = _platform_system == "Windows"
LINUX = _platform_system == "Linux"

if WINDOWS:
    import msvcrt as _getch


"""PYPI Module"""
import colorama
import lxml.html

if LINUX:
    import getch as _getch


colorama.init()


class Pypipr:
    @staticmethod
    def test_print():
        """Print simple text to test this module is working"""
        print("Hello from PyPIPr")


def print_colorize(
    text,
    color=colorama.Fore.GREEN,
    bright=colorama.Style.BRIGHT,
    color_end=colorama.Style.RESET_ALL,
    text_start="",
    text_end="\n",
):
    """Print text dengan warna untuk menunjukan text penting"""
    print(f"{text_start}{color + bright}{text}{color_end}", end=text_end, flush=True)


def log(text):
    """
    Melakukan print ke console untuk menginformasikan proses yg sedang berjalan didalam program.
    """

    def inner_log(func):
        def callable_func(*args, **kwargs):
            print_log(text)
            result = func(*args, **kwargs)
            return result

        return callable_func

    return inner_log


def print_log(text):
    print_colorize(f">>> {text}")


def console_run(command):
    """Menjalankan command seperti menjalankan command di Command Terminal"""
    return subprocess.run(command, shell=True)


def input_char(prompt=None, prompt_ending="", newline_after_input=True):
    """Meminta masukan satu huruf tanpa menekan Enter. Masukan tidak ditampilkan."""
    if prompt:
        print(prompt, end=prompt_ending, flush=True)
    g = _getch.getch()
    if newline_after_input:
        print()
    return g


def input_char_echo(prompt=None, prompt_ending="", newline_after_input=True):
    """Meminta masukan satu huruf tanpa menekan Enter. Masukan akan ditampilkan."""
    if prompt:
        print(prompt, end=prompt_ending, flush=True)
    g = _getch.getche()
    if newline_after_input:
        print()
    return g


def datetime_now(timezone=None):
    """
    Datetime pada timezone tertentu
    """
    if timezone:
        return datetime.datetime.now(zoneinfo.ZoneInfo(timezone))
    else:
        return datetime.datetime.now()


def sets_ordered(iterator):
    """
    Hanya mengambil nilai unik dari suatu list
    """
    return tuple({i: {} for i in iterator}.keys())


def list_unique(iterator):
    """Sama seperti sets_ordered()"""
    return sets_ordered(iterator)


def chunck_array(array, size, start=0):
    """
    Membagi array menjadi potongan-potongan sebesar size
    """
    return tuple(array[i : i + size] for i in range(start, len(array), size))


def regex_multiple_replace(data, regex_replacement_list, flags=0):
    """
    Melakukan multiple replacement untuk setiap list.

    regex_replacement_list = [
        {"regex":r"", "replacement":""},
        {"regex":r"", "replacement":""},
        {"regex":r"", "replacement":""},
    ]
    """
    for v in regex_replacement_list:
        data = re.sub(v["regex"], v["replacement"], data, flags=flags)
    return data


def github_push(commit=None):
    def console(t, c):
        print_log(t)
        console_run(c)

    def console_input(prompt, default):
        print_colorize(prompt, text_end="")
        if default:
            print(default)
            return default
        else:
            return input()

    print_log("Menjalankan Github Push")
    console("Checking files", "git status")
    msg = console_input("Commit Message if any or empty to exit : ", commit)
    if msg:
        console("Mempersiapkan files", "git add .")
        console("Menyimpan files", f'git commit -m "{msg}"')
        console("Mengirim files", "git push")
    print_log("Selesai Menjalankan Github Push")


def github_pull():
    print_log("Git Pull")
    console_run("git pull")


def file_get_contents(filename):
    """
    Membaca seluruh isi file ke memory.
    Apabila file tidak ada maka akan return None.
    Apabila file ada tetapi kosong, maka akan return empty string
    """
    try:
        f = open(filename, "r")
        r = f.read()
        f.close()
        return r
    except:
        return None


def file_put_contents(filename, contents):
    """
    Menuliskan content ke file.
    Apabila file tidak ada maka file akan dibuat.
    Apabila file sudah memiliki content maka akan di overwrite.
    """
    f = open(filename, "w")
    r = f.write(contents)
    f.close()
    return r


def write_file(filename, contents):
    """
    Sama seperti file_put_contents()
    """
    return file_put_contents(filename, str(contents))


def read_file(filename):
    """
    Sama seperti file_get_contents()
    """
    return file_get_contents(filename)


def create_folder(folder_name):
    """
    Membuat folder.
    Membuat folder secara recursive dengan permission.
    """
    pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)


def iscandir(folder_name=".", glob_pattern="*", recursive=True):
    """
    Mempermudah scandir untuk mengumpulkan folder, subfolder dan file
    """
    if recursive:
        return pathlib.Path(folder_name).rglob(glob_pattern)
    else:
        return pathlib.Path(folder_name).glob(glob_pattern)


def scan_folder(folder_name="", glob_pattern="*", recursive=True):
    """
    Hanya mengumpulkan nama-nama folder dan subfolder.
    Tidak termasuk [".", ".."].
    """
    p = iscandir(
        folder_name=folder_name,
        glob_pattern=glob_pattern,
        recursive=recursive,
    )
    return tuple(i for i in p if i.is_dir())


def scan_file(folder_name="", glob_pattern="*", recursive=True):
    """
    Hanya mengumpulkan nama-nama file dalam folder dan subfolder.
    """
    p = iscandir(
        folder_name=folder_name,
        glob_pattern=glob_pattern,
        recursive=recursive,
    )
    return tuple(i for i in p if i.is_file())


def html_get_contents(url, xpath=None, regex=None, css_select=None):
    """
    Mengambil content html dari url.

    Return :
    - String            : Apabila hanya url saja yg diberikan
    - List of etree     : Apabila xpath diberikan
    - False             : Apabila terjadi error
    """
    url_req = urllib.request.Request(
        url=url,
        headers={
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
        },
    )
    url_open = urllib.request.urlopen(url_req)
    try:
        if xpath:
            return lxml.html.parse(url_open).findall(xpath)
        if regex:
            return re.findall(regex, url_open.read().decode())
        if css_select:
            return lxml.html.parse(url_open).getroot().cssselect(css_select)
        return url_open.read().decode()
    except:
        return False


def url_get_contents(url, xpath=None, regex=None, css_select=None):
    """
    Sama seperti html_get_contents()
    """
    return html_get_contents(url, xpath, regex, css_select)


def get_filesize(filename):
    """
    Mengambil informasi file size dalam bytes
    """
    return pathlib.Path(filename).stat().st_size


def get_filemtime(filename):
    """
    Mengambil informasi file size dalam bytes
    """
    return pathlib.Path(filename).stat().st_mtime_ns


def dict_first(d: dict) -> tuple:
    """
    Mengambil nilai (key, value) pertama dari dictionary dalam bentuk tuple
    """
    for k, v in d.items():
        return (k, v)


def random_bool() -> bool:
    """
    Menghasilkan nilai random antara 1 atau 0.
    fungsi ini merupkan fungsi tercepat untuk mendapatkan random bool value
    """
    return random.getrandbits(1)


def run_multiprocessing(*args):
    """
    fungsi ini akan menjalankan fungsi secara bersamaan menggunakan module multiprocessing.
    Kemudian akan menunggu sampai semua selesai dijalankan.
    Kemudian akan mengembalikan nilai setiap fungsi berupa dictionary.
    Tidak bisa dijalankan kalau dari import module, Harus dari main program.
    """

    """
    Aturan:
    - Multiple Argumen berupa tuple(nama_function, dict_kwargs) sebanyak yg diinginkan
    - Setiap function harus memiliki argumen pertama berupa shared memory dictionary,
      untuk memberikan hasil dari proses function
    - Harus dijalankan di dalam scope [if __name__ == "__main__"], untuk menghindari
      proses dijalankan berkali-kali tanpa terkontrol

    contoh penggunaan:

    def gen(x):
        return x * 10

    def pertama(result, **kwargs):
        print(f'pertama {kwargs["number"]}')
        result["pop"] = gen(kwargs["number"])

    def kedua(result, **kwargs):
        print(f'kedua {kwargs["text"]}')
        result["lo"] = gen(kwargs["text"])

    if __name__ == "__main__":
        print(
            run_multiprocessing(
                (pertama, {"number": 55}),
                (pertama, {"number": 11}),
                (kedua, {"text": "ps"}),
                (kedua, {"text": "ad"}),
            )
        )
        print(run_multiprocessing(*((pertama, {"number": i}) for i in range(4))))

    """
    m = multiprocessing.Manager()
    a = tuple(m.dict() for _ in args)

    r = tuple(
        multiprocessing.Process(target=v[0], args=(a[i],), kwargs=v[1])
        for i, v in enumerate(args)
    )

    for i in r:
        i.start()

    for i in r:
        i.join()

    return tuple(x.copy() for x in a)


def set_timeout(interval, func, args=None, kwargs=None):
    """
    menjalankan fungsi ketika sudah sekian detik.
    apabila timeout masih berjalan tapi kode sudah selesai dieksekusi semua,
    maka program tidak akan berhenti sampai timeout selesai, kemudian fungsi dijalankan,
    kemudian program dihentikan.
    """
    t = threading.Timer(interval=interval, function=func, args=args, kwargs=kwargs)
    t.start()
    # t.cancel() untuk menghentikan timer sebelum waktu habis
    return t


def datetime_from_string(iso_string, timezone=datetime.timezone.utc):
    """
    Parse iso string menjadi datetime object dengan timezone UTC
    """
    return datetime.datetime.fromisoformat(iso_string).replace(tzinfo=timezone)


def get_class_method(cls):
    """
    Mengembalikan berupa tuple yg berisi list dari method dalam class
    """
    r = []
    for x in dir(cls):
        if not x.startswith("__") and not x.endswith("__"):
            if callable(g := getattr(cls, x)):
                r.append(g)
    return r


def compare_performance(*args, **kwargs):
    """
    Menjalankan seluruh function dalam list, kemudian membandingkan waktu yg diperlukan.
    Hasil berupa tuple(nama_functions, perbandingan_waktu)
    perbandingan waktu berupa persentase, terkecil berarti tercepat.
    """

    n = kwargs["number"] if "number" in kwargs else 10000
    x = tuple(timeit.timeit(i, number=n) for i in args)
    x_min = min(x)
    r = tuple((f.__name__, int(x[i] / x_min * 100)) for i, f in enumerate(args))
    return sorted(r, key=operator.itemgetter(1))


def run_asyncio(*args):
    """
    Menjalankan beberapa fungsi secara bergantian.
    Kemudian mengembalikan nilai setiap fungsi sesuai urutan.
    """

    """
    Aturan:
    - Fungsi yg dibuat harus menggunakan [async def]
    - Untuk berpindah proses gunakan [await asyncio.sleep(0)]
    - Apabila list fungsi dibuat menggunakan generator, maka gunakan sybol unpack [*]

    Contoh penggunaan:
    
    async def makerandom(idx: int, threshold: int = 6) -> int:
        print(f"Initiated makerandom({idx}).")
        i = random.randint(0, 10)
        while i <= threshold:
            print(f"makerandom({idx}) == {i} too low; retrying.")
            await asyncio.sleep(0)
            i = random.randint(0, 10)
        print(f"---> Finished: makerandom({idx}) == {i}")
        return i

    print(run_asyncio(makerandom(0, 9), makerandom(1, 8), makerandom(2, 7)))
    print(run_asyncio(*(makerandom(i) for i in range(3))))

    """

    async def main(*args):
        return await asyncio.gather(*args)

    return asyncio.run(main(*args))


def run_multithreading(*args):
    """
    fungsi ini akan menjalankan fungsi secara bersamaan menggunakan module multithreading.
    Kemudian akan menunggu sampai semua selesai dijalankan.
    Kemudian akan mengembalikan nilai setiap fungsi berupa dictionary.
    """

    """
    Aturan:
    - Multiple Argumen berupa tuple(nama_function, dict_kwargs) sebanyak yg diinginkan
    - Setiap function harus memiliki argumen pertama berupa dictionary,
      untuk memberikan hasil dari proses function
    - Harus dijalankan di dalam scope [if __name__ == "__main__"], untuk menghindari
      proses dijalankan berkali-kali tanpa terkontrol
      
    contoh penggunaan:

    def gen(x):
        return x * 10

    def pertama(result, **kwargs):
        print(f'pertama {kwargs["number"]}')
        result["pop"] = gen(kwargs["number"])

    def kedua(result, **kwargs):
        print(f'kedua {kwargs["text"]}')
        result["lo"] = gen(kwargs["text"])

    if __name__ == "__main__":
        print(
            run_multithreading(
                (pertama, {"number": 55}),
                (pertama, {"number": 11}),
                (kedua, {"text": "ps"}),
                (kedua, {"text": "ad"}),
            )
        )
        print(run_multithreading(*((pertama, {"number": i}) for i in range(4))))

    """
    a = tuple(dict() for _ in args)

    r = tuple(
        threading.Thread(target=v[0], args=(a[i],), kwargs=v[1])
        for i, v in enumerate(args)
    )

    for i in r:
        i.start()

    for i in r:
        i.join()

    return a
