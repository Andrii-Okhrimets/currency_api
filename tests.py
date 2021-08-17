from app import client


def test_get():
    res = client.get('/filters')

    assert res.status_code == 200


def test_post():
    date = {
        'id': '1',
        'current': 'UAH'
    }

    res = client.post('/', json=date)

    assert res.status_code == 200

    assert res.get_json()[-1]['current'] == date['current']
