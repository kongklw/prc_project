from gevent import monkey
import gevent
import requests



def download_img(url, filename):
    s = requests.get(url)
    content = s.content
    print(type(content))


if __name__ == '__main__':
    # monkey.patch_all()

    url1 = "https://pics4.baidu.com/feed/f636afc379310a55c69c07ba5fa7f2a18326102b.jpeg?token=cd31846e690397809e50bfb6c8f9d977"
    url2 = "https://pics4.baidu.com/feed/902397dda144ad3475bf07f3094fbffc30ad85bc.jpeg?token=1872601d9c098a28132c00bd45f7a2a0"
    url3 = "https://pics5.baidu.com/feed/48540923dd54564ef5c129f022152f8ad3584fa3.jpeg?token=2e08ff5c9f2861b0a692fe7fb89ec33f"

    gevent.joinall([
        gevent.spawn(download_img, url1, '1.jpg'),
        gevent.spawn(download_img, url2, '2.jpg'),
        gevent.spawn(download_img, url3, '3.jpg'),

    ])
