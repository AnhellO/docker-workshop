import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

print(client["mi-db"].hoomans.insert_many([
    {
        "first_name": "foo",
        "last_name": "bar",
        "email": "foo@mail.com"
    },
    {
        "first_name": "foo",
        "last_name": "baz",
        "email": "baz@mail.com"
    },
    {
        "first_name": "bar",
        "last_name": "baz",
        "email": "bar@mail.com"
    },
    {
        "first_name": "fulano",
        "last_name": "mengano",
        "email": "fulano@mail.com"
    },
    {
        "first_name": "zultano",
        "last_name": "perengano",
        "email": "zultano@mail.com"
    },
]))

