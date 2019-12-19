def stream_db_records(db_handler):
    try:
        while True:
            yield db_handler.read_n_records(10)
    except GeneratorExit:
        db_handler.close()

steamer = stream_db_records(DBHander("testdb"))
next(steamer)

next(steamer)

steamer.close()

