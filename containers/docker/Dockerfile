# Dockerイメージをビルドするための命令を含むテキストファイル．
# Dockerfileには，
# ベースイメージの指定，必要なパッケージのインストール，ファイルのコピー，
# 環境変数の設定，コンテナ起動時に実行するコマンドなどの手順が記述されている．

FROM python:3.12

# 標準出力とエラー表示に遅延が出ないためのおまじない。デバッグ作業がやりやすくなるらしい
ENV PYTHONUNBUFFERED=1

#仮想環境のロートディレクトリに任意のディレクトリを作成。
# -pがあることで、もし親ディレクトリが存在しなかったら、親も含めて作成してくれる
RUN mkdir -p /app

#仮想環境実行時にアクセスするディレクトリ
WORKDIR /app


RUN apt-get update && apt-get install -y\
    binutils\
    gdal-bin\
    libgdal-dev\
    libproj-dev\
    && rm -rf /var/lib/apt/lists/*

#requirements.txt を任意ディレクトリにコピーしてくれる
COPY containers/requirements/requirements.txt .

# ライブラリのインストール。バージョン齟齬をなくすライブラリを入れている
# requirements.txt の中身を全てインストールしている
RUN pip install --upgrade pip \
    && pip install -r containers/requirements/requirements.txt