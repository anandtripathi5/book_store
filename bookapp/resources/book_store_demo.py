from resources.base_resource import BaseResource


class BookStoreDemo(BaseResource):

    def get(self):
        return "welcome to book store"
