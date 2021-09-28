from .crud import CrudInterface


class UserRepoError(Exception):
    pass


class UserRepoInterface(CrudInterface):
    def add_user(self, user):
        """
        Adds a user to the repo. Then, after 1 minute, sends him/her a welcome email
        If not possible, raises a UserRepoError
        """
        raise NotImplementedError

    def get_email_by_uuid(self, uuid):
        """

        :param uuid:
        """