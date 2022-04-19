N = 0
P = {}


def updateCurrent(spno, seno, rpno, reno):
    if reno > 1:
        P[rpno][reno] = max(P[rpno][reno-1]+1, P[spno][seno] + 1)
    else:
        P[rpno][reno] = P[spno][seno] + 1


def updateRest(rpno, reno):
    for i in range(reno, len(P[rpno])):
        P[rpno][i+1] = max(P[rpno][i] + 1, P[rpno][i+1])


def display():
    print('\n')
    print('Result of Lamport Logical Clock:')
    for i in range(1, N+1):
        print(f'P{i} -->', end=' ')
        for j in range(1, len(P[i])+1):
            print('---', P[i][j], end='')
        print('\n')


def run():
    inc = 0
    global N
    N = int(input("Enter the number of processes: "))
    for i in range(1, N+1):
        ni = int(input("Enter the no. of events in Process {} : ".format(i)))
        ei = [j for j in range(1, ni + 1)]
        P[i] = {key: inc + key for key in ei}
        print(P[i])
    comm = int(input("Enter the no of communication lines : "))
    while inc < comm:
        sent = int(input("Enter the sending process number : "))
        recv = int(input("Enter the receiving process number : "))
        sent_event_no = int(input("Enter the sending event number : "))
        recv_event_no = int(input("Enter the receiving event number : "))

        print("P{}({}) --> P{}({})".format(sent,
              sent_event_no, recv, recv_event_no))
        updateCurrent(sent, sent_event_no, recv, recv_event_no)
        updateRest(recv, recv_event_no)
        inc += 1


if __name__ == '__main__':
    run()
    display()
