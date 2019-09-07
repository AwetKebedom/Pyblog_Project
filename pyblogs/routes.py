###################################################
######                                       ######
######            pyblogs/routes.py           ######
######                                       ######
###################################################

from pyblogs import fake_data, forms
from pyblogs import app
import flask
import datetime


@app.route('/')
@app.route('/home')
def homepage():
    d = datetime.datetime.now()
    current_date = "{}/{}/{}".format(d.day, d.month, d.year)

    return flask.render_template("home.jin", today_date=current_date)


@app.route('/contact')
def contact():
    return flask.render_template("contact.jin")


@app.route('/users')
def users_list():
    return flask.render_template('users_list.jin',
                                 users=fake_data.users)


@app.route('/user_profile/<username>')
def user_profile(username):
    found = None
    for user in fake_data.users:
        if user.username.lower() == username.lower():
            found = user

    if found:
        return flask.render_template('user_profile.jin', user=found)
    else:
        return flask.redirect(flask.url_for('homepage'))


@app.route('/news')
def sport_news():
    news_display = fake_data.news_obj
    return flask.render_template('news.jin', news=news_display)


@app.route('/news/<title>')
def news_fed(title):
    found = None
    for new in fake_data.news_obj:
        if new.title.lower() == title.lower():
            found = new

    if found:

        return flask.render_template('news_detail.jin', news=found)
    else:
        return flask.redirect(flask.url_for('sport_news'))


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form1 = forms.SignupForm()

    if flask.request.method == "GET":
        return flask.render_template("sign-up.jin", form=form1)
    else:
        if form1.validate_on_submit():

            user = fake_data.User(username=form1.username.data,
                                  email=form1.email.data)
            fake_data.users.append(user)
            flask.flash("Welcome, " + form1.username.data)
            return flask.redirect(flask.url_for('homepage'))

        else:
            flask.flash("Invalid Form")
            print('errors of form:', form1.errors)
            return flask.render_template('sign-up.jin', form=form1)


@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    form1 = forms.SigninForm()
    if flask.request.method == 'POST':
        if form1.validate_on_submit():
            added_user = form1.username.data
            print('Added user', added_user)



        else:
            print('Form In-Valid')



        return flask.redirect(flask.url_for('homepage'))

    return flask.render_template('signin.jin', form=form1)
