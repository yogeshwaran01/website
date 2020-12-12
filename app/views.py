import os

from app import app, database as db, admin, auth
from helper.github_repos import github_repo
from helper.admin_auth import Authenticate
from helper.is_allowed import is_allowed_file
from .db_handeler import DB_Handler
from .models import Posts, Contact, Portfolio
from .config import Configaration


from werkzeug.utils import secure_filename
from flask import (
    jsonify,
    request,
    abort,
    redirect,
    url_for,
    render_template,
    send_from_directory,
    flash,
)

# favicon


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon/favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


# Api of Blog-Post


@app.route("/api/get")
def get_api():
    id_ = request.args.get("id")
    if id_ is None:
        return jsonify(DB_Handler.TablePost.all_query())
    return jsonify(DB_Handler.TablePost.query_by_id(id_))


@auth.required
@app.route("/api/post", methods=["POST"])
def post_api():
    if not request.json:
        abort(400)
    if "title" or "body" not in request.json:
        abort(404)
    data = request.json
    title = data["title"]
    body = data["body"]
    return jsonify(DB_Handler.TablePost.PostData(title, body))


# Admin Panel

admin.add_view(Authenticate(Posts, db.session))
admin.add_view(Authenticate(Contact, db.session))
admin.add_view(Authenticate(Portfolio, db.session))


@auth.required
@app.route("/admin/new", methods=["GET", "POST"])
def cv():
    if request.method == "POST":
        a = request.form.get("md")
        b = request.form.get("title")
        DB_Handler.TablePost.PostData(b, a)
        return redirect("/admin/posts")
    return render_template("admin/post.html")


# Web Frontend


@app.route("/")
def index():
    data = DB_Handler.TablePortfolio.text()
    return render_template("html/index.html", text=data)


@app.route("/posts")
def posts():
    return render_template("html/posts.html", posts=DB_Handler.TablePost.all_query())


@app.route("/post")
def post():
    id_ = request.args.get("id")
    return render_template("html/post.html", post=DB_Handler.TablePost.query_by_id(id_))


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        a = DB_Handler.TableContact.PostData(name, email, message)
        return render_template("html/contact.html", message=a["message"])
    return render_template("html/contact.html")


@app.route("/projects")
def projects():
    return render_template("html/projects.html", repos=github_repo())

# Upload files


@app.route("/view")
def view_image():
    return render_template("html/view.html", images=os.listdir("app/static/uploads"))


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and is_allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(Configaration.UPLOAD_FOLDER, filename))
            return redirect("/view")
    return render_template('html/upload.html')
