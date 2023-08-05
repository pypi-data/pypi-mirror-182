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


def gen(x):
    return x * 10


def pertama(result, **kwargs):
    print("pertama")
    result["pop"] = gen(kwargs["number"])


def kedua(result, **kwargs):
    print("kedua")
    result["lo"] = gen(kwargs["text"])


if __name__ == "__main__":
    # Tidak bisa dijalankan kalau dari import module, harus dari main program
    x = run_multiprocessing(
        {
            pertama: {"number": 55},
            kedua: {"text": "po"},
        }
    )
    for i in x:
        print(i)

""""""

set_timeout(3, lambda: print("Timeout 3"))
x = set_timeout(7, lambda: print("Timeout 7"))
wait(5)
print("wait 5")
print(x)
print("menghentikan timeout 7")
x.cancel()

""""""
