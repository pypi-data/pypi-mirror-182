
# CLogs

Create Changelogs automatically





## Usage/Examples

### Create new log
```python
import clog

log = clog.Clog()

```
or
```python
import clog

log = clog.Clog("C:\...")

```

### Add entry to log

```python
import clog

log = clog.Clog()

data = LogData("V1.0", "UlifSystems") # LogData(version, contributor)
data.AddEntry("Example Eentry")

log.WriteLog(data)
```

### Get existing log

```python
import clog

log = clog.GetExistingLog("C:\...")

data = LogData("V1.0", "UlifSystems") # LogData(version, contributor)
data.AddEntry("Example Eentry")

log.WriteLog(data)
```

### Delete log

```python
import clog

log = clog.GetExistingLog("C:\...")

clog.DeleteLog("C:\...")
```
## Installation

Install clogs with pip

```bash
  python3 -m pip install clogs
```
    
## License

[MIT](https://choosealicense.com/licenses/mit/)

