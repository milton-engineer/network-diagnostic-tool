import subprocess

HOSTS = [
    "8.8.8.8",
    "google.com",
    "github.com",
]


def ping_host(host):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", host],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"[OK] {host} is reachable")
        else:
            print(f"[WARNING] {host} is unreachable")

    except Exception as error:
        print(f"[ERROR] Failed to ping {host}: {error}")


def main():
    print("Network Diagnostic Tool")
    print("-" * 40)

    for host in HOSTS:
        ping_host(host)


if __name__ == "__main__":
    main()
