# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cryptronics', 'cryptronics.coins']

package_data = \
{'': ['*'],
 'cryptronics': ['.mypy_cache/*',
                 '.mypy_cache/3.9/*',
                 '.mypy_cache/3.9/Cryptronics/*',
                 '.mypy_cache/3.9/_typeshed/*',
                 '.mypy_cache/3.9/collections/*',
                 '.mypy_cache/3.9/ctypes/*',
                 '.mypy_cache/3.9/email/*',
                 '.mypy_cache/3.9/http/*',
                 '.mypy_cache/3.9/importlib/*',
                 '.mypy_cache/3.9/importlib/metadata/*',
                 '.mypy_cache/3.9/json/*',
                 '.mypy_cache/3.9/logging/*',
                 '.mypy_cache/3.9/os/*',
                 '.mypy_cache/3.9/requests/*',
                 '.mypy_cache/3.9/urllib/*',
                 '.mypy_cache/3.9/urllib3/*',
                 '.mypy_cache/3.9/urllib3/contrib/*',
                 '.mypy_cache/3.9/urllib3/packages/*',
                 '.mypy_cache/3.9/urllib3/packages/ssl_match_hostname/*',
                 '.mypy_cache/3.9/urllib3/util/*']}

install_requires = \
['bit>=0.8.0,<0.9.0',
 'bitcoin>=1.1.42,<2.0.0',
 'kucoin-python>=1.0.11,<2.0.0',
 'litecoin-utils>=0.5.4,<0.6.0',
 'monero>=1.1.1,<2.0.0',
 'python-dogecoin>=0.0.4,<0.0.5',
 'tronapi>=3.1.6,<4.0.0']

setup_kwargs = {
    'name': 'cryptronics',
    'version': '1.4',
    'description': 'Easy to use crypto API for python.',
    'long_description': '# Что это?\nCryptronics - это удобная и простая Python обёртка для криптовалютных API сервисов:\n- octopusapisoftware.com (usdt TRC20)\n- cryptocurrencyapi.net (btc, ltc, doge, dash, bch)\n- etherapi.net (eth)\n- bnbapi.net (bnb)\n\n# Как этим пользоваться?\nВыше был приведен список сервисов, а так же список поддерживаемых ими монет.\nВам необходимо зарегистрировать аккаунты в зависимости от необходимых вам монет и сгенерировать API ключи в личном кабинете каждого из сервисов.\n\n## Импорт и настройка\nДля начала работы необходимо импортировать класс Crypto и инициализировать его, передав в качестве параметров Ваши ключи. Обратите внимание, что передавать все ключи не обязательно, можете указывать только для необходимых Вам сервисов.\n``` python\nfrom Cryptronics.base_crypto import Crypto\n\ncrypto = Crypto(\n    octopus_api_key=\'<Ваш API ключ>\',\n    crypto_api_key=\'<Ваш API ключ>\',\n    eth_api_key=\'<Ваш API ключ>\',\n    bnb_api_key=\'<Ваш API ключ>\',\n)\n```\n## Доступные методы\n### create_wallet(token, tag)\nВ качестве параметров принимает:\n- *token - тикер токена, под который нужно создать кошелек (usdt, btc, etc...)\n- *tag - метка, идентификатор. Нужна для идентификации операции в апи сервисе\n\nНиже приведен пример создания кошелька для пользователя, где в качестве тэга используется строка с вставленным в неё ID пользователя\n``` python\nresponse = crypto.create_wallet(\n    "usdt",\n    f"user-wallet-{user_id}"\n)\n```\nВ response вернется словарь (dict) с адресом только что созданного кошелька и иной информацией в зависимости от задействованного API сервиса\n\n### send(token, to_address, amount, tag)\n`Токены будут отправлены с Вашего ОСНОВНОГО кошелька. Подробнее о принципах работы системы можете почитать в документации к octopusapisoftware или cryptocurrency`\nВ качестве параметров принимает:\n- *token - тикер токена, под который нужно создать кошелек (usdt, btc, etc...)\n- *to_address - адрес для отправки токенов (с основного кошелька)\n- *amount - Кол-во монет для отправки\n- tag - метка, идентификатор. Нужна для идентификации кошелька в апи сервисе\n- mix - Отправлять монеты через миксер (True/False)\n\nНиже приведен пример вывода средств пользователю вашей системы. В качестве аргументов передан токен usdt, адрес пользователя стандарта `TRC20`, сумма и тэг \n``` python\nresponse = crypto.send(\n    token="usdt",\n    to_address="<USDT-TRC20-ADDRESS>",\n    amount=200,\n    tag=f"user-withdraw-{user_id}-{operation_id}"\n)\n```\nВ response вернется словарь (dict) с ID вашей транзакции в блокчейн сети и иной информацией в зависимости от задействованного API сервиса.\n\n### generate_wallets(tokens, tag)\n\nВ качестве параметров принимает:\n- tokens - список (list) тикеров валют, для которых необходимо создать кошельки\n- tag - уникальный тэг, для отслеживания операции в API сервисе (желательно включать в него id пользователя внутри вашей системы)\n\nНиже приведен пример генерации кошельков по всем доступным API сервисам \n``` python\ntokens = [\n    \'usdt\',\n    \'btc\',\n    \'eth\'\n]\nresponse = crypto.generate_wallets(\n    tag=f"transit-{user.id}",\n    tokens=tokens\n)\n```\n\nВернется список (list), в котором будут находится сгенерированные кошельки.\n```\n[\n    {\n        "token":"usdt",\n        "wallet":"<wallet_address>"\n    },\n    {\n        "token":"btc",\n        "wallet":"<wallet_address>"\n    },\n    {\n        "token":"eth",\n        "wallet":"<wallet_address>"\n    }\n]\n\n```\n\n# TODO:\n- ~~Возможность сгенерировать кошельки по нескольким валютам, для которых указан токен~~\n- Возможность отправки монет с использованием крипто-миксера (через биржи)\n- Возможность получить баланс кошелька, указав токен или сервис \n- Добавить возможность отслеживать количество подтверждений транзакции в блокчейн сети\n- Возможность отслеживать ожидаемое пополнение фиксированной, заранее известной суммы',
    'author': 'vsaverin',
    'author_email': 'vasiliy.saverin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
