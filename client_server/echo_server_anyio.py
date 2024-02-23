from anyio import create_tcp_listener, run, sleep


async def handle_echo(client) -> None:
    async with client:
        message = await client.receive(100)
        addr = "test"
        # addr = writer.get_extra_info('peername')
        print(f"Received {message!r} from {addr!r}")

        # Wait a bit before replying
        await sleep(2)

        # Reply
        print(f"Send: {message!r}")
        await client.send(message)


async def main() -> None:
    # start a server that does the above function
    listener = await create_tcp_listener(local_port=8888)
    print(f"Starting server {listener}")
    await listener.serve(handle_echo)


run(main, backend="trio")
