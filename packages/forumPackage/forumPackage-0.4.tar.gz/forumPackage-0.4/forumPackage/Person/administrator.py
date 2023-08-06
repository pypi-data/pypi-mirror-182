from .user import User

class Admin(User):
    """
    Includes Administrator definition and functions.
    
    Parameters
    ----------
    admins: list storing all administrators
    """
    
    admins = []
    
    def __init__(self, user, password, admincode):
        """
        Define the class administrator (inheritance User)
        
        Parameters
        ----------
        amincode: like administrator id (unique)
        """
        User.__init__(self, user, password)
        self.admincode = admincode
        Admin.admins.append(self)
        
    def displayUser(self):
        """
        Display administrator info
        
        Returns
        ----------
        The string showing username and admincode.
        """
        return f'{User.displayUser(self)} Admin code: {self.admincode}'
        
    # check number of users
    def displayCount(self):
        """
        Display the number of current users
        
        Returns
        ----------
        The string showing the number of current users.
        """
        return f'There are {len(User.users)} users'
    
    # print list of current users
    def userlist(self):
        """
        Display all user info
        
        Returns
        ----------
        The string showing all users' id and username.
        """
        # error and exception handler - 6
        try:
            for i in User.users:
                print("Userid: {} Username: {}".format(i.id, i.user))
        except IndexError:
            print('IndexError occurred')
        except:
            print('Other error occurred')
            
# administrators
admin1 = Admin('Dan', 'password3', 'A1')
admin2 = Admin('Amethyst', 'password4', 'A2')
admin3 = Admin('Madison', 'password5', 'A3')
admin4 = Admin('Abigail', 'password6', 'A4')
admin5 = Admin('Linda', 'password7', 'A5')
admin6 = Admin('Tom', 'password8', 'A6')