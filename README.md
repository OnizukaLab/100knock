# Welcome to NLP
鬼塚研究室荒瀬班へようこそ．ここでは自然言語処理に興味があるみなさんを対象に，自然言語処理の基礎的なコーディングを学んでもらいます．

教材URL: http://www.cl.ecei.tohoku.ac.jp/nlp100/

## getting start
   ```
$ git clone -b <yyyy> https://github.com/OnizukaLab/100knock.git
$ cd 100knock/
$ git config user.name <user name>
$ git config user.email <user address>
$ git config --list
$ git branch <name>-<chapter number>
$ git checkout <name>-<chapter number>
$ git branch
$ cd <yyyy>/<name>
```
`$ git config --list` では git の config 一覧が表示されます． `user.email` が正しいアドレスになっていることを確認してください．
`$ git branch` では branch の一覧が表示されます．`<name>-<chapter number>` が選択されていたら ok です．

## ディレクトリ構成
> 100knock/
>> 2018/
>>> ashihara/
>>>
>>> tanaka/
>>>
>>> nomoto/
>>>
>>> ：
>>
>> 2019/

みなさんはローカルリポジトリの `100knock/<yyyy>/<name>` で自由に作業をしてください．章ごとにディレクトリを分け，問題番号をファイル名に明記することを推奨します．

## 100本ノックの進め方
1. メンター側で `<name>-<chapter number>` という名前の issue を立てておきます．issue の説明文は問題番号が箇条書きになっています．
チェックボックスになっているので，好きに使ってください．
2. リモートリポジトリの `Issues` から該当の issue を開いて，`Assignees` を自分にします．
最初は `Assignees` がメンターになっています．ここのcheckを外して，自分にcheckを入れてください．
3. ローカルリポジトリで， `<name>-<chapter number>` branch を作成し checkout してください．
4. 問題をといてください．何かあれば，リモートリポジトリの issue ページで @<mentor name> をつけてコメントしてください．
5. 問題が解けたら，そのファイルをステージングしてください．`$ git add <file>` 
 で行えます．ただし，データは add しないでください．git は大きなデータを管理するようには設計されておらず，めちゃくちゃ動作が重くなります． 
6. `$ git status` で add したファイルが合っているかを確認してください．
間違って add したファイルがある場合は `$ git rm --cached <file>` で取り消すことができます．
7. `$ git commit -m <comment>` でコミットしてください．add したファイルの変更（新規作成を含む）が反映されます．
 `<comment>` には，変更内容を一言でわかりやすく書いてください．一言で書ききれないほど変更がある場合は，複数回に分けてコミットしてください．
8. `$ git log` で過去のコミットが新しい順で表示されます．最新のコミットがさっきのになっていたら ok です．
9. `$ git push origin <name>-<chapter number>` でコミットがリモートリポジトリに反映されます．
10. リモートリポジトリの `Pull requests` を開いて `New pull request` を押してください．プルリク作成画面が表示されますので，
`base:<yyyy>`， `compare:<name>-<chapter number>` を選択し変更が正しいことを確認して
 `Create pull request` を押してください．
11. プルリクのタイトル，説明文を書いて，`Assignees` を自分に，`Reviewer` をメンターに設定してください．
説明文には@<mentor name>をつけて，issue 番号を明記すると良いでしょう．
12. リモートリポジトリの issue で `Assignees` を自分からメンターに変更してください．
13. メンターが変更を確認し，問題がなければマージして issue を閉じ，お知らせします．
問題があればそれをコメントしますので， `Assignees` をメンターから自分に変えて，4. に戻って作業してください．
14. リモートリポジトリの `<yyyy>` ブランチに変更がマージされたことを確認したら，これをローカルリポジトリに反映してください．
以下のコマンドでできます．
```
$ git checkout <yyyy>
$ git pull origin <yyyy>
```
ディレクトリ構成などをみて，正しく反映されていることを確かめてください．

15. 不要になった `<name>-<chapter number>` ブランチを削除します．
```
$ git branch --delete <name>-<chapter number>
$ git push origin :<name>-<chapter number>
```
前者はローカルリポジトリのブランチ削除，後者はリモートリポジトリのブランチ削除です．



手順は以上です．100本ノックは基本的に1週1章ずつ進めていきます．重い章は2週に分けて行います．
メンターは参加者1人に対し必ず1人つきます．言語は自由ですが，メンターと相談してください．私はC++は見れません．

また，毎週1回，みんなで集まって答え合わせをします．担当者が解答例や次週のヒントなどを発表します．
一番最初の集まりで発表担当者を決めたり，メンターと参加者のマッチングを行ったりするので，できるだけ参加してください．
