class CustomException(Exception):
    pass


def stream_db_records(db_handler):
    try:
        while True:
            yield db_handler.read_n_records(10)
    except CustomException as e:
        print("Exception Process %r ", e)
    except Exception:
        print("Exception Process %r ", e)
        db_handler.close()


steamer = stream_db_records(DBHander("testdb"))
next(steamer)

steamer.throw(CustomException)

streamer.throw(RuntimeError)
