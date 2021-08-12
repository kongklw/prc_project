from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/home/konglingwen/Desktop", perm="elradfmwMT")
authorizer.add_anonymous("/home/konglingwen/Desktop")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()


# [I 13-02-19 10:55:42] >>> starting FTP server on 127.0.0.1:21 <<<
# [I 13-02-19 10:55:42] poller: <class 'pyftpdlib.ioloop.Epoll'>
# [I 13-02-19 10:55:42] masquerade (NAT) address: None
# [I 13-02-19 10:55:42] passive ports: None
# [I 13-02-19 10:55:42] use sendfile(2): True
# [I 13-02-19 10:55:45] 127.0.0.1:34178-[] FTP session opened (connect)
# [I 13-02-19 10:55:48] 127.0.0.1:34178-[user] USER 'user' logged in.
# [I 13-02-19 10:56:27] 127.0.0.1:34179-[user] RETR /home/giampaolo/.vimrc completed=1 bytes=1700 seconds=0.001
# [I 13-02-19 10:56:39] 127.0.0.1:34179-[user] FTP session closed (disconnect).