import markdown

from .models import db, Posts, Contact, Portfolio


class DB_Handler:
    """
    Class for direct interaction with database
    """

    class TablePost:
        @staticmethod
        def all_query() -> list:
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
        def query_by_id(_id) -> dict:
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
        def all_title() -> list:
            return [i["title"] for i in DB_Handler.TablePost.all_query()]

        @staticmethod
        def PostData(title, body) -> dict:
            post = Posts(title=title, body=body)
            db.session.add(post)
            db.session.commit()
            return {"status": 200, "message": "Data Posted sucessfully"}

    class TableContact:
        @staticmethod
        def all_query() -> list:
            data = []
            cons = Contact.query.all()
            for con in cons:
                x = {"name": con.name, "email": con.email, "message": con.message}
                data.append(x)
            return data

        @staticmethod
        def PostData(name, email, message) -> dict:
            con = Contact(name=name, email=email, message=message)
            db.session.add(con)
            db.session.commit()
            return {"status": 200, "message": "Message sended sucessfully"}

    class TablePortfolio:
        @staticmethod
        def text() -> str:

            return markdown.markdown(Portfolio.query.all()[0].text)
