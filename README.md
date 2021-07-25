zype-python
===========

A simple wrapper around Zype API. 
This wrapper is used in [Airflow Zype Provider](https://github.com/Dminor7/airflow-provider-zype)
It is really easy to use it. To illustrate, in order to get all videos from your account, you can simply do:

```python
from zype import Zype

client = Zype(api_key="<YOUR_API_KEY>")

videos = client.list_videos().get()
video_data = [video().data for video in videos().pages()]
```

```python
from zype import Zype

client = Zype(api_key="<YOUR_API_KEY>")

videos = client.list_videos().get()
for video in videos().pages(max_items=10):
        print(video.title().data)
```

Open documentation
```python
videos = client.list_videos().open_docs()
```
Change api root to *analytics*

```python
client = Zype(api_key=api_key, api_root="https://analytics.zype.com")
stream_hours = client.list_stream_hours().get()
print(stream_hours().data)
```

Supported resources

```python
dir(client) # ['list_consumers', 'list_stream_hours', 'list_subscriptions', 'list_videos']
```

Installation
------------

`$ pip install -U git+https://github.com/Dminor7/zype-python.git`


License
-------

The project is licensed under the Apache License 2.0 license.
