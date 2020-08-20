import asyncio
import argparse
import aiohttp
from demo import create_app
from demo.settings import load_config

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print('uvloop does not support Windows at the moment')

parser = argparse.ArgumentParser(description='Demo project')
parser.add_argument('--host', help='Host to listen', default='127.0.0.1')
parser.add_argument('--port', help='Port to accept connections', default=5000)
parser.add_argument('--reload', action='store_true', help='Auto-reload code on change')
parser.add_argument('-c', '--config', type=argparse.FileType('r'), help='Path to configuration file')

args = parser.parse_args()

app = create_app(config=load_config(args.config))

if args.reload:
    print('Start with code reload')
    import aioreloader
    aioreloader.start()


if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port)
