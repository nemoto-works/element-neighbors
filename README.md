# お隣誰だ？ — Element Neighbors

スマホ向け静的HTMLの周期表左右隣クイズ。18族×7周期の空欄グリッドに問題元素の位置を示し、回答後に正解元素のマスを表示する。

主周期表から分離して描かれるランタノイド・アクチノイドは出題対象外。グリッド上で左右に直接接する元素だけを出題する。

## 起動
`index.html` をブラウザで開く。外部APIやログイン不要。

## テスト
```sh
python3 -m unittest discover -s . -p 'test_*.py' -v
```

上記はHTMLの構造・出題処理の存在を確認する**静的スモークテスト**。正誤の動作、スマホ実機表示、アクセシビリティは別途人間が確認する。

## 公開
GitHub Pages:

https://nemoto-works.github.io/element-neighbors/

この公開リポジトリが開発・保守の正本。`main` ブランチからGitHub Pagesへ配信する。
