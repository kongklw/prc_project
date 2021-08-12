from functools import wraps

READ_PERMISSION = 'READ'
WRITE_PERMISSION = 'WRITE'
EXEC_PERMISSION = 'EXECUTE'


# def get_logined_user():
#     user = {'kong', {'pd': 'konglingwen'}}
#     return user


def permission_required(permission):
    def decorator(func):
        @wraps(func)
        def decorator_function(*args, **kwargs):
            # 获取当前用户
            user = get_logined_user()
            # 判断用户是否存在对应的权限
            if not user or not user.can(permission):
                raise Exception('无权限')

            return func(*args, **kwargs)

        return decorator_function

    return decorator


@permission_required(READ_PERMISSION)
def read_file():
    print('read successfully')


@permission_required(WRITE_PERMISSION)
def write_file():
    print('write successfully'）

@permission_required(RBAC.EXEC_PERMISSION)
def exec_file():
    print('execute successfully')


# Role 角色
VISITOR_TYPE = 'VISITOR'
OPERATOR_TYPE = 'OPERATOR'
MANAGER_TYPE = 'MANAGER'

# 定义角色对应的权限
PERMISSION_MAP = {
    VISITOR_TYPE: {READ_PERMISSION},
    OPERATOR_TYPE: {READ_PERMISSION, WRITE_PERMISSION},
    MANAGER_TYPE: {READ_PERMISSION, WRITE_PERMISSION, EXEC_PERMISSION},
}


# 基础的角色类，提供接口 has() 用于判断角色是否存在特定的权限
class Role:
    @abstractmethod
    def _role_type(self):
        pass

    def has(self, permission):
        return permission in PERMISSION_MAP[self._role_type()]


# 定义角色 VisitorRole，拥有的权限为 [READ_PERMISSION]
class VisitorRole(Role):
    def _role_type(self):
        return VISITOR_TYPE


# 定义角色 OperatorRole，拥有的权限为 [READ_PERMISSION, WRITE_PERMISSION]
class OperatorRole(Role):
    def _role_type(self):
        return OPERATOR_TYPE


# 定义角色 ManagerRole，拥有的权限为 [READ_PERMISSION, WRITE_PERMISSION, EXEC_PERMISSION]
class ManagerRole(Role):
    def _role_type(self):
        return MANAGER_TYPE


class User:
    def __init__(self, name, role=None):
        self._name = name
        self._role = role

    def set_role(self, role):
        self._role = role

    def can(self, permission):
        return self._role and self._role.has(permission)

logined_user = None

# 模拟 web 服务中的登录功能
def login(user):
    global logined_user
    logined_user = user

# 模拟 Web 服务中获取当前用户的功能
def get_logined_user():
    return logined_user

# 创建用户，指定为 OperatorRole，具备 [READ_PERMISSION, WRITE_PERMISSION] 权限
operator_role = OperatorRole()
current_user = User('opt', operator_role)

# 登录用户
login(current_user)

# 写入文件，需要 WRITE_PERMISSION, 用户存在此权限
write_file()

# 执行文件，需要 EXEC_PERMISSION, 用户不存在此权限，报错
exec_file()