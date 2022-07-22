# Spark standalone

### Skills and tools:
`PySpark`, `PyTest`, `Poetry`, `Wheel`, `Quinn`

---
### Task: Create PySpark project with Poetry DMS:
  * Build project with Poetry (DMS) *Dependency Management System*
  * Add *Quinn* package to project with *Poetry*
  * Create and run tests to verify proper installation and work of *PySpark* and *Quinn* packages
  * Package PySpark project as wheel files


---
###  Work progress: 
1) [*Installing Poetry*][1]

2) Creating project with *Poetry* dependency management for Python

```shell
poetry new Spark_Poetry
```

2) Adding *PySpark* to project
```shell
poetry add pyspark
```
3) Set idea python interpreter as poetry & set path:
```shell
/home/vt/.cache/pypoetry/virtualenvs/spark-standalone-RRWaD6iA-py3.10/bin/python3.10
```
4) install *Python Distutils* for poetry dependencies update
```shell
sudo apt-get install python3.10-distutils

```
5) [*Creating Spark session*][2]
6) [*Creating Dataframe file to transform*][3]
7) [*Creating PyTest for transformation file*][4]
8) Executing first test:

```shell
PASSED  [100%]

+----+---+
|name|age|
+----+---+
|jose|  1|
|  li|  2|
+----+---+

+----+---+---------+
|name|age|Greetings|
+----+---+---------+
|jose|  1|   hello!|
|  li|  2|   hello!|
+----+---+---------+
```

9) Adding Quinn dependency to project:
```shell
poetry add quinn
```
10) Creating second test with new DataFrame that contain non-word characters. 
With use of quinn.remove_non_word_characters() function we will remove non-word characters.

11) Executing second test:
```shell
PASSED [100%]

+----------+------+
|first_name|letter|
+----------+------+
|    jo&&se|     a|
|      ##li|     b|
|   !!sam**|     c|
+----------+------+

+----------+------+----------------+
|first_name|letter|Clean_first_name|
+----------+------+----------------+
|    jo&&se|     a|            jose|
|      ##li|     b|              li|
|   !!sam**|     c|             sam|
+----------+------+----------------+
```
12) Specify package name in *pyproject.toml*
```shell
packages = [
    { include = "Spark_Poetry" }
]
```
13) Package wheel file
```shell
poetry build

>>> Building Spark_Poetry (0.1.0)
  - Building sdist
  - Built Spark_Poetry-0.1.0.tar.gz
  - Building wheel
  - Built Spark_Poetry-0.1.0-py3-none-any.whl

```

[1]: https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions
[2]: https://github.com/Amboss/Spark_Poetry/blob/master/Spark_Poetry/sparksession.py
[3]: https://github.com/Amboss/Spark_Poetry/blob/master/Spark_Poetry/transformation.py
[4]: https://github.com/Amboss/Spark_Poetry/blob/master/tests/test_transformations.py
