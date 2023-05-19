from datetime import datetime, timezone
from create_bot import collection


def err(mess):
    print(f'❗️Error except: {mess}')
    return False


def check_null(search):
    if search != None:
        return True
    else:
        return False


def set_date():
    return datetime.now(tz=timezone.utc).replace(tzinfo=None).replace(second=0, microsecond=0)


async def create_applications(user_id, username, firstname, fullname, lastname):
    try:
        search = await collection.bot_applications.find_one({"telegramId": user_id})

        if (search == None):
            date = set_date()
            search = await collection.bot_applications.insert_one({
                "telegramId": user_id,
                "username": username,
                "firstname": firstname,
                "fullname": fullname,
                "lastname": lastname,
                "date": date
            })

        return check_null(search)

    except:
        err('create_applications')
