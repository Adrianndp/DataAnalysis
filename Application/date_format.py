from datetime import datetime, timedelta


def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')


def get_date_day(days_ago):
    date_with_time = datetime.now() - timedelta(days=days_ago)
    return date_with_time.strftime('%Y-%m-%d')


def get_date_month(months_ago):
    date_with_time = datetime.now() - timedelta(days=months_ago * 30)
    return date_with_time.strftime('%Y-%m-%d')


def get_date_year(years_ago):
    date_with_time = datetime.now() - timedelta(days=years_ago * 365)
    return date_with_time.strftime('%Y-%m-%d')

