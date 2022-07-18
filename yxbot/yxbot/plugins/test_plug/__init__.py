import nonebot
from nonebot import on_command, logger
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment
from . import test_xq

xq=on_command("徐迁", aliases={"xq","六十"}, priority=2, block=True)
zyx=on_command("赵云霄", priority=2,block=True)


@xq.handle()
async def _(bot: Bot, event: MessageEvent):
    await xq.send(message="是猴")


@zyx.handle()
async def _(bot: Bot, event: MessageEvent):
    await xq.send(message="是你爹")
