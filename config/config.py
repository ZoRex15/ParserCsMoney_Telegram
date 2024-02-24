from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    admin_ids: list
@dataclass
class Config:
    tg_bot: TgBot
    group_id: int

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=tuple(map(int, env.list('ADMIN_IDS')))
        ),
        group_id=int(env('GROUP_ID'))
    )