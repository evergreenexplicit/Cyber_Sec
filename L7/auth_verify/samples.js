var mime_samples = [
  { 'mime': 'application/xhtml+xml', 'samples': [
    { 'url': 'http://127.0.0.1:8000/', 'dir': '_m0/0', 'linked': 2, 'len': 848 },
    { 'url': 'http://127.0.0.1:8000/accounts/', 'dir': '_m0/1', 'linked': 5, 'len': 6371 },
    { 'url': 'http://127.0.0.1:8000/accounts/login/', 'dir': '_m0/2', 'linked': 5, 'len': 959 },
    { 'url': 'http://127.0.0.1:8000/accounts/login/', 'dir': '_m0/3', 'linked': 5, 'len': 1109 },
    { 'url': 'http://127.0.0.1:8000/accounts/password_reset/done/', 'dir': '_m0/4', 'linked': 2, 'len': 679 },
    { 'url': 'http://127.0.0.1:8000/register', 'dir': '_m0/5', 'linked': 5, 'len': 2193 } ]
  }
];

var issue_samples = [
  { 'severity': 2, 'type': 30601, 'samples': [
    { 'url': 'http://127.0.0.1:8000/accounts/password_reset/', 'extra': '', 'sid': '0', 'dir': '_i0/0' } ]
  },
  { 'severity': 0, 'type': 10602, 'samples': [
    { 'url': 'http://127.0.0.1:8000/accounts/login/', 'extra': '', 'sid': '0', 'dir': '_i1/0' },
    { 'url': 'http://127.0.0.1:8000/accounts/login/', 'extra': '', 'sid': '0', 'dir': '_i1/1' },
    { 'url': 'http://127.0.0.1:8000/accounts/login/', 'extra': '', 'sid': '0', 'dir': '_i1/2' },
    { 'url': 'http://127.0.0.1:8000/accounts/login/', 'extra': '', 'sid': '0', 'dir': '_i1/3' },
    { 'url': 'http://127.0.0.1:8000/register', 'extra': '', 'sid': '0', 'dir': '_i1/4' } ]
  },
  { 'severity': 0, 'type': 10205, 'samples': [
    { 'url': 'http://127.0.0.1:8000/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i2/0' },
    { 'url': 'http://127.0.0.1:8000/accounts/login/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i2/1' },
    { 'url': 'http://127.0.0.1:8000/accounts/password_reset/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i2/2' } ]
  },
  { 'severity': 0, 'type': 10204, 'samples': [
    { 'url': 'http://127.0.0.1:8000/', 'extra': 'X-Frame-Options', 'sid': '0', 'dir': '_i3/0' } ]
  },
  { 'severity': 0, 'type': 10202, 'samples': [
    { 'url': 'http://127.0.0.1:8000/', 'extra': 'WSGIServer/0.2 CPython/3.6.8', 'sid': '0', 'dir': '_i4/0' } ]
  }
];

