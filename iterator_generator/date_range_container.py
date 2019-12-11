from datetime import date, timedelta

class DateRangeContainerIterable:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date

        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)

r1 = DateRangeContainerIterable(date(2019,1,1), date(2019,1,5))
days = ", ".join(map(str, r1))
print(days)

max_day = max(r1)
print(max_day)

class DateRangeSequence:
    def __init__(self, s_date, e_date):
        self.s_date = s_date
        self.e_date = e_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.s_date
        while current_day < self.e_date:
            days.append(current_day)
            current_day += timedelta(days=1)

        return days

    def __getitem__(self, day_no):
        return self._range[day_no]

    def __len__(self):
        return len(self._range)

