# done )
import abc


class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.posts = []
        self.comments = []
        self.shared_content = []
        self.messages_sent = []

    def view_profile(self):
        print(f'Posts: {self.posts}\n Comments: {self.comments} \n Shared content: {self.shared_content}')

    def receive_message(self):
        print(self.messages_sent[-1])


class Post:
    def __init__(self, user: User, post_content: str, date: str):
        self.user = user
        self.content = post_content
        self.date = date


class PhotoPost(Post):
    def __init__(self, user: User, post_content: str, date: str):
        super().__init__(user, post_content, date)
        self.format = 'jpg'

    def pixel_counter(self):
        pass


class TextPost(Post):
    def __init__(self, user: User, post_content: str, date: str):
        super().__init__(user, post_content, date)
        self.max_word_count = 50

    def word_counter(self):
        pass


class Comment:
    def init(self, user: User, comment_content: str, comment_date: str):
        self.user = user
        self.comment_content = comment_content
        self.comment_date = comment_date

    def add_sticker(self):
        print('Sticker')


class SocialMediaSystem(abc.ABC):
    @abc.abstractmethod
    def create_post(self, user: User, post: Post):
        pass

    @abc.abstractmethod
    def share_post(self, user1: User, user2: User, post: Post):
        pass


class Facebook(SocialMediaSystem):

    def create_post(self, user: User, post: Post):
        user.posts.append(post)
        print(f'Successfully created post by the user {user},  at {post.date}, with the content: {post.content}')

    def share_post(self, user1: User, user2: User, post: Post):
        user1.shared_content.append(post)
        print(f'{user2}"s post was shared by {user1}')

    def create_comment(self, user: User, comment: Post):
        user.comments.append(comment)
        print(f"{user}'s {comment.content} was published at {comment.date}")

    def send_message(self, user1: User, user2: User, message: str):
        user1.messages_sent.append(message)
        print('Message was sent!')
