# AtCoderのインタラクティブ問題のエミュレータ

[B - Interactive Sorting](https://atcoder.jp/contests/practice/tasks/practice_2)の テストセット3 の最適解を求めるために、エミュレータを自作してみました。

## 内容
* pipeloop.py

第一引数のプログラムの標準出力を第二引数のプログラムの標準入力に渡し、第二引数のプログラムの標準出力を第一引数のプログラムの標準入力に渡します。(パイプ)

いずれかのプログラムが終了するまでそのパイプを続けます。

* B_question

B - Interactive Sorting の問題プログラムの自作エミュレータです。


## 使用方法
$ python pipeloop.py 'python B_question.py n' myprog.exe

* n: 問題番号 0...119 (番号は独自)
* myprog.exe : 問題B用のコードをコンパイルしたもの
