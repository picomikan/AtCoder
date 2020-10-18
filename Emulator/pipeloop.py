import sys
import subprocess


def pipe_loop(cmd1, cmd2):
    '''
    cmd1の標準出力をcmd2の標準入力と繋ぎ、
    cmd2の標準出力をcmd1の標準入力と繋ぐ

    MEMO
    - cmd1が先に標準出力すること。
    - cmd2の標準出力がなくなるまで繰り返す
    '''

#   標準エラー出力をまとめて取り出す場合
#    proc1 = subprocess.Popen(cmd1.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    proc2 = subprocess.Popen(cmd2.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc1 = subprocess.Popen(cmd1.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(cmd2.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    while proc1.poll() is None and proc2.poll() is None:
        # cmd1の標準出力をcmd2の標準入力へ
        line = proc1.stdout.readline()
        print('[1]', line.decode().rstrip(), file=sys.stderr)
        proc2.stdin.write(line)
        proc2.stdin.flush()

        # cmd2の標準出力をcmd1の標準入力へ
        line = proc2.stdout.readline()
        print('[2]', line.decode().rstrip(), file=sys.stderr)
        proc1.stdin.write(line)
        proc1.stdin.flush()

#   標準エラー出力をまとめて取り出す場合
#    serr = proc1.communicate()[1]
#    print(serr.decode().rstrip())
#    serr = proc2.communicate()[1]
#    print(serr.decode().rstrip())
    
    return


if __name__ == '__main__':
    rc = 0

    if len(sys.argv) < 3:
        print('Usage: ' + sys.argv[0] + ' {cmd1} {cmd2}', file=sys.stderr)
    else:
        pipe_loop(sys.argv[1], sys.argv[2])
    
    sys.exit(rc)
