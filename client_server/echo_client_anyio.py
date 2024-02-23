import sys

from anyio import connect_tcp, run


async def tcp_echo_client(message: str) -> None:
    async with await connect_tcp("127.0.0.1", 8888) as client:
        print(f"Send: {message!r}")
        await client.send(message.encode())

        data = await client.receive(100)
        print(f"Received: {data.decode()!r}")


if __name__ == "__main__":
    run(tcp_echo_client, sys.argv[1], backend="trio")
