def stream_db_records(db_handler):
    retrived_data = None
    previous_page_size = 10

    try:
        while True:
            # 적어도 한번은 next()를 호출해서 yield 로 움직여야지 send() 메소드를 사용할 수 있다.
            # 적어도 한번 next()를 사용하기 위해서 None을 전달
            page_size = yield retrived_data

            if page_size is None:
                page_size = previous_page_size

            previous_page_size = page_size

            retrived_data = db_handler.read_n_records(page_size)

    except GeneratorExit:
        db_handler.close()

