import pyodbc 
from datetime import datetime
class newsFeed():
    def __init__(self):
        self.un = 'abc'
        self.pwd = 'scaler'
        self.post_upvotes1 = 0
        self.post_downvotes1 = 0
        self.comment_upvotes1 = 0
        self.comment_downvotes1 = 0
        self.upvotedPost = {}
        self.downvotedPost = {}
        self.upvotedComment = {}
        self.downvotedComment = {}

    def dbConnectionSignUp(self,email_id1,password1,name1):
        
        cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-LAARVRBO;"
                      "Database=scaler23_intermediate;"
                      "Trusted_Connection=yes;")

        
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM dbo.users")
        result_set = cursor.fetchall()
        flag = True
        for row in result_set:
            if(email_id1 in row):
                print('Sorry, email id already exists!')
                flag = False
                break
        if(flag):
            # increment the user_id by 1 every time a new signUp takes place
            cursor.execute("INSERT INTO dbo.users(user_id, user_name, user_email_id, user_password) VALUES(?, ?, ?, ?)", (130, name1, email_id1, password1))
            cnxn.commit()
            print('Sign Up Successful!!!')
            cnxn.close()
        # for row in cursor:
        #     print('row = %r' % (row,))

    def dbConnectionLogin(self, un , pwd):
        
        cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-LAARVRBO;"
                      "Database=scaler23_intermediate;"
                      "Trusted_Connection=yes;")

        
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM dbo.users")
        result_set = cursor.fetchall()
        flag = True
        for row in result_set:
            if(un in row and pwd in row):
                print('Login was successful!')
                flag = False
                break
        if(flag):
            print('Sorry, Credentials are not registered!')

    def dbConnectionPost(self, un, postText):
        cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-LAARVRBO;"
                      "Database=scaler23_intermediate;"
                      "Trusted_Connection=yes;")

        
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM dbo.users")
        result_set = cursor.fetchall()
        flag = True
        for row in result_set:
            if(un in row):
                user_id_post = row[0]
                print(row[0])
                flag = False
                break
        
        if(flag):
            print('Sorry, Credentials are not registered!')
        else:

            #cursor.execute("INSERT INTO dbo.followers(follower_id, user_id, follower_name) VALUES(?, ?, ?)", (0, user_id_post, "None"))
            #---------------- Note: everytime a new post is added by the logged in user, the follower id corresponding to that post is put to 0 always.
            # increment the post_id by 1 every time a new post is written by the logged in user
            cursor.execute("INSERT INTO dbo.posts(post_id, follower_id, user_id, post_upvotes, post_downvotes, post_text, post_timestamp) VALUES(?, ?, ?, ?, ?, ?, ?)", (4, 0, user_id_post, self.post_upvotes1, self.post_downvotes1, postText, datetime.now()))
            cnxn.commit()
            print('Posted successfully!')
            cnxn.close()
    
    def dbConnectionFollow(self, un, followeeName):
        cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-LAARVRBO;"
                      "Database=scaler23_intermediate;"
                      "Trusted_Connection=yes;")

        
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM dbo.users")
        result_set = cursor.fetchall()
        flag = True
        for row in result_set:
            if(un in row):
                user_id_follow = row[0]
                print(row[0])
                flag = False
                break
        
        if(flag):
            print('Sorry, Credentials are not registered!')
        else:
            # increment the follower_id by 1 every time logged in user follows a new user
            cursor.execute("INSERT INTO dbo.followers(follower_id, user_id, follower_name) VALUES(?, ?, ?)", (2, user_id_follow, followeeName))
            cnxn.commit()
            print('Followed successfully!')
            cnxn.close()
    
    def dbConnectionComment(self, un, postID, postComment):
        cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-LAARVRBO;"
                      "Database=scaler23_intermediate;"
                      "Trusted_Connection=yes;")

        
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM dbo.users")
        result_set = cursor.fetchall()
        flag = True
        for row in result_set:
            if(un in row):
                user_id_follow = row[0]
                print(row[0])
                flag = False
                break
        
        if(flag):
            print('Sorry, Credentials are not registered!')
        else:
            # increment the comment_id by 1 every time a new comment is written by the logged in user
            cursor.execute("INSERT INTO dbo.comments(comment_id, post_id, comment_upvotes, comment_downvotes, comment_text, comment_timestamp) VALUES(?, ?, ?, ?, ?, ?)", (1, postID, self.comment_upvotes1, self.comment_downvotes1, postComment, datetime.now()))
            cnxn.commit()
            print('Commented successfully!')
            cnxn.close()
    
    def dbConnectionReply(self, un, commentID, reply):
        cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-LAARVRBO;"
                      "Database=scaler23_intermediate;"
                      "Trusted_Connection=yes;")

        
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM dbo.users")
        result_set = cursor.fetchall()
        flag = True
        for row in result_set:
            if(un in row):
                user_id_follow = row[0]
                print(row[0])
                flag = False
                break
        
        if(flag):
            print('Sorry, Credentials are not registered!')
        else:
            # increment the reply_id by 1 every time a new reply is written by the logged in user
            cursor.execute("INSERT INTO dbo.replies(reply_id, comment_id, reply_text) VALUES(?, ?, ?)", (1, commentID, reply))
            cnxn.commit()
            print('Replied successfully!')
            cnxn.close()
    
    def dbConnectionPostVote(self, un, postID, vote):
        cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-LAARVRBO;"
                      "Database=scaler23_intermediate;"
                      "Trusted_Connection=yes;")

        
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM dbo.users")
        result_set = cursor.fetchall()
        flag = True
        for row in result_set:
            if(un in row):
                user_id_follow = row[0]
                print(row[0])
                flag = False
                break
        
        if(flag):
            print('Sorry, Credentials are not registered!')
        else:
            if(vote == 'U'):
                if(postID in self.upvotedPost):
                    self.upvotedPost[postID] += 1
                else:
                    self.upvotedPost[postID] = 1
                cursor.execute("UPDATE dbo.posts SET post_upvotes = ? where post_id = ?", self.upvotedPost[postID], postID)
                cnxn.commit()
            elif(vote == 'D'):
                if(postID in self.downvotedPost):
                    self.downvotedPost[postID] += 1
                else:
                    self.downvotedPost[postID] = 1
                cursor.execute("UPDATE dbo.posts SET post_downvotes = ? where post_id = ?", self.downvotedPost[postID], postID)
                cnxn.commit()
            print('Post Votes updated successfully!')
            cnxn.close()
    
    def dbConnectionCommentVote(self, un, commentID, vote):
        cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-LAARVRBO;"
                      "Database=scaler23_intermediate;"
                      "Trusted_Connection=yes;")

        
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM dbo.users")
        result_set = cursor.fetchall()
        flag = True
        for row in result_set:
            if(un in row):
                user_id_follow = row[0]
                print(row[0])
                flag = False
                break
        
        if(flag):
            print('Sorry, Credentials are not registered!')
        else:
            if(vote == 'U'):
                if(commentID in self.upvotedComment):
                    self.upvotedComment[commentID] += 1
                else:
                    self.upvotedComment[commentID] = 1
                cursor.execute("UPDATE dbo.comments SET comment_upvotes = ? where comment_id = ?",(self.upvotedComment[commentID], commentID))
                cnxn.commit()
            elif(vote == 'D'):
                if(commentID in self.downvotedComment):
                    self.downvotedComment[commentID] += 1
                else:
                    self.downvotedComment[commentID] = 1
                cursor.execute("UPDATE dbo.comments SET comment_downvotes = ? where comment_id = ?",(self.downvotedComment[commentID], commentID))
                cnxn.commit()
            print('Comment Votes updated successfully!')
            cnxn.close()

    def dbConnectionPostTime(self, un, postID):
        cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-LAARVRBO;"
                      "Database=scaler23_intermediate;"
                      "Trusted_Connection=yes;")

        
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM dbo.users")
        result_set = cursor.fetchall()
        flag = True
        for row in result_set:
            if(un in row):
                user_id_follow = row[0]
                flag = False
                break
        
        if(flag):
            print('Sorry, Credentials are not registered!')
        else:
            cursor.execute("select * from dbo.posts where post_id = ?", postID)
            result_set = cursor.fetchall()
            for row in result_set:
                timestamp1 = row[-1]
                time = timestamp1
                now = datetime.now()
                diff = datetime.now()
                if type(time) is int:
                    diff = now - datetime.fromtimestamp(time)
                elif isinstance(time, datetime):
                    diff = now - time
                elif not time:
                    diff = 0
                second_diff = diff.seconds
                day_diff = diff.days

                if day_diff < 0:
                    print('')
                    return ''

                if day_diff == 0:
                    if second_diff < 10:
                        print("just now")
                        return "just now"
                    if second_diff < 60:
                        print(str(second_diff) + " seconds ago")
                        return str(second_diff) + " seconds ago"
                    if second_diff < 120:
                        print("a minute ago")
                        return "a minute ago"
                    if second_diff < 3600:
                        print(str(second_diff // 60) + " minutes ago")
                        return str(second_diff // 60) + " minutes ago"
                    if second_diff < 7200:
                        print("an hour ago")
                        return "an hour ago"
                    if second_diff < 86400:
                        print(str(second_diff // 3600) + " hours ago")
                        return str(second_diff // 3600) + " hours ago"
                if day_diff == 1:
                    print("Yesterday")
                    return "Yesterday"
                if day_diff < 7:
                    print(str(day_diff) + " days ago")
                    return str(day_diff) + " days ago"
                if day_diff < 31:
                    print(str(day_diff // 7) + " weeks ago")
                    return str(day_diff // 7) + " weeks ago"
                if day_diff < 365:
                    print(str(day_diff // 30) + " months ago")
                    return str(day_diff // 30) + " months ago"
                print(str(day_diff // 365) + " years ago")
                return str(day_diff // 365) + " years ago"
            cnxn.close()

    def dbConnectionCommentTime(self, un, commentID):
        cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-LAARVRBO;"
                      "Database=scaler23_intermediate;"
                      "Trusted_Connection=yes;")

        
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM dbo.users")
        result_set = cursor.fetchall()
        flag = True
        for row in result_set:
            if(un in row):
                user_id_follow = row[0]
                flag = False
                break
        
        if(flag):
            print('Sorry, Credentials are not registered!')
        else:
            cursor.execute("select * from dbo.comments where comment_id = ?", commentID)
            result_set = cursor.fetchall()
            for row in result_set:
                timestamp1 = row[-1]
                time = timestamp1
                now = datetime.now()
                diff = datetime.now()
                if type(time) is int:
                    diff = now - datetime.fromtimestamp(time)
                elif isinstance(time, datetime):
                    diff = now - time
                elif not time:
                    diff = 0
                second_diff = diff.seconds
                day_diff = diff.days

                if day_diff < 0:
                    print('')
                    return ''

                if day_diff == 0:
                    if second_diff < 10:
                        print("just now")
                        return "just now"
                    if second_diff < 60:
                        print(str(second_diff) + " seconds ago")
                        return str(second_diff) + " seconds ago"
                    if second_diff < 120:
                        print("a minute ago")
                        return "a minute ago"
                    if second_diff < 3600:
                        print(str(second_diff // 60) + " minutes ago")
                        return str(second_diff // 60) + " minutes ago"
                    if second_diff < 7200:
                        print("an hour ago")
                        return "an hour ago"
                    if second_diff < 86400:
                        print(str(second_diff // 3600) + " hours ago")
                        return str(second_diff // 3600) + " hours ago"
                if day_diff == 1:
                    print("Yesterday")
                    return "Yesterday"
                if day_diff < 7:
                    print(str(day_diff) + " days ago")
                    return str(day_diff) + " days ago"
                if day_diff < 31:
                    print(str(day_diff // 7) + " weeks ago")
                    return str(day_diff // 7) + " weeks ago"
                if day_diff < 365:
                    print(str(day_diff // 30) + " months ago")
                    return str(day_diff // 30) + " months ago"
                print(str(day_diff // 365) + " years ago")
                return str(day_diff // 365) + " years ago"
            cnxn.close()
        
    def dbConnectionShowNewsFeed(self, un):
        cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-LAARVRBO;"
                      "Database=scaler23_intermediate;"
                      "Trusted_Connection=yes;")

        
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM dbo.users")
        result_set = cursor.fetchall()
        flag = True
        user_id = []
        for row in result_set:
            if(un in row):
                user_id_follow = row[0]
                print("Logged in user id: "+str(row[0])+"")
                flag = False
                break
        
        if(flag):
            print('Sorry, Credentials are not registered!')
        else:
            cursor.execute("select * from dbo.followers where user_id = ?", user_id_follow) 
            result_set = cursor.fetchall()
            for row in result_set:
                if(row[-1] != 'None'):
                    user_id.append(row[-1])
                    print(row)
            
            print('Followers showed successfully!')
            user_id1 = []
            for name in user_id:
                cursor.execute("select * from dbo.users where user_name = ?", name) 
                for row in cursor:
                    user_id1.append(row[0])
            followers_post = []
            print("Posts by followers: ")
            for id in user_id1:
                cursor.execute("select * from dbo.posts where user_id = ?", id)
                for row in cursor:
                    if(row!=None):
                        followers_post.append(list(row))
                        print(list(row))
            print("Posts by non-followers: ")
            nonfollowers_post = []
            cursor.execute("select * from dbo.posts") 
            result_set = cursor.fetchall()
            for row in result_set:
                if(list(row) not in followers_post):
                    nonfollowers_post.append(list(row))
                    print(list(row))
            for k in range(len(followers_post)):
                cursor.execute("select count(*) from dbo.comments where post_id = ?", followers_post[k][0])
                for row in cursor:
                    followers_post[k].append(row[0])
            for k in range(len(followers_post)):
                cursor.execute("select * from dbo.posts where post_id = ?", followers_post[k][0])
                for row in cursor:
                    followers_post[k].append(row[-4]-row[-3])
            followers_post.sort(key = lambda x:x[-3], reverse = True)
            followers_post.sort(key = lambda x:x[-2])
            followers_post.sort(key = lambda x:x[-1], reverse = True)
            for k in followers_post:
                print(k[-4])
                self.dbConnectionPostTime(un, k[0])
            for k in range(len(nonfollowers_post)):
                cursor.execute("select count(*) from dbo.comments where post_id = ?", nonfollowers_post[k][0])
                for row in cursor:
                    nonfollowers_post[k].append(row[0])
            for k in range(len(nonfollowers_post)):
                cursor.execute("select * from dbo.posts where post_id = ?", nonfollowers_post[k][0])
                for row in cursor:
                    nonfollowers_post[k].append(row[-4]-row[-3])
            nonfollowers_post.sort(key = lambda x:x[-3], reverse = True)
            nonfollowers_post.sort(key = lambda x:x[-2])
            nonfollowers_post.sort(key = lambda x:x[-1], reverse = True)
            for k in nonfollowers_post:
                print(k[-4])
                self.dbConnectionPostTime(un, k[0])
    def signUp(self):
        name1 = input("Enter your name for SignUp: ")
        email_id1 = input("Enter your email_id for SignUp: ")
        password1 = input("Enter your password for SignUp: ")
        self.dbConnectionSignUp(email_id1,password1,name1)
    
    def login(self):
        self.un = input("Enter email-id for Login: ")
        self.pwd = input("Enter password for Login: ")
        self.dbConnectionLogin(self.un, self.pwd)

    def login_post(self):
        self.un = input("Enter email-id for Login: ")
        self.pwd = input("Enter password for Login: ")
        self.dbConnectionLogin(self.un, self.pwd)
        postText = input("Enter text for the post: ")
        self.dbConnectionPost(self.un, postText)

    def login_follow(self):
        self.un = input("Enter email-id for Login: ")
        self.pwd = input("Enter password for Login: ")
        self.dbConnectionLogin(self.un, self.pwd)
        followeeName = input("Enter name of person to follow: ")
        self.dbConnectionFollow(self.un, followeeName)

    def login_comment(self):
        self.un = input("Enter email-id for Login: ")
        self.pwd = input("Enter password for Login: ")
        self.dbConnectionLogin(self.un, self.pwd)
        postID = int(input("Enter post ID to comment on: "))
        postComment = input("Enter comment for the post: ")
        self.dbConnectionComment(self.un, postID, postComment)

    def login_reply(self):
        self.un = input("Enter email-id for Login: ")
        self.pwd = input("Enter password for Login: ")
        self.dbConnectionLogin(self.un, self.pwd)
        commentID = int(input("Enter comment ID to comment on: "))
        reply = input("Enter reply for the comment: ")
        self.dbConnectionReply(self.un, commentID, reply)

    def login_post_vote(self):
        self.un = input("Enter email-id for Login: ")
        self.pwd = input("Enter password for Login: ")
        self.dbConnectionLogin(self.un, self.pwd)
        postID = int(input("Enter post ID to vote for: "))
        vote = input("Enter U or D: ")
        self.dbConnectionPostVote(self.un, postID, vote)

    def login_comment_vote(self):
        self.un = input("Enter email-id for Login: ")
        self.pwd = input("Enter password for Login: ")
        self.dbConnectionLogin(self.un, self.pwd)
        commentID = int(input("Enter comment ID to vote for: "))
        vote = input("Enter U or D: ")
        self.dbConnectionCommentVote(self.un, commentID, vote)

    def time_ago_post(self):
        self.un = input("Enter email-id for Login: ")
        self.pwd = input("Enter password for Login: ")
        self.dbConnectionLogin(self.un, self.pwd)
        postID = int(input("Enter post ID to check timestamp for: "))
        self.dbConnectionPostTime(self.un, postID)

    def time_ago_comment(self):
        self.un = input("Enter email-id for Login: ")
        self.pwd = input("Enter password for Login: ")
        self.dbConnectionLogin(self.un, self.pwd)
        commentID = int(input("Enter comment ID to check timestamp for: "))
        self.dbConnectionCommentTime(self.un, commentID)

    def login_showNewsFeed(self):
        self.un = input("Enter email-id for Login: ")
        self.pwd = input("Enter password for Login: ")
        self.dbConnectionLogin(self.un, self.pwd)
        self.dbConnectionShowNewsFeed(self.un)

if __name__=="__main__":
    Q = int(input("Enter number of actions to be performed: "))
    obj = newsFeed()
    for _ in range(Q):
        num = int(input("Enter number from following options: (1 for SignUp; 2 for Login; 3 for Posting; 4 for Following; 5 for Commenting; 6 for Replying; 7 for voting Post; 8 for voting Comment; 9 for post timestamp; 10 for comment timestamp; 11 for show NewsFeed) : "))
        if(num==1):
            obj.signUp()
        elif(num==2):
            obj.login()
        elif(num==3):
            obj.login_post()
        elif(num==4):
            obj.login_follow()
        elif(num==5):
            obj.login_comment()
        elif(num==6):
            obj.login_reply()
        elif(num==7):
            obj.login_post_vote()
        elif(num==8):
            obj.login_comment_vote()
        elif(num==9):
            obj.time_ago_post()
        elif(num==10):
            obj.time_ago_comment()
        elif(num==11):
            obj.login_showNewsFeed()
