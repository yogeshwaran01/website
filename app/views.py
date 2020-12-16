import os

from app import app, database as db, admin, auth
from helper.github_repos import github_repo
from helper.admin_auth import Authenticate
from .db_handeler import DB_Handler
from .models import Posts, Contact, Portfolio


from flask import (
    jsonify,
    request,
    abort,
    redirect,
    render_template,
    send_from_directory,
)

# favicon


@app.route("/favicon.ico")
def favicon():
    """ Route for favicons """
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon/favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


# Api of Blog-Post


@app.route("/api/get")
def get_api():
    """
    Route for JSON api for blog posts

    Method:
    ------
        GET

    Admin Authentication:
    --------------------
        Not Required

    """
    id_ = request.args.get("id")
    if id_ is None:
        return jsonify(DB_Handler.TablePost.all_query())
    return jsonify(DB_Handler.TablePost.query_by_id(id_))


@auth.required
@app.route("/api/post", methods=["POST"])
def post_api():
    """
    Route for post blog_posts in database

    Method:
    ------
        POST

    Admin Authentication:
    --------------------
        Required

    """
    if not request.json:
        abort(400)
    if "title" or "body" not in request.json:
        abort(404)
    data = request.json
    title = data["title"]
    body = data["body"]
    return jsonify(DB_Handler.TablePost.PostData(title, body))


# Admin Panel

# Admin Panel views are created by flask_admin
# Method: GET
# Admin Authentication: Required

admin.add_view(Authenticate(Posts, db.session))
admin.add_view(Authenticate(Contact, db.session))
admin.add_view(Authenticate(Portfolio, db.session))


@auth.required
@app.route("/admin/new", methods=["GET", "POST"])
def cv():
    """
    Route for blog post editor

    Method:
    ------
        POST, GET

    Admin Authentication:
    --------------------
        Required

    """

    if request.method == "POST":
        a = request.form.get("md")
        b = request.form.get("title")
        DB_Handler.TablePost.PostData(b, a)
        return redirect("/admin/posts")
    return render_template("admin/post.html")


# Web Frontend

# All below routes for public views
# No admin authentication is required
# Method: GET


@app.route("/")
def index():
    """ Route for home page """
    data = DB_Handler.TablePortfolio.text()
    return render_template("html/index.html", text=data)


@app.route("/posts")
def posts():
    """ Route for all posts """
    return render_template("html/posts.html", posts=DB_Handler.TablePost.all_query())


@app.route("/post")
def post():
    """
    Route for post with particular id
    id from the url params
    """

    id_ = request.args.get("id")
    return render_template("html/post.html", post=DB_Handler.TablePost.query_by_id(id_))


@app.route("/contact", methods=["POST", "GET"])
def contact():
    """
    Route for Contact page

    Method:
    ------
        POST, GET

    Admin Authentication:
    --------------------
        Not Required

    """

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        a = DB_Handler.TableContact.PostData(name, email, message)
        return render_template("html/contact.html", message=a["message"])
    return render_template("html/contact.html")


@app.route("/projects")
def projects():
    """ Route path for projects """
    return render_template("html/projects.html", repos=github_repo("yogeshwaran01"))
