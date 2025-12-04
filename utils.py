from pathlib import Path
import socket
import yaml
import toml


HOSTNAME = socket.gethostname()


def generate_email_from_name(name: str) -> str:
    address = ".".join(name.lower().split())
    return f"{address}@skyworksinc.com"


def check_active(port: int, timeout: float = 1.0) -> bool:
    """TCPコネクションが張れるかを確認（ポートが開いているか）"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((HOSTNAME, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False


def collect_app_info(root_dir: str) -> list[dict]:
    data = []

    info_files = list(Path(root_dir).rglob("info.yaml"))
    for file in info_files:
        # YAMLファイルの読み込み
        with open(file, "r", encoding="utf-8") as f:
            info = yaml.safe_load(f)

        # email を補完
        if not info["email"]:
            name = info.get("developer", "")
            info["email"] = generate_email_from_name(name)

        # .streamlit/config.toml の読み込み
        config_file = file.parent / ".streamlit/config.toml"
        if config_file.exists():
            config = toml.load(config_file)
            port = config.get("server", {}).get("port")
        else:
            port = "unknown"
        info["port"] = port

        url = f"http://{HOSTNAME}:{port}"
        info["url"] = url

        info["status"] = "active" if check_active(info["port"]) else "inactive"

        data.append(info)

    return data
