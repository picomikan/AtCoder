import sys
import re

FULL_MSG = True

def dsp_msg(*s):
    if FULL_MSG:
        print(*s, file=sys.stderr)

def make_question(seed):
    '''
    5個を7回で並び替える問題のうち、指定の一問を作成

    Args:
        seed: 問題番号(0...119) ただし、番号は独自の数え方

    Returns:
        rc  :  0: 正常 / それ以外: 異常
        {'A':a, 'B':b, 'C':c, 'D':d, 'E':e}
            : それぞれ0...4の値。お互いに同じ値にはならない

    '''

    if seed not in range(120):
        print('B_question: seed value is out of range!!', file=sys.stderr)
        return -1, {}
    
    i = 0
    found = False
    for a in range(5):
        for b in range(5):
            if b == a:
                continue
            for c in range(5):
                if c in [b, a]:
                    continue
                for d in range(5):
                    if d in [c, b, a]:
                        continue
                    for e in range(5):
                        if e in [d, c, b, a]:
                            continue
                        
                        if i == seed:
                            #print("B_question: [a, b, c, d, e] =", a, b, c, d, e, file=sys.stderr)
                            found = True
                            break

                        i += 1

                    if found:
                        break
                if found:
                    break
            if found:
                break
        if found:
            break

    s = ''
    for i in range(5):
        if i == a:
            s += 'A'
        if i == b:
            s += 'B'
        if i == c:
            s += 'C'
        if i == d:
            s += 'D'
        if i == e:
            s += 'E'
    
    dsp_msg('B_question: Q No.' + str(seed) + ' Exp:' + s)

    return 0, {'A':a, 'B':b, 'C':c, 'D':d, 'E':e}

def start_qa(seed, qdata, Q):
    '''
    5個を7回で並び替える問題をインタラクティブに出題

    Args:
        seed: 問題番号(0...119) ただし、番号は独自の数え方
        {'A':a, 'B':b, 'C':c, 'D':d, 'E':e}
        Q: クエリの上限回数

    Returns:
        rc  : 0 = 正常 / それ以外 = 異常
    
    '''

    N = len(qdata)  # 個数

    seed_str = ''
    if not FULL_MSG:
        seed_str += 'Q No.' + str(seed) + ' '

    # 問題出力
    print(N, Q, flush=True)

    # クエリ回数
    count = 0

    # インタラクティブ
    while True:
        line = sys.stdin.readline()
        if line == '':
            break

        line = line.replace('\n', '')

        cmd, *s = re.split(' ', line)

        if cmd == '?':
            # Query

            if len(s) != 2:
                dsp_msg('B_question: Query ' + str(count + 1) + ':', *s)
                print('B_question: ' + seed_str + 'Query format error', file=sys.stderr)
                return -1
            
            for c in s:
                if c not in qdata.keys():
                    dsp_msg('B_question: Query ' + str(count + 1) + ':', *s)
                    print('B_question: ' + seed_str + 'Wrong character =', c, file=sys.stderr)
                    return -1
            
            if s[0] == s[1]:
                dsp_msg('B_question: Query ' + str(count + 1) + ':', *s)
                print('B_question: ' + seed_str + 'Wrong character =', s[1], file=sys.stderr)
                return -1
            
            # Reply for Query
            if qdata[s[0]] < qdata[s[1]]:
                dsp_msg('B_question: Query ' + str(count + 1) + ':', s[0] + ' < ' + s[1])
                print('<', flush=True) 
            elif qdata[s[0]] > qdata[s[1]]:
                dsp_msg('B_question: Query ' + str(count + 1) + ':', s[0] + ' > ' + s[1])
                print('>', flush=True) 
            else:
                dsp_msg('B_question: Query ' + str(count + 1) + ':', *s)
                print('B_question: ' + seed_str + 'Compare failed.', *s, file=sys.stderr)
                return -1

            count += 1


        elif cmd == '!':
            # Answer
            dsp_msg('B_question: Ans', *s)
        
            if len(s) != 1:
                print('B_question: ' + seed_str + 'Answer format error', file=sys.stderr)
                return -1

            # Test Answer
            ans = s[0]
            if len(ans) != N:
                print('B_question: ' + seed_str + 'Answer format error', file=sys.stderr)
                return -1

            for i in range(N):
                c = ans[i:(i+1)]
                if qdata[c] != i:
                    print('B_question: ' + seed_str + 'Wrong Answer...', file=sys.stderr)
                    return -1
            
            if count > Q:
                print('B_question: ' + seed_str + 'Query count over... count=', count, file=sys.stderr)
                return -1

            print('B_question: ' + seed_str + 'Accepted !!  (count=' + str(count) + ')', file=sys.stderr)
            return 0
        
        else:
            # Unknown command
            print('B_question: ' + seed_str + 'Unknown command =', cmd, file=sys.stderr)
            return -1

def usage():
    print('Usage: ' + sys.argv[0] + ' {n} [-s]', file=sys.stderr)
    print('\tn : seed value(0...119)', file=sys.stderr)
    print('\t-s: short message', file=sys.stderr)

if __name__ == '__main__':
    rc = 0

    if len(sys.argv) < 2:
        usage()
        sys.exit(rc)

    seed = -1
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '-s':
            FULL_MSG = False
        elif seed == -1:
            seed = int(sys.argv[i])
        
        i += 1
    
    if seed == -1:
        usage()
        sys.exit(-1)

    rc, qdata = make_question(seed)
    if rc != 0:
        sys.exit(rc)

    start_qa(seed, qdata, 7)

    sys.exit(rc)
    
