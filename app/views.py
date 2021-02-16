import os
from urllib.parse import urlparse
from smtplib import SMTPRecipientsRefused

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
    make_response,
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


# Sitemap


@app.route("/sitemap")
@app.route("/sitemap/")
@app.route("/sitemap.xml")
def sitemap():

    host_components = urlparse(request.host_url)
    host_base = host_components.scheme + "://" + host_components.netloc
    s_urls = []
    d_urls = []
    for rule in app.url_map.iter_rules():
        url = {"loc": f"{host_base}{str(rule)}"}
        s_urls.append(url)

    for post_title in DB_Handler.TablePost.all_title():
        url = {
            "loc": f"{host_base}/post/{post_title}",
            "lastmod": DB_Handler.TablePost.query_by_title(post_title)["timestamp"],
        }
        d_urls.append(url)

    xml_sitemap = render_template(
        "public/sitemap.xml", static_urls=s_urls, dynamic_urls=d_urls
    )
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response


# Robots.txt


@app.route("/robots.txt")
def robots():
    ro = render_template("public/robots.txt")
    response = make_response(ro)
    response.headers["Content-Type"] = "text/plain"

    return response


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
    return render_template(
        "html/posts.html",
        posts=DB_Handler.TablePost.all_query(),
        content="Yogeshwaran's Blogs",
        title="Blogs - YOGESHWARAN R",
    )


@app.route("/post")
def post():
    """
    Route for post with particular id
    id from the url params
    """

    id_ = request.args.get("id")
    if id_ in DB_Handler.TablePost.all_id():
        title = DB_Handler.TablePost.title_by_id(id_)
        return render_template(
            "html/post.html",
            post=DB_Handler.TablePost.query_by_id(id_),
            title=title,
            content=title
        )
    else:
        return page_not_found(404)


@app.route("/post/<title>")
def post_title(title):
    """
    Route for post with particular Title
    """

    if title in DB_Handler.TablePost.all_title():
        return render_template(
            "html/post.html",
            post=DB_Handler.TablePost.query_by_title(title),
            content=title,
            title=title,
        )
    else:
        return page_not_found(404)


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
    return render_template(
        "html/contact.html",
        content="Contact Yogeshwaran",
        title="Contact - YOGESHWARAN R",
    )


@app.route("/projects")
def projects():
    """ Route path for projects """
    return render_template(
        "html/projects.html",
        repos=github_repo("yogeshwaran01"),
        content="Projects of Yogeshwaran",
        title="Projects - YOGESHWARAN R",
    )


# Error Handling


@app.errorhandler(404)
def page_not_found(e):
    """ Handling page_not_found 404 error """
    return (
        render_template(
            "html/error.html",
            code=404,
            message_1="Sorry, You are Lost",
            message_2="Page is not available",
            title="404",
        ),
        404,
    )


@app.errorhandler(500)
def internal_server_error(e):
    """ Handling internal_server_error 500 error """
    return (
        render_template(
            "html/error.html",
            code=500,
            message_1="Internal Server Error",
            message_2="Sorry for this problem! we clear it ASAP",
            title="505",
        ),
        404,
    )
