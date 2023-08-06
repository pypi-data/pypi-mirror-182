# request_content_type_finder

Finds type of requests content in the following cases - 

- content disposition and content type present in response headers
- when none of the above is present, content type is found using file signatures(magic bytes)

### Installation
```bash
pip install request-content-type-finder
```

### Usage
```python
from request_content_type_finder import find
```

```python
find(requests_response)
```

### Contributors

| Name         | Contact             |
|--------------|---------------------|
|Shivam Kadukar|shivamk2802@gmail.com|


