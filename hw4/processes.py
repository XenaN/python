import time
from multiprocessing import Process, Queue, Pipe
from codecs import encode
from datetime import datetime


def put_in_queue(conn, q):
    while True:
        msg = conn.recv()
        if msg:
            if msg == 'stop':
                conn.close()
                break
            q.put(msg.lower())
            time.sleep(5)


def encoder(conn, q):
    while True:
        if not q.empty():
            msg = q.get()
            if msg == 'stop':
                q.close()
                conn.close()
                break
            conn.send(encode(msg, 'rot_13'))


if __name__ == "__main__":
    q = Queue()

    main_conn, A_conn = Pipe()
    p1 = Process(target=put_in_queue, args=(A_conn, q, ))
    p1.start()

    main_conn_2, B_conn = Pipe()
    p2 = Process(target=encoder, args=(B_conn, q, ))
    p2.start()

    with open('artifacts/hard/logging.txt', 'a') as log_file:
        while True:
            msg = input()
            log_file.write(f'{datetime.fromtimestamp(time.time())} {msg} \n')
            if msg:
                main_conn.send(msg)

            if msg == 'stop':
                break
            msg_end = main_conn_2.recv()
            if msg_end:
                print(datetime.fromtimestamp(time.time()), msg_end)
                log_file.write(f'{datetime.fromtimestamp(time.time())} {msg_end} \n')

        p1.join()
        p2.join()
