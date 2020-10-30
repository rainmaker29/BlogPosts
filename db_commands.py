from app import db,BlogPost
db.create_all()
# print("Initial BlogPosts : ",BlogPost.query().all())
# print("Initial BlogPosts : ",db.session.query().all())
db.session.add(BlogPost(title="BlogPost 1",content="c1",author="a1"))
print("BlogPosts after adding one : ",BlogPost.query().all())
