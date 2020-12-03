import markdown

from .models import db, Posts, Contact

class DB_Handler:
    class TablePost:
        @staticmethod
        def all_query():
            data = []
            posts = Posts.query.all()
            for post in posts:
                x = {
                    "title": post.title,
                    "body": post.body,
                    "timestamp": post.timestamp,
                    "id": post.id,
                }
                data.append(x)
            return data

        @staticmethod
        def query_by_id(_id):
            post = Posts.query.filter_by(id=_id).first()
            if post is None:
                return {"status": 404, "message": "No id Available"}
            return {
                "title": post.title,
                "body": markdown.markdown(post.body),
                "timestamp": post.timestamp,
                "id": post.id,
            }

        @staticmethod
        def PostData(title, body):
            post = Posts(title=title, body=body)
            db.session.add(post)
            db.session.commit()
            return {"status": 200, "message": "Data Posted sucessfully"}

    class TableContact:
        @staticmethod
        def all_query():
            data = []
            cons = Contact.query.all()
            for con in cons:
                x = {"name": con.name, "email": con.email, "message": con.message}
                data.append(x)
            return data

        @staticmethod
        def PostData(name, email, message):
            con = Contact(name=name, email=email, message=message)
            db.session.add(con)
            db.session.commit()
            return {"status": 200, "message": "Message sended sucessfully"}
