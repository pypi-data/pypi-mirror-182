from Content.topic import Topic

class Post(Topic):
    """
    Includes post definition and functions.
    
    Parameters
    ----------
    index: count the number of post created
    posts: list storing all current posts
    """
    
    posts = []
    index = 1
    def __init__(self, topicid, detail, user):
        """
        Define the class post (inheritance Topic)
        
        Parameters
        ----------
        tid: id of topic which this post under
        detail: content of the post
        user: name of user who write this post
        comments: list of comments under this post
        like: number of likes this post has
        pidL id of the post (unique)
        """
        topic = Topic.topics_name[topicid-1]
        self.tid = topicid
        Topic.__init__(self, topic, user='')
        Post.posts.append(self)
        self.detail = detail
        self.user = user
        self.comments = []
        self.like = 0
        self.pid = Post.index
        Post.index += 1
        
    def add_comment(self, comment):
        ## Function to add a comment to a post
        
        # error and exception handler - 2
        try:
            comment = str(comment)
        except TypeError: 
            print('TypeError occurred')
        except:
            print('Other error occurred')
        else:
            self.comments.append(comment)
        
    def add_like(self, num=1):
        # Function to add a like to a post
        # error and exception handler - 3
        try:
            num = int(num)
        except ValueError:
            print('ValueError occurred')
        except:
            print('Other error occurred')
        else:
            self.like += num
        
    def check(self):
        """
        Display post info of likes and comments, by quantity.
        
        Returns
        ----------
        The string showing how many likes and comments this post have.
        """
        return f'This post has {self.like} like and {len(self.comments)} comments.'
    
    def show_post(self):
        """
        Display post info
        
        Returns
        ----------
        The string showing post id, detail, writer and comments or indicating there is no comment under this post.
        """
        print(f'Post id: {self.pid}\n{self.detail} ----- by {self.user}')
        if self.comments:
            print('Comments: ')
            for i in self.comments:
                print(i)
        else:
            print('[Currently no comment.]')
            
    def search_all_post(topicid):
        """
        Display posts under a given topic
        
        Returns
        ----------
        The string showing posts under a given topic or indicating there is no post under the given topic.
        """
        exist = 0
        for i in Post.posts:
            if i.tid == topicid:
                exist = 1
                i.show_post()
                print('·'*20)
        if exist == 0:
            print('[No post under this topic.]')
            
    def search_post(keyword):
        """
        Display post containing a given keyword
        
        Returns
        ----------
        The string showing posts with a given keyword or indicating there is no post containing the given keyword.
        """
        exist = 0
        for i in Post.posts:
            if keyword in i.detail:
                exist = 1
                i.show_post()
                i.check()
                print('·'*20)
        if exist == 0:
            print('[No post with this keyword.]')

# posts
user1 = 'amethyst1016'
post1 = Post(10, 'Winter break starts on December 23rd!', user1)
post1.add_like(num=10)
post1.add_comment('Wow!')
post1.add_comment('Two more weeks to go!')
post2 = Post(8, 'Project step 1 due on December 14th.', user1)
post2.add_like(num=2)
post2.add_comment('Already finished.')
post3 = Post(6, 'Final quiz on December 19th.', 'emeliegustafsson')
post3.add_like(num=4)
post3.add_comment('Test on lecture5 to lecture7 inclusive.')
post4 = Post(2, 'Final quiz on December 21st.','jeffandrews')
post4.add_like(num=3)
post4.add_comment('Includes MCQ and short answers.')
post5 = Post(1, 'Final quiz on December 20th', 'khaladhasan')
post5.add_like(num=6)