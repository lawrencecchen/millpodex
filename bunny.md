## sqlite

```python
import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("create table if not exists (youtube_id, title, transcript);")
```
