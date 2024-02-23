from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    admin_id: int

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
            admin_id=env('ADMIN_ID')
        ),
        group_id=int(env('GROUP_ID'))
    )