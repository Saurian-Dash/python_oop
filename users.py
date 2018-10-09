import datetime as dt

company = 'Secret Escapes'

class User:

    def __init__(self, 
                first_name, 
                last_name, 
                user_type):

        now = dt.datetime.timestamp(dt.datetime.now())

        self.user_id      = int(now)
        self.first_name   = first_name
        self.last_name    = last_name
        self.user_type    = user_type
        self.date_created = now


    def __repr__(self):

        return f'User({self.first_name}, {self.last_name}, {self.user_type})'


    def __str__(self):

        return f'User ID: {self.user_id} | User Name: {self.user_name} | Created at: {self.date_created}'


    @property
    def user_name(self):

        return f'{self.first_name}_{self.last_name}'.lower()


    @property
    def email(self):

        company_text = company.replace(' ', '').lower()
        return f'{self.first_name}.{self.last_name}@{company_text}.com'


    @classmethod
    def from_string(cls, user_str, delimiter):

        first_name, \
        last_name,  \
        user_type   \
        = user_str.split(delimiter)

        return cls(first_name,
                    last_name,
                    user_type)


class Developer(User):

    def __init__(self, 
                first_name, 
                last_name,
                prog_lang):

        super().__init__(first_name, 
                        last_name, 
                        user_type='Developer')

        self._prog_lang = []
        self._prog_lang.append(prog_lang)


    @property
    def prog_lang(self):

        return self._prog_lang


    def add_prog_lang(self, new_lang):

        self.prog_lang.append(new_lang)


user_01 = Developer('Carol', 'Danvers', 'Binary')

print(user_01)
print(user_01.prog_lang)
print(user_01.__repr__())

user_02 = User.from_string('Barry,Allen,Admin', ',')
print(user_02)

# Need to move date_created from base Class into instance
