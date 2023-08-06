# django-db-counter

Obtain continuous count.

## Install

```
pip install django-db-counter
```

## Use a shared table to count

```
from django_db_counter.models import DjangoDBCounter


some_id = DjangoDBCounter.get_next("some_keyword")
```

## Use a dedicated table to count

*app/models.py*

```
from django_db_counter.models import DjangoDBCounterBase

class MyCounter(DjangoDBCounterBase):
    default_key = "my_counter_keyword" # default to "default"
```

*app/views.py*

```
from app.models import MyCounter

some_id = MyCounter.get_next()
```


## Releases

### v0.1.0

- First release.
