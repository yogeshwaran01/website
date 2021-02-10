from typing import Any
import markdown

from .models import db, Posts, Contact, Portfolio


class DB_Handler:
    """
    Class that directly interacts with database
    """

    class TablePost:
        """ Class handele the Post table in db """

        @staticmethod
        def all_query() -> list:
            """
            Method returns lists of all posts from database
            """
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
        def query_by_id(_id: int) -> dict:
            """
            Method returns post for given id from db
            """
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
        def query_by_title(title: str) -> dict:
            """
            Method returns post for given id from db
            """
            post = Posts.query.filter_by(title=title).first()
            if post is None:
                return {"status": 404, "message": "No Post Available"}
            return {
                "title": post.title,
                "body": markdown.markdown(post.body),
                "timestamp": post.timestamp,
                "id": post.id,
            }

        @staticmethod
        def all_id() -> list:
            """
            Method return all id of the post
            """
            return [str(i["id"]) for i in DB_Handler.TablePost.all_query()]

        @staticmethod
        def all_title() -> list:
            """
            Method returns all titles of the posts from db
            """
            return [i["title"] for i in DB_Handler.TablePost.all_query()]

        @staticmethod
        def title_by_id(id_: int) -> str:
            """
            Return the title of the post for given id
            """
            post = Posts.query.filter_by(id=id_).first()
            if post is None:
                return "404"
            return post.title


        @staticmethod
        def PostData(title: str, body: str) -> dict:
            """
            Method add blog posts data to the db
            """
            post = Posts(title=title, body=body)
            db.session.add(post)
            db.session.commit()
            return {"status": 200, "message": "Data Posted successfully"}

    class TableContact:
        """ Class handele the Contact table in db """

        @staticmethod
        def all_query() -> list:
            """
            Method returns lists of all contacts from database
            """
            data = []
            cons = Contact.query.all()
            for con in cons:
                x = {"name": con.name, "email": con.email, "message": con.message}
                data.append(x)
            return data

        @staticmethod
        def PostData(name: str, email: str, message: str) -> dict:
            """
            Method add contact data to the db
            """
            con = Contact(name=name, email=email, message=message)
            db.session.add(con)
            db.session.commit()
            return {"status": 200, "message": "Message sended successfully"}

    class TablePortfolio:
        """ Class handele the Portfolio table in db """

        @staticmethod
        def text() -> Any:
            """ Method return the html string for index """
            return markdown.markdown(Portfolio.query.all()[0].text)
