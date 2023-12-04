from django.shortcuts import render

import datetime

def practice(request):
    d = {
        'val': 4,
        'str_val': "i'm Hasib",
        'str_val2': "I Am Hasib",
        'dflt_val': '',
        'f_size' : 123456789,
        'lst_item' : ['a', 'b', 'c', 'd', 'e', 'f'],
        'l_number' : 'one\ntwo\nthree',
        'lst_val': [
            {'name': 'Tuhin', 'age': 24},
            {'name': 'Hasib', 'age': 21},
            {'name': 'Shikhan', 'age': 31},
        ],
        'date_val': datetime.datetime.now(),  # For date-related filters
        'blog_date': datetime.date(2006, 6, 1),
        'comment_date': datetime.datetime(2006, 6, 1, 8, 0),
        'title_val': "my FIRST post",
        'var': ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
    }
    return render(request, 'practice.html', d)  