from .pypipr import *


""""""

Pypipr.test_print()

""""""

array = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]
print([i for i in sets_ordered(array)])

""""""

array = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]
print([i for i in list_unique(array)])

""""""

array = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]
print([i for i in chunck_array(array, 5)])

""""""

print_colorize("Print Colorize")

""""""


@log("Percobaan print log decorator")
def contoh_fungsi():
    pass


contoh_fungsi()

""""""

print_log("Percobaan print log standalone")

""""""

console_run("ls")
console_run("dir")

""""""

input_char("Input Char tanpa ditampilkan : ")

""""""

input_char_echo("Input Char dengan ditampilkan : ")

""""""

print(f"Is Windows : {WINDOWS}")

""""""

print(f"Is Linux : {LINUX}")

""""""

d = datetime_now()
print(f"Time now                : {d}")
d_jakarta = datetime_now("Asia/Jakarta")
print(f"Timezone Asia/Jakarta   : {d_jakarta}")
d_gmt = datetime_now("GMT")
print(f"Timezone GMT            : {d_gmt}")
d_utc = datetime_now("UTC")
print(f"Timezone UTC            : {d_utc}")
d_universal = datetime_now("Universal")
print(f"Timezone Universal      : {d_universal}")
d_gmt7 = datetime_now("Etc/GMT+7")
print(f"Timezone Etc/GMT+7      : {d_gmt7}")

""""""

file_put_contents("ifile_test.txt", "Contoh menulis content")

""""""

print(file_get_contents("ifile_test.txt"))

""""""

create_folder("contoh_membuat_folder")
create_folder("contoh/membuat/folder/recursive")
create_folder("./contoh_membuat_folder/secara/recursive")

""""""

for i in iscandir(recursive=False):
    print(i)

""""""

if __name__ == "__main__":

    """"""

    for i in scan_folder():
        print(i)

    """"""

    for i in scan_file():
        print(i)

""""""

regex_replacement_list = [
    {"regex": r"\{\{\s*(ini)\s*\}\}", "replacement": r"itu dan \1"},
    {"regex": r"\{\{\s*sini\s*\}\}", "replacement": "situ"},
]
data = "{{ ini }} adalah ini. {{sini}} berarti kesini."
data = regex_multiple_replace(data, regex_replacement_list, re.IGNORECASE)
print(data)

""""""

if __name__ == "__main__":

    """"""

    # print(html_get_contents("https://google.com/"))
    print(r := url_get_contents("https://google.com/"))
    assert r != False

    """"""

    a = html_get_contents("https://animekompi.net/", xpath="//a")
    for i in a:
        print(f"{i.text} : {i.attrib}")

    """"""

    a = html_get_contents(
        "https://animekompi.net/", regex=r"(<a.[^>]+>(?:(?:\s+)?(.[^<]+)(?:\s+)?)<\/a>)"
    )
    for i in a:
        print(i)

    """"""

    a = html_get_contents("https://animekompi.net/", css_select="a")
    for i in a:
        print(f"{i.text} : {i.attrib}")

""""""

print(get_filesize(__file__))

""""""

print(get_filemtime(__file__))

""""""

d = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}
print(dict_first(d))

""""""

print(random_bool())

""""""

set_timeout(1, lambda: print("Timeout 1"))
x = set_timeout(3, lambda: print("Timeout 3"))
time.sleep(2)
print("sleep 2")
print(x)
print("menghentikan timeout 3")
x.cancel()

""""""

print(datetime_from_string("2022-12-12 15:40:13").isoformat())

""""""


class alk:
    def a():
        return [x for x in range(10)]

    def b():
        return [x for x in range(10)]

    def c():
        return [x for x in range(10)]

    def d():
        return [x for x in range(10)]


print(compare_performance(*get_class_method(alk)))

""""""


async def makerandom(idx: int, threshold: int = 6) -> int:
    print(f"Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(0)
        i = random.randint(0, 10)
    print(f"---> Finished: makerandom({idx}) == {i}")
    return i


print(run_asyncio(makerandom(0, 8), makerandom(1, 8), makerandom(2, 8)))
print(run_asyncio(*(makerandom(i, 8) for i in range(3))))

""""""


def gen(x):
    return x * 10


def pertama(result, **kwargs):
    print(f'pertama {kwargs["number"]}')
    result["pop"] = gen(kwargs["number"])


def kedua(result, **kwargs):
    print(f'pertama {kwargs["text"]}')
    result["lo"] = gen(kwargs["text"])


if __name__ == "__main__":
    # Tidak bisa dijalankan kalau dari import module, harus dari main program
    print(
        *run_multiprocessing(
            (pertama, {"number": 55}),
            (pertama, {"number": 11}),
            (kedua, {"text": "ps"}),
            (kedua, {"text": "ad"}),
        )
    )
    print(*run_multiprocessing(*((pertama, {"number": i}) for i in range(4))))


""""""


if __name__ == "__main__":
    # Tidak bisa dijalankan kalau dari import module, harus dari main program
    print(
        run_multithreading(
            (pertama, {"number": 55}),
            (pertama, {"number": 11}),
            (kedua, {"text": "ps"}),
            (kedua, {"text": "ad"}),
        )
    )
    print(run_multithreading(*((pertama, {"number": i}) for i in range(4))))


""""""
