Simple screen monitoring project

Install requirements
```bash
 pip install -r requirements.txt
```

Start http server
```bash
screenshot_reciever_server.py 127.0.0.1 5432
```

Start screenshot sender
```bash
screenshot_sender.py D:/tmp http://127.0.0.1:5432/upload-screenshot 1200
```