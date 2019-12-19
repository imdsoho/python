def stream_db_records(db_handler):
    retrived_data = None
    page_size = 10

    try:
        while True:
            page_size = (yield retrived_data) or page_size
            retrived_data = db_handler.read_n_records(page_size)

    except GeneratorExit:
        db_handler.close()

