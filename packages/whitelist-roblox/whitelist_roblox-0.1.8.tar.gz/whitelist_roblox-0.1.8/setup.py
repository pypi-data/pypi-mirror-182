from setuptools import setup

setup(
    name='whitelist_roblox',
    version='0.1.8',    
    description='Whitelist For Roblox Script',
    author='MaGiXx#6964',
    packages=[
        'wl_magixx', 
        'wl_magixx/discordbot',
        'wl_magixx/discordbot/cogs'
    ],
    install_requires=[
        'requests',        
        'disnake'             
    ]
)