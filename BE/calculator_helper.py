import logger

class CalculatorHelper():
    log_properties = {
        'custom_dimensions': {
            'userId': 'amela_music'
        }
    }

    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculatorHelper, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self._user_list = []
            self._current_user = None
            admin = self.User('admin','test1234')
            self._user_list.append(admin)
            self._is_initialized = True
            self.logger = logger.get_logger(__name__)

    class User():
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def __repr__(self):
            return f"User(username={self.username}, password={self.password})"

    def add(self, a, b):
        self.logger.debug(f"Adding {a} and {b}", extra=self.log_properties)
        return a + b

    def subtract(self, a, b):
        self.logger.debug(f"Subtracting {b} from {a}", extra=self.log_properties)
        return a - b

    def multiply(self, a, b):
        self.logger.debug(f"Multiplying {a} by {b}", extra=self.log_properties)
        return a * b

    def divide(self, a, b):
        if b == 0:
            self.logger.error("Attempted to divide by zero", extra=self.log_properties)
            raise ValueError("Cannot divide by zero")
        self.logger.debug(f"Dividing {a} by {b}", extra=self.log_properties)
        return a / b

    def register_user(self, username, password):
        for user in self._user_list:
            if(user.username == username):
                self.logger.info(f"User {username} already exists", extra=self.log_properties)
                return None
        user = self.User(username, password)
        self._user_list.append(user)
        self.logger.info(f"Registered new user {username}", extra=self.log_properties)
        return username

    def login(self, username, password):
        for user in self._user_list:
            if(user.username == username and user.password == password):
                self._current_user = user
                self.logger.info(f"User {username} logged in", extra=self.log_properties)
                return username
        self.logger.info(f"Failed to login for user {username}", extra=self.log_properties)
        return None

    def logout(self):
        user = self._current_user
        self._current_user = None
        self.logger.info(f"User {user.username} logged out", extra=self.log_properties)
        return user

    def get_current_user(self):
        return self._current_user