import pymysql

from Kindergarten_django import errors

handler400 = 'django.views.defaults.bad_request'
handler403 = 'django.views.defaults.permission_denied'
handler404 = 'Kindergarten_django.erros.handler400'
handler500 = 'django.views.defaults.server_error'

pymysql.install_as_MySQLdb()
