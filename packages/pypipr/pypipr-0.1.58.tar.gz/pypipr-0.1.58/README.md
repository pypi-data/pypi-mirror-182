# About
The Python Package Index Project (pypipr)

pypi : https://pypi.org/project/pypipr


# Setup
Install with pip
```
python -m pip install pypipr
```

Import with * for fastest access
```
from pypipr.pypipr import *
```


# Functions
`WINDOWS` True apabila berjalan di platform Windows

```python
print(WINDOWS)
```


`LINUX` True apabila berjalan di platform Linux

```python
print(LINUX)
```


`random_bool()` Menghasilkan nilai random antara 1 atau 0

```python
print(random_bool())
```


`set_timeout()` Menjalankan fungsi ketika sudah sekian detik.

```python
set_timeout(3, lambda: print("Timeout 3"))
x = set_timeout(7, lambda: print("Timeout 7"))
print(x)
print("menghentikan timeout 7")
x.cancel()
```


`get_class_method()` Mengembalikan berupa tuple yg berisi list dari method dalam class

```python
class alk:
    def a():
        return [x for x in range(10)]

    def b():
        return [x for x in range(10)]

    def c():
        return [x for x in range(10)]

    def d():
        return [x for x in range(10)]


print(get_class_method(alk))

```


`compare_performance()` Menjalankan seluruh function dalam list, kemudian membandingkan waktu yg diperlukan.

```python
class alk:
    num = 10

    def a():
        return [x for x in range(self.num)]

    def b():
        return [x for x in range(self.num)]

    def c():
        return [x for x in range(self.num)]

    def d():
        return [x for x in range(self.num)]


print(compare_performance(*get_class_method(alk) [, number=10000]))
```


# ASyncIO / MultiThreading / MultiProcessing

`run_asyncio()` Menjalankan program secara bersamanaan dengan bergantian.

```python
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
```


`run_multithreading()` Menjalankan program secara bersamaan menggunakan module multithreading

```python
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
```


`run_multiprocessing()` Menjalankan program secara bersamaan menggunakan module multiprocessing

```python
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
```


`run_asyncio() / run_multithreading() / run_multiprocessing()` Contoh penggunaan kode

```python
# Contoh fungsi biasa
def fun(x):
    return x * 10

# Contoh fungsi dijadikan async
async def afun(x):
    return fun(x)

# Contoh fungsi dijadikan multithreading
def mtfun(result, **kwargs):
    result["mt_ret"] = fun(kwargs["x"])

# Contoh fungsi dijadikan multiprocessing
def mpfun(result, **kwargs):
    result["mp_ret"] = fun(kwargs["x"])

if __name__ == "__main__":
    print(
        run_asyncio(
            afun(11),
            afun("aa"),
        )
    )
    print(
        run_multithreading(
            (mtfun, {"x": 22}),
            (mtfun, {"x": "bb"}),
        )
    )
    print(
        run_multiprocessing(
            (mpfun, {"x": 33}),
            (mpfun, {"x": "cc"}),
        )
    )
```


# Collections

`sets_ordered()` Hanya mengambil nilai unik dari suatu list

```python
array = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]
print([i for i in sets_ordered(array)])
```


`chunck_array()` membagi array menjadi potongan dengan besaran yg diinginkan

```python
array = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]
print([i for i in chunck_array(array, 5)])
```


`dict_first()` Mengambil nilai (key, value) pertama dari dictionary dalam bentuk tuple

```python
d = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}
print(dict_first(d))
```


# Console

`print_colorize()` print ke console dengan warna

```python
print_colorize("Print some text")
print_colorize("Print some text" [, color=colorama.Fore.GREEN])
```


`@Log()` / `Log decorator` akan melakukan print ke console. Mempermudah pembuatan log karena tidak perlu mengubah fungsi yg sudah ada. Berguna untuk memberikan informasi proses program yg sedang berjalan.

```python
@log("Calling some function")
def some_function():
    ...
    return
```


`print_log` akan melakukan print ke console. Berguna untuk memberikan informasi proses program yg sedang berjalan.

```python
print_log("Standalone Log")
```


`input_char()` meminta masukan satu huruf tanpa menekan enter. Char tidak ditampilkan.

```python
input_char("Input Char without print : ")
```


`input_char()` meminta masukan satu huruf tanpa menekan enter. Char ditampilkan.

```python
input_char_echo("Input Char n : ")
```


# Datetime

`datetime_now()` memudahkan dalam membuat tanggal dan waktu untuk suatu timezone

```python
datetime_now("Asia/Jakarta")
datetime_now("GMT")
datetime_now("Etc/GMT+7")
```


`datetime_from_string()` Parse iso_string menjadi datetime object dengan timezone UTC

```python
print(datetime_from_string("2022-12-12 15:40:13").isoformat())
print(datetime_from_string("2022-12-12 15:40:13", timezone="Asia/Jakarta").isoformat())
```


# File and Folder

`file_put_contents()` membuat file kemudian menuliskan contents ke file. Apabila file memiliki contents, maka contents akan di overwrite.

```python
file_put_contents("ifile_test.txt", "Contoh menulis content")
```


`file_get_contents()` membaca contents file ke memory.

```python
print(file_get_contents("ifile_test.txt"))
```


`html_get_contents()` Mengambil content html dari url

```python
# Using XPATH
a = html_get_contents("https://google.com/", xpath="//a")
for i in a:
    print(i.text)
    print(i.attrib.get('href'))

# Using REGEX
a = html_get_contents("https://google.com/", regex=r"(<a.[^>]+>(?:(?:\s+)?(.[^<]+)(?:\s+)?)<\/a>)")
for i in a:
    print(i)

# Using cssselect
a = html_get_contents("https://google.com/", css_select="a")
for i in a:
    print(i.text)
    print(i.attrib.get('href'))
```


`get_filesize()` Mengambil informasi file size dalam bytes

```python
print(get_filesize(__file__))
```


`get_filemtime()` Mengambil informasi last modification time file dalam nano seconds

```python
print(get_filemtime(__file__))
```


`create_folder()` membuat folder secara recursive.

```python
create_folder("contoh_membuat_folder")
create_folder("contoh/membuat/folder/recursive")
create_folder("./contoh_membuat_folder/secara/recursive")
```


`iscandir()` scan folder, subfolder, dan file

```python
for i in iscandir():
    print(i)
```


`scan_folder()` scan folder dan subfolder

```python
for i in scan_folder():
    print(i)
```


`scan_file()` scan file dalam folder dan subfolder

```python
for i in scan_file():
    print(i)
```


`regex_multiple_replace()` Melakukan multiple replacement untuk setiap list regex. 

```python
regex_replacement_list = [
    {"regex": r"\{\{\s*(ini)\s*\}\}", "replacement": r"itu dan \1"},
    {"regex": r"\{\{\s*sini\s*\}\}", "replacement": r"situ"},
]
data = "{{ ini }} adalah ini. {{sini}} berarti kesini."
data = regex_multiple_replace(data, regex_replacement_list, re.IGNORECASE)
print(data)
```


# Third Party

`github_pull()` simple github pull

```python
github_pull()
```


`github_push()` simple github push dengan auto commit message

```python
github_push('Commit Message')
```
