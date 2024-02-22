from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str

@dataclass
class Config:
    tg_bot: TgBot
    group_id: int

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
        ),
        group_id=int(env('GROUP_ID'))
    )