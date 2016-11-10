import time
from redis import Redis
from rq import Queue
from util import count_words_at_url


def main():
    q = Queue(connection=Redis())

    job = q.enqueue(count_words_at_url, 'http://nvie.com')
    print(job.result)

    time.sleep(3)
    print(job.result)


if __name__ == '__main__':
    main()
