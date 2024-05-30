from db import cur, conn
from models import User, UserStatus
from sessions import Session
import utils
import time

session = Session()

def login(username: str, password: str):
    user: Session | None = session.check_session()
    if user:
        return utils.BadRequest('You already logged in', status_code=401)

    get_user_by_username = """SELECT * FROM users WHERE username = %s;"""
    cur.execute(get_user_by_username, (username,))
    user_data = cur.fetchone()
    if not user_data:
        return utils.BadRequest('Username not found')

    _user = User(username=user_data[1], password=user_data[2], role=user_data[3], status=user_data[4], login_try_count=user_data[5])

    if _user.status == UserStatus.BLOCKED.value and time.time() - user_data[5] < 3600:
        return utils.BadRequest('Your account is blocked. Please try again after 1 hour.')

    if password != _user.password:
        update_count_query = """UPDATE users SET login_try_count = login_try_count + 1 WHERE username = %s;"""
        cur.execute(update_count_query, (_user.username,))
        conn.commit()

        if _user.login_try_count >= 2:
            update_status_query = """UPDATE users SET status = %s, login_try_count = %s WHERE username = %s;"""
            cur.execute(update_status_query, (UserStatus.BLOCKED.value, time.time(), _user.username))
            conn.commit()
            return utils.BadRequest('Your account has been blocked for 1 hour due to too many failed login attempts.')

        return utils.BadRequest('Incorrect password')

    _user.login_try_count = 0
    update_count_query = """UPDATE users SET login_try_count = %s WHERE username = %s;"""
    cur.execute(update_count_query, (_user.login_try_count, _user.username))
    conn.commit()

    session.add_session(_user)
    return utils.ResponseData('User successfully logged in')

while True:
    choice = input('Enter your choice: ')
    if choice == '1':
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        login(username, password)
    else:
        break
