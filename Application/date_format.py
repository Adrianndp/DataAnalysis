from datetime import datetime, timedelta


def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')


def get_date_day(days_ago):
    """
    :param int days_ago: If you want the date of 5 days ago than 5 as parameter
    """
    date_with_time = datetime.now() - timedelta(days=days_ago)
    return date_with_time.strftime('%Y-%m-%d')


def get_date_month(months_ago):
    """
    :param int months_ago: If you want the date of 5 months ago than 5 as parameter
    """
    date_with_time = datetime.now() - timedelta(days=months_ago * 30)
    return date_with_time.strftime('%Y-%m-%d')


def get_date_year(years_ago):
    """
    :param int years_ago: If you want the date of 5 years ago than 5 as parameter
    """
    date_with_time = datetime.now() - timedelta(days=years_ago * 365)
    return date_with_time.strftime('%Y-%m-%d')

