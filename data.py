# Коды ответов
STATUS_OK = 200
STATUS_BAD_REQUEST = 400
STATUS_UNAUTHORIZED = 401
STATUS_FORBIDDEN = 403
STATUS_SERVER_ERROR = 500

# Тексты ошибок
USER_EXISTS_MESSAGE = "User already exists"
REQUIRED_FIELDS_MESSAGE = "Email, password and name are required fields"
INCORRECT_LOGIN_MESSAGE = "email or password are incorrect"
UNAUTHORISED_MESSAGE = "You should be authorised"
NO_INGREDIENTS_MESSAGE = "Ingredient ids must be provided"

# Обязательные поля пользователя
USER_REQUIRED_FIELDS = ["email", "password", "name"]

# Поля, которые можно изменить
USER_UPDATE_FIELDS = ["email", "password", "name"]

# Невалидный хеш ингредиента
INVALID_INGREDIENT_HASH = "123"
