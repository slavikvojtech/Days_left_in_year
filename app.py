from flask import Flask, render_template
from datetime import date
import calendar

app = Flask(__name__)


def get_today():
    """Return today's date."""
    return date.today()


def get_day_of_year(today):
    """Return today's day number in the year (1-365/366)."""
    return int(today.strftime("%j"))


def get_days_in_year(today):
    """Return number of days in the year (365/366)."""
    return 366 if calendar.isleap(today.year) else 365


def get_days_left(days_in_year, day_of_year):
    """Return days left until end of year."""
    return days_in_year - day_of_year


@app.route("/")
def home():
    today = get_today()
    year = today.year

    day_of_year = get_day_of_year(today)
    days_in_year = get_days_in_year(today)
    days_left = get_days_left(days_in_year, day_of_year)

    return render_template(
        "index.html",
        year=year,
        day_of_year=day_of_year,
        days_in_year=days_in_year,
        days_left=days_left

    )


if __name__ == "__main__":
    app.run(debug=True)
