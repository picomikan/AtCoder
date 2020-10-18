import sys
import re

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
                            print("B_question: [a, b, c, d, e] =", a, b, c, d, e, file=sys.stderr)
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

    return 0, {'A':a, 'B':b, 'C':c, 'D':d, 'E':e}

def start_qa(qdata, Q):
    '''
    5個を7回で並び替える問題をインタラクティブに出題

    Args:
        {'A':a, 'B':b, 'C':c, 'D':d, 'E':e}
        Q: クエリの上限回数

    Returns:
        rc  : 0 = 正常 / それ以外 = 異常
    
    '''

    N = len(qdata)  # 個数

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

        cmd, *str = re.split(' ', line)

        if cmd == '?':
            # Query
            print('B_question: Query', *str, file=sys.stderr)

            if len(str) != 2:
                print('B_question: Query format error', file=sys.stderr)
                return -1
            
            for c in str:
                if c not in qdata.keys():
                    print('B_question: Wrong character =', c, file=sys.stderr)
                    return -1
            
            if str[0] == str[1]:
                print('B_question: Wrong character =', str[1], file=sys.stderr)
                return -1
            
            count += 1

            # Reply for Query
            if qdata[str[0]] < qdata[str[1]]:
                print('<', flush=True) 
            elif qdata[str[0]] > qdata[str[1]]:
                print('>', flush=True) 
            else:
                print('B_question: Compare failed.', *str, file=sys.stderr)
                return -1
        
        elif cmd == '!':
            # Answer
            print('B_question: Ans', *str, file=sys.stderr)
        
            if len(str) != 1:
                print('B_question: Answer format error', file=sys.stderr)
                return -1

            # Test Answer
            ans = str[0]
            if len(ans) != N:
                print('B_question: Answer format error', file=sys.stderr)
                return -1

            for i in range(N):
                c = ans[i:(i+1)]
                if qdata[c] != i:
                    print('B_question: Wrong Answer !!', file=sys.stderr)
                    return -1
            
            if count > Q:
                print('B_question: Query count over... count=', count, file=sys.stderr)
                return -1

            print('B_question: Accepted !!', file=sys.stderr)
            return 0
        
        else:
            # Unknown command
            print('B_question: Unknown command =', cmd, file=sys.stderr)
            return -1


if __name__ == '__main__':
    rc = 0

    if len(sys.argv) < 2:
        print('Usage: ' + sys.argv[0] + ' {n}', file=sys.stderr)
        print('\tn: seed value(0...119)', file=sys.stderr)
        sys.exit(rc)

    rc, qdata = make_question(int(sys.argv[1]))
    if rc != 0:
        sys.exit(rc)

    start_qa(qdata, 7)

    sys.exit(rc)
    
