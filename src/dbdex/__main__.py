import asyncio

import logfire

from dbdex.cli.args import get_cli_args
from dbdex.cli.run import run

args = get_cli_args()

# Configure logging

logfire.configure(send_to_logfire="if-token-present", console=None if args.debug else False)

asyncio.run(
    run(
        db_uri=args.db_uri,
        model_name=args.model,
        api_key=args.api_key,
        max_return_values=args.max_return_values,
        stream=args.stream,
    )
)
