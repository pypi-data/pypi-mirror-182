# user-defined exception
class PasswordTooShort(Exception):
    def __init__(self):
        pass

class PasswordTooLong(Exception):
    def __init__(self):
        pass

class User():
    """
    Includes User definition and functions.
    
    Parameters
    ----------
    userCount: count the number of User created
    users: list storing all current users
    usernames: list storing all user names
    """
    
    userCount = 1 
    
    users = [] 

    usernames = []
    
    def __init__(self, user, password):
        """
        Define the class user
        
        Parameters
        ----------
        user: the name of user
        id: the id of user (unique)
        password: personal password for login (private variable)
        """
        if user not in self.usernames:
            self.user = user
            self.id = User.userCount
            self._password = password # password is private 
            #print('Username: {}'.format(self.user))
            User.userCount += 1
            self.users.append(self)
            self.usernames.append(user)
        self.user = user
        
    def displayUser(self):
        """
        Display user info
        
        Returns
        ----------
        The string showing username.
        """
        return f'Username: {self.user}'
        
        # change password
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        # error and exception handler - 5
        try:
            if len(value) < 6:
                raise PasswordTooShort
            elif len(value) > 12:
                raise PasswordTooLong
        except PasswordTooShort:
            print('The password is too short')
        except PasswordTooLong:
            print('The password is too long')
        except:
            print('Other error occurred')
        else:
            self._password = value

# users
user1 = User('madison13g', 'password1')
user2 = User('amethyst1016', 'password2')
user3 = User('khaladhasan', 'khalad1')
user4 = User('jeffandrews', 'jeff1')
user5 = User('christeldeas', 'christel1')
user6 = User('gemarodriguezperez', 'gema1')
user7 = User('ifeomaadaji', 'ifeoma1')
user8 = User('johnthompson', 'john1')
user9 = User('emeliegustafsson', 'emelie1')
user10 = User('patricialassere', 'patricia1')