Compile:
```
python3 -m nuitka --standalone --onefile --python-flag=no_site --include-module=service -o microservice.bin main.py
```


* Access API: http://localhost:8181/
* Access Docs (Swagger): http://localhost:8181/docs
* Access Docs (redoc): http://localhost:8181/redoc
* Access "openapi.json": http://localhost:8181/openapi.json
