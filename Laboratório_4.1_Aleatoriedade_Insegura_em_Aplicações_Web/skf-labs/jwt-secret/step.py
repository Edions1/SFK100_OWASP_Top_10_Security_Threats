current_time = datetime.datetime.now()
timestamp = current_time.second

to_hash = values[0][1] + str(timestamp)

resetToken = hashlib.sha1(
    to_hash.encode('utf-8')
).hexdigest()




# import hashlib

# username = "admin"

# for second in range(60):
#     to_hash = username + str(second)
#     token = hashlib.sha1(
#         to_hash.encode('utf-8')
#     ).hexdigest()
#     print(second, token)
