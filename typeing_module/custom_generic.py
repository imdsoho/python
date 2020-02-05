from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):
#class LoggedVar(T):        # ERROR - Sub Class를 생성하지 못함
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)

from typing import Iterable
#def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
def zero_all_vars(vars):
    for var in vars:
        var.set(0)

logger = Logger('typing_code_logger')
a_vars = LoggedVar('1', '/', logger)
b_vars = LoggedVar('2', '/index', logger)
c_vars = LoggedVar('3', '/main', logger)

log_vars = [a_vars, b_vars, c_vars]
for log in log_vars:
    print(log.get())

zero_all_vars(log_vars)

for log in log_vars:
    print(log.get())
