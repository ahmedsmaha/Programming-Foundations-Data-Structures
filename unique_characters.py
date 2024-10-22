def unique_characters(data):
    unique_data = set(data)
    return len(data) == len(unique_data)

print(unique_characters('sample'))
print(unique_characters('linkedin'))
