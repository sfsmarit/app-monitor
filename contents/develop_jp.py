import streamlit as st
import socket

import components


nl = "  "
HOST = socket.gethostname()


st.title("Streamlit 開発ガイド")
st.set_page_config(page_title="Streamlit Server", page_icon=":signal_strength:")

# components.render_resouce_usage()
# components.render_available_ports()

st.header("開発の流れ")
st.subheader("1. Streamlit サーバのアカウントを取得", divider=True)
st.markdown(
    f"""
    IT Service Desk{nl}
    https://skyworksinc.atlassian.net/servicedesk/customer/portal/9/group/37/create/229 {nl}
    [Summary]
    Request for login access to {HOST}
       
    DB を使用する場合は、DB へのアクセス権限も別チケットでリクエストしましょう。
    """
)

st.subheader("2. アプリを開発してデプロイする", divider=True)
st.markdown(
    f"""
    こちらのページで詳しく解説しています。{nl}
    https://app-startguide.streamlit.app/
    
    デプロイするときは、ホームディレクトリの直下に `streamlit` ディレクトリを作成し、その配下にアプリを配置してください。
    ```bash
    cd
    mkdir streamlit
    cd streamlit
    git clone https://github.com/<UserName>/sample-app.git
    ```
    
    """
)

st.subheader("3. ポートの固定", divider=True)
st.markdown(
    f"""
    ```bash
    # プロジェクトディレクトリに移動
    cd ~/streamlit/sample-app/
    
    # .streamlit/config.toml を作成
    mkdir .streamlit
    touch .streamlit/config.toml
    ```    
    config.toml を編集してポートを指定します。
    ```toml
    [server]
    port=8650
    ```    
    利用可能なポートについては、このページの上部を参照してください。
    """
)

st.subheader("4. info.yaml の配置", divider=True)
st.markdown(
    f"""
    Streamlit Server のアプリ一覧に情報が表示されるようにします。
    ```bash
    # プロジェクトディレクトリに移動
    cd ~/streamlit/sample-app/

    # info.yaml をコピー
    cp ~/marit/template/info.yaml ./
    ```    
    info.yaml を編集します。
    ```yaml
    port:8650
    ```    

    """
)

st.subheader("5. アプリ起動", divider=True)
st.markdown(
    f"""
    ```bash
    nohup <path_to_your_venv>/bin/streamlit run main.py &
    ```
    > nohup : ログアウトしてもプロセスが残る{nl}
    > & : バックグラウンド実行
    """
)
