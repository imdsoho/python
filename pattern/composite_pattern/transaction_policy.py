from datetime import datetime

class TransactionalPolicy():
    def __init__(self, policy_dat, **extra_data):
        self._data = {**policy_dat, **extra_data}

    def change_in_policy(selfself, customer_id, **new_policy_data):
        self._data[customer_id].update(**new_policy_data)

    def __getitem__(self, customer_id):
        return self._data[customer_id]

    def __len__(self):
        return len(self._data)

c_1_data = {"client01": {
                            "fee": 1000.0,
                            "expiration_date": datetime(2020,1,3)
                        }
            }

policy = TransactionalPolicy(c_1_data, time_limits="10")
print(policy["client01"])
print(policy["time_limits"])

print(policy.__dict__)
