from datetime import datetime, timedelta

'''class Bucket(object):
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return 'Bucket(quota=%d)' % self.quota
'''

# Example 7
class Bucket(object):
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)   # 1분
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return ('Bucket(max_quota=%d, quota_consumed=%d)' %
                (self.max_quota, self.quota_consumed))

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        print("max_quote ", self.max_quota)
        print("amount ", amount)
        print("delta ", delta)

        if amount == 0:
            # 새 기간의 할당량을 리셋함
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # 새 기간의 할당량을 채움
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            # 기간 동안 할당량을 소비함
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta

#bucket = Bucket(60)
#print(bucket)

# Example 2
def fill(bucket, amount):
    print("fill : ", amount)
    now = datetime.now()

    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount


# Example 3
def deduct(bucket, amount):
    print("deduct : ", amount)

    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False

    if bucket.quota - amount < 0:
        return False

    print(">>",  bucket.quota, " : ", amount)
    bucket.quota -= amount
    return True

bucket = Bucket(60)
fill(bucket, 100)
print(bucket)
print("------------")
deduct(bucket, 70)
print(bucket)
print("------------")
deduct(bucket, 40)
print('Still', bucket)



'''bucket = Bucket(60)
print('Initial', bucket)

fill(bucket, 100)
print('Filled', bucket)

u_amt = 99
if deduct(bucket, u_amt):
    print('Had %s quota' % u_amt)
else:
    print('Not enough for %s quota' % u_amt)

print('Now', bucket)

a_amt = 3
if deduct(bucket, a_amt):
    print('Had %s quota' % a_amt)
else:
    print('Not enough for %s quota' % a_amt)

print('Still', bucket)'''