# deleting and updating todos

# from db import cur, conn
# from models import User, UserStatus, Todo, TodoType
# from sessions import Session
# import utils

# session = Session()

# def login(username: str, password: str):
#     pass

# def create_todo(title: str, user_id: int, todo_type: TodoType = TodoType.Optional):
#     query = "INSERT INTO todos (name, todo_type, user_id) VALUES (%s, %s, %s)"
#     cur.execute(query, (title, todo_type.value, user_id))
#     conn.commit()
#     return utils.ResponseData(f'Todo "{title}" created successfully.')

# def delete_todo(todo_id: int, user_id: int):
#     query = "DELETE FROM todos WHERE id = %s AND user_id = %s"
#     cur.execute(query, (todo_id, user_id))
#     if cur.rowcount == 0:
#         return utils.BadRequest(f'Todo with ID {todo_id} not found or not belonging to the user.')
#     conn.commit()
#     return utils.ResponseData(f'Todo with ID {todo_id} deleted successfully.')

# def update_todo(todo_id: int, user_id: int, title: str = None, todo_type: TodoType = None):
#     query = "UPDATE todos SET name = COALESCE(%s, name), todo_type = COALESCE(%s, todo_type) WHERE id = %s AND user_id = %s"
#     cur.execute(query, (title, todo_type.value if todo_type else None, todo_id, user_id))
#     if cur.rowcount == 0:
#         return utils.BadRequest(f'Todo with ID {todo_id} not found')
#     conn.commit()
#     return utils.ResponseData(f'Todo with ID {todo_id} updated successfully')

# while True:
#     choice = input('Enter your choice (1. Login, 2. Create Todo, 3. Delete Todo, 4. Update Todo, 5. Exit): ')
#     if choice == '1':
#         login(input('Enter your username: '), input('Enter your password: '))
#     elif choice == '2':
#         create_todo(input('Ente todo title: '), int(input('Enteruser ID: ')), TodoType(input(f'Enter the todo type ({", ".join([t.value for t in TodoType])}): ')))
#     elif choice == '3':
#         delete_todo(int(input('Enter the todo ID: ')), int(input('Enter the user ID: ')))
#     elif choice == '4':
#         todo_id = int(input('Enter todo ID: '))
#         user_id = int(input('Enter user ID: '))
#         title = input('Enter the new title: ')
#         todo_type = input(f'Enter the new todo type ({", ".join([t.value for t in TodoType])}): ')
#         update_todo(todo_id, user_id, title, TodoType(todo_type))
#     else:
#         break



# blocking user part, i've already done this part in the last hometask

# if password != _user.password:
#     update_count_query = """UPDATE users SET login_try_count = login_try_count + 1 WHERE username = %s;"""
#     cur.execute(update_count_query, (_user.username,))
#     conn.commit()

#     if _user.login_try_count >= 2:
#         update_status_query = """UPDATE users SET status = %s, login_try_count = %s WHERE username = %s;"""
#         cur.execute(update_status_query, (UserStatus.BLOCKED.value, time.time(), _user.username))
#         conn.commit()
#         return utils.BadRequest('Your account has been blocked for 1 hour due to too many failed login attempts.')

#     return utils.BadRequest('Incorrect password. Please try again.')
