# About
The Python Package Index Project (pypipr)

pypi : https://pypi.org/project/pypipr


# Setup
Install with pip
```
python -m pip install pypipr
```

Import with * for fastest access
```python
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


`get_class_method()` Mengembalikan berupa tuple yg berisi list dari method dalam class

```python
class CustomClass:
    def a():
        return [x for x in range(10)]

    def b():
        return [x for x in range(10)]

    def c():
        return [x for x in range(10)]

    def d():
        return [x for x in range(10)]


if __name__ == "__main__":
    print(get_class_method(CustomClass))
```


# Compare Performance

`class ComparePerformance` Menjalankan seluruh method dalam class, kemudian membandingkan waktu yg diperlukan.

```python
class CustomClass(ComparePerformance):
    z = 10

    def a(self):
        return (x for x in range(self.z))

    def b(self):
        return tuple(x for x in range(self.z))

    def c(self):
        return [x for x in range(self.z)]

    def d(self):
        return list(x for x in range(self.z))


if __name__ == "__main__":
    print(CustomClass().compare_result())
    print(CustomClass().compare_performance())
    print(CustomClass().compare_performance())
    print(CustomClass().compare_performance())
    print(CustomClass().compare_performance())
    print(CustomClass().compare_performance())
```


# Run Parallel

`class RunParalel` Menjalankan program secara bersamaan

```python
class CustomClass(RunParallel):
    z = "ini"

    def __init__(self) -> None:
        self.pop = random.randint(0, 100)

    def a(self, result):
        result["z"] = self.z
        result["pop"] = self.pop
        result["a"] = "a"

    def b(self, result):
        result["z"] = self.z
        result["pop"] = self.pop
        result["b"] = "b"

    def c(self, result):
        result["z"] = self.z
        result["pop"] = self.pop
        result["c"] = "c"

    async def d(self):
        print("hello")
        await asyncio.sleep(0)
        print("hello")

        result = {}
        result["z"] = self.z
        result["pop"] = self.pop
        result["d"] = "d"
        return result

    async def e(self):
        print("world")
        await asyncio.sleep(0)
        print("world")

        result = {}
        result["z"] = self.z
        result["pop"] = self.pop
        result["e"] = "e"
        return result


if __name__ == "__main__":
    print(CustomClass().run_asyncio())
    print(CustomClass().run_multi_threading())
    print(CustomClass().run_multi_processing())
```


# Collections

`sets_ordered()` Hanya mengambil nilai unik dari suatu list

```python
array = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]
print(sets_ordered(array))
```


`chunck_array()` membagi array menjadi potongan dengan besaran yg diinginkan

```python
array = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]
print(chunck_array(array, 5))
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
print_colorize("Print some text", color=colorama.Fore.RED)
```


`@Log()` / `Log decorator` akan melakukan print ke console. Mempermudah pembuatan log karena tidak perlu mengubah fungsi yg sudah ada. Berguna untuk memberikan informasi proses program yg sedang berjalan.

```python
@log("Calling some function")
def some_function():
    ...
    return

if __name__ == "__main__":
    some_function()
```


`print_log` akan melakukan print ke console. Berguna untuk memberikan informasi proses program yg sedang berjalan.

```python
print_log("Standalone Log")
```


`input_char()` meminta masukan satu huruf tanpa menekan enter. Char tidak ditampilkan.

```py
input_char("Input Char without print : ")
```


`input_char()` meminta masukan satu huruf tanpa menekan enter. Char ditampilkan.

```py
input_char_echo("Input Char: ")
```


# Datetime

`datetime_now()` memudahkan dalam membuat tanggal dan waktu untuk suatu timezone

```python
print(datetime_now("Asia/Jakarta"))
print(datetime_now("GMT"))
print(datetime_now("Etc/GMT+7"))
```


`datetime_from_string()` Parse iso_string menjadi datetime object dengan timezone UTC

```python
print(datetime_from_string("2022-12-12 15:40:13").isoformat())
print(datetime_from_string("2022-12-12 15:40:13", timezone="Asia/Jakarta").isoformat())
```


# File and Folder

`file_put_contents()` membuat file kemudian menuliskan contents ke file. Apabila file memiliki contents, maka contents akan di overwrite.

```py
file_put_contents("ifile_test.txt", "Contoh menulis content")
```


`file_get_contents()` membaca contents file ke memory.

```py
print(file_get_contents("ifile_test.txt"))
```


`html_get_contents()` Mengambil content html dari url

```python
print(html_get_contents("https://arbadzukhron.deta.dev/"))
```
```py
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

```py
create_folder("contoh_membuat_folder")
create_folder("contoh/membuat/folder/recursive")
create_folder("./contoh_membuat_folder/secara/recursive")
```


`iscandir()` scan folder, subfolder, dan file

```py
for i in iscandir():
    print(i)
```


`scan_folder()` scan folder dan subfolder

```python
for i in scan_folder():
    print(i)
```


`scan_file()` scan file dalam folder dan subfolder

```py
for i in scan_file():
    print(i)
```


# Third Party

`github_pull()` simple github pull

```python
github_pull()
```


`github_push()` simple github push dengan auto commit message

```py
github_push('Commit Message')
```
